# Import de module os
import os

# Définie le dossier du fichier "glfw_main.py"
WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Définie la taille de la partie cliente de la fenêtre
VIEWPORT_WIDTH = 640
VIEWPORT_HEIGHT = 640

# Définie la taille du tableau
TABLE_SIZE = 20
# Définie le nombre de mines
MINE_COUNT = 50

# Définie la taille d'une case
TABLE_ITEM_SIZE = VIEWPORT_WIDTH / TABLE_SIZE

# Définie comment les bombes sont affichés
ITEM_BOMB = "*"
# Définie comment les marqueurs sont affichés
ITEM_MARKER = "@"
# Définie comment les cases fermées sont affichés
ITEM_SEALED = "#"
# Définie comment les cases ouvertes sont affichés
ITEM_DISCOVERED = "_"

# Axes (horizontal, vertical, et diagonal)
AXIS = [-1, 0, 1]