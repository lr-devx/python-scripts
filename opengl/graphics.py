# Imports des modules necessaires
from PIL import Image
from OpenGL.GL import *

from constants import *

# { "Name": ID }
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
    Lecture de toutes les textures sur le disque et créer une nouvelle texture OpenGL pour chaque avec un ID qui correspond
    Cette ID sera utiliser pour référencer la texture par la suite
    """
    for key in TEXTURES:
        img = Image.open(f"{WORKING_DIRECTORY}\\textures\\{key}.png")
        data = img.tobytes()
        width, height = img.size

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        TEXTURES[key] = texture_id

# Dessine le jeu
def draw_game(table, size, width, height):
    """
    Dessine l'intégralité du jeu (Grille, cases, numéros)
    """
    squareWidth = width / size
    squareHeight = height / size

    x = 0
    y = 0

    # Dessine la grille de jeu
    glBegin(GL_LINES)
    glColor(0.1, 0.1, 0.1)

    for _ in range(0, size):
        glVertex2d(x, 0)
        glVertex2d(x, width)
        x += squareWidth

        glVertex2d(0, y)
        glVertex2d(height, y)
        y += squareHeight

    glColor(1, 1, 1)
    glEnd()

    # Dessine les cases
    for tx in range(len(table)):
        for ty in range(len(table[tx])):
            if table[tx][ty] == ITEM_SEALED:
                draw_texture(tx * TABLE_ITEM_SIZE + 1,
                             ty * TABLE_ITEM_SIZE + 1,
                             TABLE_ITEM_SIZE - 2, "cell")
            elif type(table[tx][ty]) == int:
                draw_texture(tx * TABLE_ITEM_SIZE + 1,
                             ty * TABLE_ITEM_SIZE + 1,
                             TABLE_ITEM_SIZE - 2, f"num_{table[tx][ty]}")
            
    

# Dessine un carré
def draw_square(x, y, size, color = [1,1,1]):
    """
    Dessine un carré avec sa position, sa taille et sa couleur
    """
    glBegin(GL_QUADS)
    glColor(*color)
    glVertex2d(x, y)
    glVertex2d(x + size, y)
    glVertex2d(x + size, y + size)
    glVertex2d(x, y + size)
    glEnd()

# Dessine une texture
def draw_texture(x, y, size, texture_name):
    """
    Dessine une texture avec sa position, taille
    """
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, TEXTURES[texture_name])

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x, y)
    glTexCoord2f(1, 0); glVertex2f(x + size, y)
    glTexCoord2f(1, 1); glVertex2f(x + size, y + size)
    glTexCoord2f(0, 1); glVertex2f(x, y + size)
    glEnd()

    glDisable(GL_TEXTURE_2D)

# Montre toutes les mines
def reveal_all_bombs(positions, is_flag):
    """
    Affiche toutes les mines, elles sont affichées de façon différentes en fonction de "is_flag"
    """
    for pos in positions:
        x = pos[0] * TABLE_ITEM_SIZE + 1
        y =  pos[1] * TABLE_ITEM_SIZE + 1
        size = TABLE_ITEM_SIZE - 2

        color = is_flag and [0,1,0] or [1,0,0]
        texture = is_flag and "flag" or "mine"

        draw_square(x, y, size, color)
        draw_texture(x, y, size, texture)