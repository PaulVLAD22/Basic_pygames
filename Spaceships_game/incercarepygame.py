import pygame
import random
import math
import decimal

# initializeaza pygame
pygame.init()

# ecranu
screen = pygame.display.set_mode((800,600))

# background
background = pygame.image.load('background.jpg')

# titlu si iconita
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('my_icon.png')
pygame.display.set_icon(icon)

# font
font = pygame.font.Font(None, 64)
font_precision = pygame.font.Font(None, 32)

# audio
bulletsound = pygame.mixer.Sound('bulletshot.wav')
explosion = pygame.mixer.Sound('explosion.wav')

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 450
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(30)

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# score
score = 0
lista_scoruri = []
lista_scoruri.append(pygame.image.load('zero.png'))
lista_scoruri.append(pygame.image.load('one.png'))
lista_scoruri.append(pygame.image.load('two.png'))
lista_scoruri.append(pygame.image.load('three.png'))
lista_scoruri.append(pygame.image.load('four.png'))
lista_scoruri.append(pygame.image.load('five.png'))
lista_scoruri.append(pygame.image.load('six.png'))
lista_scoruri.append(pygame.image.load('seven.png'))
lista_scoruri.append(pygame.image.load('eight.png'))
lista_scoruri.append(pygame.image.load('nine.png'))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance


# Game loop
running = True
precision = 0
bullets_shot = 0
while running:

    # RGB- Red,Green,Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    screen.blit(font_precision.render("Precision:", True, (255, 255, 255)), (500, 20))
    if (score > 0):
        screen.blit(font_precision.render(str(precision), True, (255, 255, 255)), (650, 20))
        screen.blit(font_precision.render("%", True, (255, 255, 255)), (730, 20))
        precision = score / bullets_shot * 100
        precision = round(precision, 2)
    if (score > 0):
        screen.blit(font_precision.render("Score:", True, (255, 255, 255)), (30, 20))
        screen.blit(font_precision.render(str(score), True, (255, 255, 255)), (100, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether is right or left
        if (event.type == pygame.KEYDOWN):
            print("A keystroke is pressed")
            if (event.key == pygame.K_LEFT):
                print("Left arrow is pressed")
                playerX_change = -4
            if (event.key == pygame.K_RIGHT):
                print("Right arrow is pressed")
                playerX_change = 4
            if (event.key == pygame.K_SPACE):
                if (bullet_state is "ready"):
                    bulletX = playerX
                    bulletsound.play()
                    fire_bullet(bulletX, bulletY)
                    bullets_shot += 1
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                print("Keystroke has been released")
                playerX_change = 0
    # 5 =5+ -0.1 -> 5=5-0.1
    # 5=5+0.1->5.1
    # checking for boundries of spaceship so it doesn't go out of bounce
    playerX += playerX_change
    if (playerX <= 0):
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Enemey Movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if (enemyX[i] <= 0):
            enemyX_change[i] = enemyX_change[i] * -1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = enemyX_change[i] * -1
            enemyY[i] += enemyY_change[i]
        # COLISION , with the bullet and with the player
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if (collision < 27):
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            screen.blit(pygame.image.load('explosion.png'), (enemyX[i], enemyY[i]))
            explosion.play()
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
        if (collision < 56):
            screen.blit(font.render("GAME OVER", True, (0, 0, 0)), (400, 300))
            pygame.time.set_timer(pygame.QUIT, 1000)
        enemy(enemyX[i], enemyY[i], i)
    # Bullet Movement
    if (bulletY <= 0):
        bulletY = 480
        bullet_state = "ready"
    if (bullet_state is "fire"):
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    player(playerX, playerY)
    pygame.display.update()
