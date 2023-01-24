import random

tableau = []
for i in range(66):
    ligne = []
    for j in range(66):
        ligne.append(0)
    tableau.append(ligne)

# Remplacer au hasard 10 valeurs par des 1
for i in range(600):
    x = random.randint(0, 65)
    y = random.randint(0, 65)
    tableau[x][y] = 1

# Ajouter des -1 sur les bordures du tableau
for i in range(66):
    tableau[i][0] = -1
    tableau[i][65] = -1
    tableau[0][i] = -1
    tableau[65][i] = -1

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

f = open("tableau.html", "w")

# Écrire la chaîne HTML dans le fichier
f.write(html)

# Fermer le fichier
f.close()