# La grille de jeu
# J'utilise pas un tableau eu deux dimensions
# pour pouvoir par la suite désigner une case par un seul nombre au lieu d'une coordonnée.
game_grid = [
    "_","_","_",
    "_","_","_",
    "_","_","_" 
]

# Au lieu de faire des formules dans tout les sens, je fais juste une liste de toute les possibilités de jeu
game_issues = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

# La fonction pour afficher la grille
def show_grid(grid):
    """
    Prend une grille comme argument
    Affiche la grille en admettant que la grille donnée à 9 cases 
    """
    print()
    for i in range(len(grid)):
        print(grid[i], end=" ")
        # Toute les 3 cases, on affiche une nouvelle ligne
        if (i+1) % 3 == 0: print()
    print()

# La fonction pour obtenir la position du joueur 
def get_input(grid, is_player_o):
    """
    Prend et verifie l'entrée donnée par le joueur
    """
    player = "X"
    if is_player_o:
        player = "O"

    print("Tour de Joueur", player)

    pos = 0
    while pos == 0 or pos > 9:
        in_pos = input("Case: ")
        # Verifie si l'entrée est un seul caractère et qu'il est compris entre 1 et 9
        if len(in_pos) == 1 and ord(in_pos) > 48 and ord(in_pos) < 58:
            pos = int(in_pos)

    # Verifie si la case est déjà utiliser
    if grid[pos - 1] != "_":
        # On appelle la fonction recursivement si c'est le cas
        return get_input(grid, is_player_o)

    # On renvois la position du joueur et le joueur en lui-même
    return pos, player

# La fonction qui place le joueur et vérifie si le joueur a gagné
def check_input(grid, pos, player):
    """
    Place et vérifie si le joueur a gagné
    """
    grid[pos - 1] = player
    
    has_match = 0
    has_won = False

    for issue in game_issues:
        for issue_pos in issue:
            if (grid[issue_pos-1] == player):
                has_match += 1

        if has_match == 3:
            has_won = True
            break

        has_match = 0

    return has_won

# La fonction qui affiche le message de fin
def show_win_message(grid, player):
    """
    Affiche le joueur qui a gagné
    """
    show_grid(grid)
    print("Joueur", player, "a gagné!!!")

has_game_finished = False

# Boucle principale
while not has_game_finished:
    show_grid(game_grid)

    input_x = get_input(game_grid, False)

    if check_input(game_grid, input_x[0], input_x[1]):
        show_win_message(game_grid, input_x[1])
        has_game_finished = True

    # On vérifie que le joueur X n'a pas encore gagné
    if not has_game_finished:
        input_o = get_input(game_grid, True)

        if check_input(game_grid, input_o[0], input_o[1]):
            show_win_message(game_grid, input_o[1])
            has_game_finished = True