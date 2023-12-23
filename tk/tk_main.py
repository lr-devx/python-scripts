#######################################################
#######################################################
############## Tk Minesweeper (Démineur) ##############
#######################################################
#######################################################

# Import des modules nécessaires
from math import floor
from tkinter import *
from constants import *

import graphics
import logic

# Position du curseur
cursorPosX = 0
cursorPosY = 0

# Définie si le jeu est terminé
is_game_finished = False
# Définie si le joueur a gagné
has_player_won = False

# Définie la case séléctionée
current_row = 0
current_column = 0

# Canvas
canvas = None

def on_mouse_motion(e):
    """
    Quand le curseur bouge; change la case courrante par rapport à la position du curseur
    """
    global cursorPosX, cursorPosY, current_row, current_column
    
    cursorPosX = e.x
    cursorPosY = e.y

    if cursorPosX > 0 and cursorPosX < VIEWPORT_WIDTH and cursorPosY > 0 and cursorPosY < VIEWPORT_HEIGHT:
        current_row = floor(cursorPosX / TABLE_ITEM_SIZE)
        current_column = floor(cursorPosY / TABLE_ITEM_SIZE)

def on_left_click(e):
    """
    Logique principale du jeu
    """
    global is_game_finished, has_player_won

    if is_game_finished:
        return

    should_stop, has_won = logic.check_game_status(current_row, current_column)
    graphics.draw_game(canvas, logic.game, TABLE_SIZE, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)

    if should_stop:
        is_game_finished = True
        has_player_won = has_won

        graphics.reveal_all_bombs(canvas, logic.mines, has_player_won)

def create_window():
    global canvas

    """
    Créer une fenêtre et créer le canvas
    Lance la boucle principale
    """

    # Créer la fenêtre
    window = Tk()
    window.title("Minesweeper (Tk)")

    # Ajoute les 'callbacks' aux évenements
    window.bind("<Motion>", on_mouse_motion)
    window.bind("<ButtonRelease-1>", on_left_click)

    # Créer un canvas
    canvas = Canvas(window, width=VIEWPORT_WIDTH, height=VIEWPORT_WIDTH, bd=0, highlightthickness=0, bg="#7f7f7f")
    canvas.pack(anchor=CENTER, expand=True)

    # Initialise les textures
    graphics.init_textures()

    # Dessine le jeu
    graphics.draw_game(canvas, logic.game, TABLE_SIZE, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)

    # Boucle de la fenêtre
    window.mainloop()

create_window()