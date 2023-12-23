######################################################
######################################################
########### Open GL Minesweeper (Démineur) ###########
######################################################
######################################################

# Import des modules nécessaires
import glfw

from math import floor
from OpenGL.GL import *
from OpenGL.GLU import *

from constants import *

import graphics
import logic
import inputs

# Position du curseur
cursorPosX = 0
cursorPosY = 0

# Définie si le jeu est terminé
is_game_finished = False
# Définie si le joueur a gagné
has_player_won = False

# Fonction utilisé lorsque le jeu est en cours
def on_game_running(window):
    """
    Logique principale pour le jeu
    """
    global cursorPosX, cursorPosY, is_game_finished, has_player_won

    cursorPosX, cursorPosY = glfw.get_cursor_pos(window)
    
    # Dessine le jeu
    graphics.draw_game(logic.game, TABLE_SIZE, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)

    # On récupére la position du curseur pour savoir quelle case est concernée par un clique gauche de l'utilisateur 
    if cursorPosX > 0 and cursorPosX < VIEWPORT_WIDTH and cursorPosY > 0 and cursorPosY < VIEWPORT_HEIGHT:
        row = floor(cursorPosX / TABLE_ITEM_SIZE)
        column = floor(cursorPosY / TABLE_ITEM_SIZE)

        if inputs.is_left_click(window):
            should_stop, has_won = logic.check_game_status(row, column)
            if should_stop:
                is_game_finished = True
                has_player_won = has_won


# Foncition utilisé lorsque le jeu est fini
def on_game_ended():
    """
    Dessine le jeu avec les bombes quand la partie est terminée
    """
    graphics.draw_game(logic.game, TABLE_SIZE, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)
    graphics.reveal_all_bombs(logic.mines, has_player_won)

def create_window():
    """
    Créer une fenêtre avec les APIs corresponds à la platforme et créer un context OpenGL
    Lance la boucle principale
    """
    if not glfw.init():
        return

    # Indique que la fenêtre ne peut pas être redimensioner
    glfw.window_hint(glfw.RESIZABLE, GL_FALSE)

    # Créer la fenêtre
    window = glfw.create_window(VIEWPORT_WIDTH, VIEWPORT_HEIGHT, "Minesweeper (OpenGL)", None, None)
    if not window:
        glfw.terminate()
        return

    # Créer le context OpenGl
    glfw.make_context_current(window)

    # Change la taille minimale et maximale de la fenêtre
    glfw.set_window_size_limits(window, VIEWPORT_WIDTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)

    # Créer une matrice de projection orthographique
    gluOrtho2D(0, VIEWPORT_WIDTH, VIEWPORT_HEIGHT, 0)

    # Initialise les textures
    graphics.init_textures()

    # Change la couleur de rafraichissement de la fenêtre 
    glClearColor(0.5, 0.5, 0.5, 1)

    # Boucle principale
    while not glfw.window_should_close(window):
        # Rafraichit la fenêtre
        glClear(GL_COLOR_BUFFER_BIT)

        # Logique principale
        if not is_game_finished:
            on_game_running(window)
        else:
            on_game_ended()

        # Inversion le buffer derrière avec le buffer avant
        glfw.swap_buffers(window)

        # Execution de tout les évenements de la fenêtre
        glfw.poll_events()

    # Extermination (oui)
    glfw.terminate()

create_window()