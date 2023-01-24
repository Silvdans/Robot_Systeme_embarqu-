import random
LEN_GRID=66
def set_emtpy_tab():
    tableau = []
    for i in range(66):
        ligne = []
        for j in range(66):
            ligne.append(0)
        tableau.append(ligne)

    for i in range(66):
        tableau[i][0] = -1
        tableau[i][65] = -1
        tableau[0][i] = -1
        tableau[65][i] = -1
    
    return tableau
def set_tableau():
    tableau = []
    for i in range(66):
        ligne = []
        for j in range(66):
            ligne.append(0)
        tableau.append(ligne)

    # Remplacer au hasard 10 valeurs par des 1
    check = set()
    while len(check) !=900:
        
        x = random.randint(1, 64)
        y = random.randint(1, 64)
        if (x,y) not in check and not (x == 1 and y == 1):
            check.add((x,y))
            tableau[x][y] = -1

    # Ajouter des -1 sur les bordures du tableau
    for i in range(66):
        tableau[i][0] = -1
        tableau[i][65] = -1
        tableau[0][i] = -1
        tableau[65][i] = -1
    
    return tableau
class Robot:
    x, y = 1, 1
    last_case = None
    real_grid = set_tableau()
    prediction_grid = set_emtpy_tab()
    def mark_case_as_seen(self, grid, x, y):
        grid[x][y] = 1

    def mark_wall(self, dir):
        if dir == "right":
            self.prediction_grid[self.x][self.y + 1] = -1
        elif dir == "down":
            self.prediction_grid[self.x + 1][self.y] = -1
        elif dir == "left":
            self.prediction_grid[self.x][self.y - 1] = -1
        elif dir == "up":
            self.prediction_grid[self.x - 1][self.y] = -1
    def is_scan_finished(self):
        for i in range(66):
            for j in range(66):
                if self.prediction_grid[i][j] == 0:
                    return False
        return True
    def can_go_check_last_case(self, dir):
        if dir == "right":
            return not self.last_case ==  (self.x, self.y+1)
        elif dir == "down":
            return not self.last_case ==  (self.x+1, self.y)
        elif dir == "left":
            return not self.last_case ==  (self.x, self.y-1)
        elif dir == "up":
            return not self.last_case ==  (self.x - 1, self.y)

    def _can_walk_to_next_case(self, grid, dir):
        if(not self.can_go_check_last_case(dir)):
            return False
        if dir == "right":
            return grid[self.x][self.y + 1] != -1
        elif dir == "down":
            return grid[self.x + 1][self.y ] != -1
        elif dir == "left":
            return grid[self.x ][self.y - 1] != -1
        elif dir == "up":
            return grid[self.x- 1][self.y ] != -1

    def moveForward(self, dir):
        last_case = (self.x, self.y)
        if dir == "right":
            self.y += 1
        elif dir == "down":
            self.x += 1
        elif dir == "left":
            self.y -= 1
        elif dir == "up":
            self.x -= 1

    def turnRight(self, dir):
        if dir == "right":
            return "down"
        elif dir == "down":
            return "left"
        elif dir == "left":
            return "up"
        elif dir == "up":
            return "right"
    
    def turnLeft(self, dir):
        if dir == "right":
            return "up"
        elif dir == "down":
            return "right"
        elif dir == "left":
            return "down"
        elif dir == "up":
            return "left"
    
    def scan(self, dir = "right"):
        self.mark_case_as_seen(self.prediction_grid, self.x, self.y)
        if(self._can_walk_to_next_case(self.real_grid, dir)):
            self.moveForward(dir)
            self.scan(dir)
        else:
            self.mark_wall(dir)
            self.scan(self.turnRight(dir))
            
        if self.is_scan_finished():
            return self.prediction_grid

def count_1_in_tab_of_tab(tab):
    count = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == -1:
                count += 1
    return count


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




robot = Robot()
tableau = set_tableau()
generate_file(tableau, "vraitable.html")
prediction = robot.scan()
generate_file(prediction, "prediction.html")

print(tableau == prediction)
#I want a function that simulate a robot parcouring the tableau, but the robot dont have the information on the whole tableau, he can look the case in front on him, he can rotate, and he can move forward, write a function that scan the array and return the number of 1 that the robot can see

