# Import des modules nécessaires
from random import randint
from constants import *

game = [ [ ITEM_SEALED ] * TABLE_SIZE for _ in range(TABLE_SIZE) ]

# Positions de mines
mines = [] # (x,y)
# Positions des nombres
numbers = {} # {(x,y): value}

# Gets X,Y coordinates from an integer using the table size
def get_pos_from_int(value):
    """
    Converti un nombre entier en une coordonnées dans un espace en 2D à l'aide de la taille du tableau
    """
    x = value // TABLE_SIZE
    y = value % TABLE_SIZE
    return (x,y)

# Randomly places each mine in the grid
def init_mines():
    """
    Place de façon (pseudo-)aléatoire les mines dans le tableau "table"
    """
    positions = []
    for _ in range(MINE_COUNT):
        pos = randint(0, TABLE_SIZE * TABLE_SIZE - 1)
        while pos in positions:
            pos = randint(0, TABLE_SIZE * TABLE_SIZE - 1)

        positions.append(pos)
        mines.append(
            get_pos_from_int(pos)
        )

# Places the numbers around the mines 
def init_numbers():
    """
    Place dans le tableau "num_table" les coordonnées de chacun des nombres correspondant au nombre de mines autour
    """
    for mine in mines:
        for xAxis in AXIS:
            for yAxis in AXIS:
                num_pos = (mine[0] + xAxis, mine[1] + yAxis)
                if num_pos in mine:
                    return

                if num_pos not in numbers:
                    numbers[num_pos] = 1
                else:
                    numbers[num_pos] += 1

# Checks if the given coordinates are within the bounds of the grid
def is_within_bounds(x, y):
    """
    Renvois si la coordonnée donnée est dans ou hors du tableau
    """
    return x >= 0 and x < TABLE_SIZE and y >= 0 and y < TABLE_SIZE

# Reveals the cells recursively
def reveal_seals_recursive(x, y):
    """
    Révelle à l'utilisateur les cases (récursivement)
    """
    # Oui j'utilise des returns, j'ai pas envie que mon code soit illisble
    if (x, y) in mines:
        return

    if game[x][y] != ITEM_SEALED:
        return

    if (x,y) in numbers:
        game[x][y] = numbers[(x,y)]
        return
    
    game[x][y] = ITEM_DISCOVERED

    for xAxis in AXIS:
        for yAxis in AXIS:
            next_pos = (x + xAxis, y + yAxis)
            if is_within_bounds(*next_pos) and next_pos:
                reveal_seals_recursive(*next_pos)

# Checks if the game continues or not and notifies if the user lost or won if the game ended
def check_game_status(x, y):
    """
    Renvois si le jeu doit continuer ou pas. S'il ne continue pas affiche si le joueur a gagné ou non
    """
    should_stop = False
    has_won = False
    if (x, y) in mines:
        should_stop = True
    else:
        reveal_seals_recursive(x, y)

    seals_count = 0
    for x in range(TABLE_SIZE):
        for y in range(TABLE_SIZE):
            if game[x][y] == ITEM_SEALED and (x, y) not in mines:
                seals_count += 1

    if seals_count == 0:
        has_won = True
        should_stop = True

    return should_stop, has_won

# Initialisation des mines et nombres dans le tableau
init_mines()
init_numbers()