# Imports des modules necessaires
from PIL import Image, ImageTk

from constants import *

# { "Name": Data }
TEXTURES = {
    "cell": 0,
    "mine": 0,
    "flag": 0,
    "num_1": 0,
    "num_2": 0,
    "num_3": 0,
    "num_4": 0,
    "num_5": 0,
    "num_6": 0,
    "num_7": 0,
    "num_8": 0 
}

# Initialisation de toutes les textures
def init_textures():
    """
    Lecture de toutes les textures sur le disque et création d'une nouvelle instance de "PhotoImage"
    """
    for key in TEXTURES:
        img = Image.open(f"{WORKING_DIRECTORY}\\textures\\{key}.png")
        img = img.resize(
            (TABLE_ITEM_SIZE - 2, TABLE_ITEM_SIZE - 2),
            Image.NEAREST
        )
        TEXTURES[key] = ImageTk.PhotoImage(img)

# Dessine le jeu
def draw_game(canvas, table, size, width, height):
    """
    Dessine l'intégralité du jeu (Grille, cases, numéros)
    """
    squareWidth = width / size
    squareHeight = height / size

    x = 0
    y = 0

    canvas.create_rectangle((0,0),(VIEWPORT_WIDTH, VIEWPORT_HEIGHT), fill="#7f7f7f")

    # Dessine la grille de jeu
    for _ in range(0, size):
        canvas.create_line(x, 0, x, width)
        x += squareWidth

        canvas.create_line(0, y, height, y)
        y += squareHeight

    # Dessine les cases
    for tx in range(len(table)):
        for ty in range(len(table[tx])):
            if table[tx][ty] == ITEM_SEALED:
                draw_texture(canvas,
                             tx * TABLE_ITEM_SIZE + 1,
                             ty * TABLE_ITEM_SIZE + 1, 
                             TABLE_ITEM_SIZE - 2, "cell")
            elif type(table[tx][ty]) == int:
                draw_texture(canvas,
                             tx * TABLE_ITEM_SIZE + 1,
                             ty * TABLE_ITEM_SIZE + 1,
                             TABLE_ITEM_SIZE - 2, f"num_{table[tx][ty]}")
            
    
# Dessine une texture
def draw_texture(canvas, x, y, size, texture_name):
    """
    Dessine une texture avec sa position, taille
    """

    canvas.create_image(
        (x + size / 2, y + size / 2),
        image=TEXTURES[texture_name]
    )

# Montre toutes les mines
def reveal_all_bombs(canvas, positions, is_flag):
    """
    Affiche toutes les mines, elles sont affichées de façon différentes en fonction de "is_flag"
    """
    for pos in positions:
        x = pos[0] * TABLE_ITEM_SIZE + 1
        y =  pos[1] * TABLE_ITEM_SIZE + 1
        size = TABLE_ITEM_SIZE - 2

        texture = is_flag and "flag" or "mine"

        draw_texture(canvas, x, y, size, texture)