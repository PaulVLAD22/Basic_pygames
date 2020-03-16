import pygame
import random
import math
from timeit import default_timer as timer
# initializeaza pygame
pygame.init()

# ecranu
screen = pygame.display.set_mode((800,600))

# background
background = pygame.image.load('background_flappy.png')

# titlu si iconita
pygame.display.set_caption("Birdy doing the flapp")
icon = pygame.image.load('my_icon.png')
pygame.display.set_icon(icon)

# font
font_score = pygame.font.Font(None, 32)
# audio
music = pygame.mixer_music.load('music.mp3')
pygame.mixer_music.play(-1)

#player
playerImg=pygame.image.load("my_icon.png")
playerX = 370
playerY = 200
playerY_change = 3

#score
def score_function(score):
    screen.blit(font_score.render("Score:", True, (255, 255, 255)), (30, 20))
    screen.blit(font_score.render(str(score), True, (255, 255, 255)), (100, 20))

def player(x, y):
    screen.blit(playerImg, (x, y))

def isCollision(playerX, playerY, X, Y): #fie lovitura de pillar, fie de ecran
    distance = math.sqrt(math.pow(playerX - X, 2) + math.pow(playerY - Y, 2))
    return distance<15

#pillars
pillarImg=pygame.image.load("pillar.png")
pillars_X=[]
pillars_Y=[]
pillars_X_change=-2
def pillar_spawnning(score):
    i=1
    spawn_times = []
    for j in range (500):
        if (j%3==0):
            spawn_times.append(j)
    if (score in spawn_times): # se executa de 4 ori
        for i in range(i+spawn_times.index(score)-1):
            pillar_x=random.randint(370+200,720) # 370 e playerX
            pillar_y=random.randint(100,540)
            pillars_X.append(pillar_x)
            pillars_Y.append(pillar_y)

def print_on_screen_pillars(pillars_X,pillars_Y):
    for i in range (len(pillars_X)):
        screen.blit(pillarImg,(pillars_X[i],pillars_Y[i]))

def pillar_out_of_screen(pillars_X,pillars_Y):
    for i in range (len(pillars_X)-1):
        for j in range (len(pillars_X)):
            if (pillars_X[i]==pillars_X[j]):
                pillars_X[i]+=1
            if (pillars_Y[i]==pillars_Y[j]):
                pillars_Y[i]+=1
    for i in range (len(pillars_X)):
        if (isCollision(pillars_X[i],pillars_Y[i],0,pillars_Y[i])):
            pillars_X.pop(i)
            pillars_Y.pop(i)

#game loop
running=True
while (running):
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    score_function(round(timer(),1))

    pillar_spawnning(round(timer(),1))

    print_on_screen_pillars(pillars_X,pillars_Y)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False
            if event.key == pygame.K_SPACE:
                playerY_change*=-1


     # COLLISIONS

    #Out of screen
    if (isCollision(playerX,playerY,playerX,0) or isCollision(playerX,playerY,playerX,800)):
        screen.blit(font_score.render("GAME OVER", True, (0, 0, 0)), (350, 300))
        pygame.time.set_timer(pygame.QUIT, 1000)
    #COLLISSIONS WITH PILLARS
    for i in range (len(pillars_X)):
        if (isCollision(playerX,playerY,pillars_X[i],pillars_Y[i])):
            print("AAA")
            screen.blit(font_score.render("GAME OVER", True, (0, 0, 0)), (350, 300))
            pygame.time.set_timer(pygame.QUIT, 1000)
    #movement
    playerY+=playerY_change

    for i in range(len(pillars_X)):
        pillars_X[i]+=pillars_X_change

    player(playerX, playerY)
    pygame.display.update()

# NU MERGE SA SE OPREASCA SUNT HANDICAPAT








