import pygame
import random
import math
import decimal

#initializeaza pygame
pygame.init()

#ecran
screen = pygame.display.set_mode((800,600))

#background
background=pygame.image.load('background2.jpg')

# titlu si iconita
pygame.display.set_caption("VladvsBakugo")
icon = pygame.image.load('enemy.png')
pygame.display.set_icon(icon)

#font
font=pygame.font.Font(None,32) # pentru a scrie "Muie Bakugo" cand nimeresti

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 450
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(50,150))
    enemyY.append(random.randint(100,300))
    enemyX_change.append(2)
    enemyY_change.append(3)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

#queen
queenImg=pygame.image.load('c59eba9b-45d1-42ed-b869-a6da726de737.png')
queenX=700
queenY=300


def queen(x,y):
    screen.blit(queenImg,(x,y))




#bullet
bulletImg = pygame.image.load('bulletu.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

#lovitura
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance

running=True

while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
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
                    fire_bullet(bulletX, bulletY)
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                print("Keystroke has been released")
                playerX_change = 0
    playerX += playerX_change
    if (playerX <= 0):
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if(collision<40):
            bulletY=480
            screen.blit(font.render("MUIE", True, (255, 255, 255)), (500, 20))
            bullet_state="ready"
            screen.blit(pygame.image.load('explosion.png'), (enemyX[i], enemyY[i]))
            enemyX[i] = random.randint(50,150)
            enemyY[i] = random.randint(100,400)
        collision=isCollision(enemyX[i],enemyY[i],queenX,queenY)
        if (enemyX[i]==800):
            enemyX[i] = random.randint(50, 150)
            enemyY[i] = random.randint(100, 400)
        if(collision<56):
            screen.blit(font.render("TI-A FURAT-O FRATE", True, (0, 0, 0)), (400, 300))
            pygame.time.set_timer(pygame.QUIT, 1000)
        enemy(enemyX[i],enemyY[i],i)
    if (bulletY <= 0):
        bulletY = 480
        bullet_state = "ready"
    if (bullet_state is "fire"):
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    queen(queenX,queenY)
    player(playerX,playerY)
    pygame.display.update()