# Necessary Imports
from microbit import *
from random import *

# Initializes variables
elapsedTick = 0
elapsedTime = 0

spawnRateMultiplier = 5
baseSpawnRate = 125

score = 0
playerX = 2
playerY = 4

enemies = []

# Calculates how fast enemies are going to spawn
def calculateSpawnRate():
    difficulty = score * spawnRateMultiplier
    if difficulty >= baseSpawnRate:
        return 1
    return baseSpawnRate - difficulty

# Adds an enemy
def addEnemy():
    x = randint(0, 4)
    enemies.append((x, 0))

# Checks whether the player collides with an enemy
def isColliding():
    for enemy in enemies:
        if enemy[0] == playerX and enemy[1] == playerY:
            return True
    return False

# Moves the player to the left or right based on the x parameter
def movePlayer(x):
    global playerX
    if (playerX + x) > 4 or (playerX + x) < 0:
        return
    playerX += x

# Game start countdown
for i in range(5, 0, -1):
    display.show(str(i))
    sleep(750)

# Game loop
while True:
    # Clears the screen
    display.clear()
    
    # Checks whether the game is running slowly
    if elapsedTime != 0 and elapsedTime + 100 < running_time():
        print("==========TICK SLOW==========")

    # Moves the player to the left or right based on whether the buttons are pressed or not
    if button_a.was_pressed():
        movePlayer(-1)
    if button_b.was_pressed():
        movePlayer(1)

    # Adds an enemy based on the spawn rate
    if elapsedTick % calculateSpawnRate() == 0:
        addEnemy()

    # Render the enemies
    for enemy in enemies:
        display.set_pixel(enemy[0], enemy[1], 3)
    
    # Check if the player has reached the top of the screen
    if playerY < 0:
        display.clear()
        enemies.clear()
        score  += 1
        playerY = 4

    # Renders the player
    display.set_pixel(playerX, playerY, 9)
    
    # Moves the player up
    if elapsedTick != 0 and elapsedTick % 75 == 0:
        playerY -= 1

    # Checks whether the player collides with an enemy
    if isColliding():
        break
    
    # Update tick count and elapsed time
    elapsedTick += 1
    elapsedTime = running_time()
    sleep(10)

# Shows game over message
display.scroll(str(score))
display.scroll("GAME OVER")
