import copy
import random
LEN_GRID_DEFAULT = 66

def set_emtpy_tab(grid_lenght):
    tableau = []
    for i in range(grid_lenght):
        ligne = []
        for j in range(grid_lenght):
            ligne.append(0)
        tableau.append(ligne)

    for i in range(grid_lenght):
        tableau[0][0] = -1
        tableau[0][grid_lenght - 1] = -1
        tableau[grid_lenght - 1][0] = -1
        tableau[grid_lenght - 1][grid_lenght - 1] = -1
    
    return tableau
def set_tableau(grid_lenght, number_of_wall = 100):
    tableau = []
    for i in range(grid_lenght):
        ligne = []
        for j in range(grid_lenght):
            ligne.append(0)
        tableau.append(ligne)

    # Remplacer au hasard 10 valeurs par des 1
    check = set()
    while len(check) != number_of_wall:
        
        x = random.randint(2, grid_lenght - 3)
        y = random.randint(2, grid_lenght - 3)
        if (x,y) not in check and not (x == 1 and y == 1):
            if tableau[x-1][y] != -1 or tableau[x+1][y] != -1 or tableau[x][y-1] != -1 or tableau[x][y+1] != -1: #Empecher que une case soit enfermée de murs
                check.add((x,y))
                tableau[x][y] = -1

    # Ajouter des -1 sur les bordures du tableau
    for i in range(grid_lenght):
        tableau[i][0] = -1
        tableau[i][grid_lenght - 1] = -1
        tableau[0][i] = -1
        tableau[grid_lenght - 1][i] = -1
    
    return tableau

def replace_all_0_by_1(tableau):
    copy_tab = copy.deepcopy(tableau)
    for i in range(len(tableau)):
        for j in range(len(tableau)):
            if copy_tab[i][j] == 0:
                copy_tab[i][j] = 1
    return copy_tab

class Robot:
    x, y = 1, 1
    grid_lenght = 0
    real_grid : list = None 
    prediction_grid : list = None
    direction = ""
    visited_walls = None
    counter = 1
        
    def __init__(self, grid_lenght, read_grid = None):
        self.grid_lenght = grid_lenght
        if not read_grid:
            self.real_grid = set_tableau(grid_lenght)
        else:
            self.real_grid = read_grid
        self.prediction_grid = set_emtpy_tab(grid_lenght)
        self.prediction_grid[1][1] = 1
        self.direction = random.choice(["right", "left", "up", "down"])
        self.visited_walls = set()
    
    def get_next_coordinates(self):
        if(self.direction == "right"):
            return self.x, self.y + 1
        elif(self.direction == "left"):
            return self.x, self.y - 1
        elif(self.direction == "up"):
            return self.x - 1, self.y
        elif(self.direction == "down"):
            return self.x + 1, self.y
    def update_direction(self):
        return random.choice(["right", "left", "up", "down"])
    
    def can_move(self, coordinates : tuple):
        x, y = coordinates
        return self.real_grid[x][y] != -1
   
    def mark_case_as_visited(self, coordinates : tuple):
        x, y = coordinates
        self.counter += 1
        self.prediction_grid[x][y] = 1
    
    def is_scan_complete(self):
        return self.counter == ((self.grid_lenght * self.grid_lenght) - 4)
    
    def update_coordinates(self, coordinates : tuple):
        self.x, self.y = coordinates
        if self.prediction_grid[self.x][self.y] == 0:
            self.mark_case_as_visited(coordinates)

    def mark_wall(self, coordinates : tuple):
        x, y = coordinates
        if(coordinates not in self.visited_walls):
            self.visited_walls.add(coordinates)
            self.counter += 1
            self.prediction_grid[x][y] = -1
        
    def scan(self):
        while(not self.is_scan_complete()):
            next_coordinates = self.get_next_coordinates()
            if self.can_move(next_coordinates):
                self.update_coordinates(next_coordinates)
            else:
                self.mark_wall(next_coordinates)
            self.direction = self.update_direction()
            
        return self.prediction_grid
        
def generate_file(tableau, filename):
    html = "<style>td { padding: 10px; border: 1px solid black; } td.negatif { background-color: red; } td.un { background-color: orange; }</style><table>"
    for ligne in tableau:
        html += "<tr>"
        for valeur in ligne:
            if valeur == -1:
                html += "<td class='negatif'>" + str(valeur) + "</td>"
            elif valeur == 1:
                html += "<td class='un'>" + str(valeur) + "</td>"
            else:
                html += "<td>" + str(valeur) + "</td>"
        html += "</tr>"
    html += "</table>"

    f = open(filename, "w")

    # Écrire la chaîne HTML dans le fichier
    f.write(html)

    # Fermer le fichier
    f.close()

