# Import du module nécessaire
import glfw

# Dictionnaire pour stocker l'état des touches
keys = {}

def is_key_pressed(window, key):
    """
    Renvois si une touche a été appuié puis relaché
    """
    global keys

    is_key_released = False
    
    if keys.get(key) and glfw.get_key(window, key) == glfw.RELEASE:
        is_key_released = True
    
    keys[key] = glfw.get_key(window, key) == glfw.PRESS

    return is_key_released

# Stocke l'état du clique gauche et clique droit
left_click_down = False
right_click_down = False

def is_left_click(window):
    """
    Renvois si un bouton de la souris a été appuié puis relaché
    """
    global left_click_down

    is_left_click_release = False
    
    if left_click_down and glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_1) == glfw.RELEASE:
        is_left_click_release = True
    
    left_click_down = glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_1) == glfw.PRESS

    return is_left_click_release