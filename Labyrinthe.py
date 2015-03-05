empty=" "
wall="0"
start="A"
end="B"
visited="-"
good="x"


LABYRINTH = """
0000000000000000000000000000000000000000000000000000000000000
A        0              0        0        0     0           0
0  0000  0000  0000000  0  0000  0  0000  0  0  0  0000000  0
0  0  0     0  0     0  0     0     0  0  0  0  0  0        0
0  0  0000  0  0000  0  0  0  0000000  0  0000  0000  0000000
0  0     0     0     0  0  0  0        0     0  0     0     0
0  0000  0  0000  0000  0000  0  0000000000  0  0  0000  0000
0  0     0     0     0  0     0  0     0  0     0  0        0
0  0  0000000000000  0  0  0000  0  0  0  0000000  0000  0  0
0        0        0              0  0     0        0     0  0
0000  0000  0  0000000  0  0000000  0000  0  0000000  0000  0
0     0     0  0        0  0        0     0  0        0     0
0  0000  0000000  0000000  0  0000000  0000  0  0000000  0000
0  0              0           0     0     0     0           0
0000  0000000000000  0000000000  0  0000  0000  0  0000000000
0     0           0     0     0  0     0        0  0        0
0  0000  0000000  0  0  0  0  0000000  0000000000  0  0000  0
0     0  0        0  0     0  0        0        0  0  0     0
0000  0000  0000000000000000  0  0000000  0000  0  0  0  0000
0  0  0     0                 0  0     0  0     0     0     0
0  0  0  0000  0000000000000000  0  0  0  0000000000000  0  0
0  0  0     0  0     0        0  0  0     0           0  0  0
0  0  0  0  0  0  0  0  0000  0  0  0000000  0000000  0  0  0
0  0  0  0  0     0  0  0     0  0     0     0     0     0  0
0  0  0000  0000000  0  0000000  0000  0000  0  0  0000000  0
0     0           0  0     0  0     0           0  0     0  0
0  0000  0000000000  0000  0  0  0  0000000  0000  0  0  0  0
0                 0  0     0     0  0        0     0  0  0  0
0000000000000000  0  0  0000000000  0  0000000  0000000  0  0
0     0           0     0        0  0  0     0           0  0
0  0000  0000000000  0000  0  0000  0  0  0000000000000000  0
0        0        0  0     0        0  0                 0  0
0000000000  0  0  0  0  0  0000000000  0000000000000000  0  0
0           0  0  0  0  0                 0                 0
0  0000000000  0000  0000000000000000000000  0000000000000  0
0           0        0              0        0     0        0
0000000000  0000000000  0000000000  0  0000  0  0000  0000000
0           0           0        0     0     0        0     0
0  0000000000  0000000000  0000000000000  0000000000000  0  0
0           0  0           0           0     0           0  0
0000000000  0  0  0000000000  0000  0000000  0  0000000000  0
0     0     0     0        0     0  0     0  0  0     0     0
0  0  0  0000000000  0000  0000  0  0  0  0000  0  0000  0000
0  0  0              0  0  0     0     0     0        0     0
0  0  0000000000000000  0  0  0  0000000000  0000  0  0000  0
0  0     0              0     0  0        0     0  0     0  0
0  0000  0  0000000  0000000000000  0000000000  0  0000000  0
0  0              0  0     0     0                 0        0
0  0000000  0  0000  0  0000  0  0000  0000  0  0000  0000000
0        0  0     0  0        0  0        0  0     0  0     0
0  0000  0  0000  0  0  0000000  0000000000  0000000  0000  0
0  0  0  0  0     0  0     0     0           0     0        0
0  0  0  0000  0000  0000  0  0000  0000000000  0  0000000000
0     0  0     0     0  0  0     0              0     0     0
0000000  0  0000000  0  0  0000  0  0000000000000000  0000  0
0        0     0     0  0  0  0     0                 0     0
0  0000000000  0  0000  0  0  0000  0  0000000000000000  0000
0  0     0     0        0  0        0  0     0        0  0  0
0  0  0  0  0000000000000  0000000  0  0  0  0000000  0  0  0
0     0  0                 0        0     0                 B
0000000000000000000000000000000000000000000000000000000000000

"""


""" on  verifie si les elements de la matrice sont deja visite ou pas. La verification se realise en refaisant le chemin, et en retournant si elle trouve une voie bloquee. """

def solve(labyrinth, x, y, m, n):
    path = False
    if 0 <= x < m and 0 <= y < n:
        if labyrinth[y][x] in (empty, start):
            if labyrinth[y][x] == empty:
                labyrinth[y][x] = visited
            if (solve(labyrinth, x+1, y, m, n) or solve(labyrinth, x-1, y, m, n) or solve(labyrinth, x, y+1, m, n) or solve(labyrinth, x, y-1, m, n)):
                if labyrinth[y][x] == visited:
                    labyrinth[y][x] = good
                path = True
        elif labyrinth[y][x] == end:
            path = True
    return path

""" labyrinth- prend une liste du caracteres pour le labyrinthe
    x- c'est la position de x
    y- c'est la position de y
    m, n- c'est la dimension de la matrice (matrice avec m lignes, n colonnes) """


def main():
    labyrinth = [list(x) for x in LABYRINTH.splitlines() if x]
    solve(labyrinth, 0, 1, len(labyrinth[0]), len(labyrinth))
    for line in labyrinth:
        print ("".join(line))

if __name__ == "__main__":
    main()

"""ici c'est l'initialisation du contructeur main pour trouver la solution du labyrinthe""" 
