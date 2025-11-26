import pygame
from pygame.locals import *
from pygame import mixer
from classes import Tap, Hold
import math

# Initialize pygame
mixer.init(44100, -16, 2, 4096)
pygame.init()


SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rhota - Rhythm Game")
mixer.music.set_volume(0.7)

songs = {}
bg = pygame.image.load("Background1.png")
tap_notes_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
clicked_notes = {"s":False, "d":False, "j":False, "k":False}
hold_clicked_notes = {"s":False, "d":False, "j":False, "k":False}

start = True
status = 'home'
frame = 0
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get(): 
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()
    
    screen.blit(bg, (0, 0))
    frame += 1
    
    pygame.display.update()
    clock.tick(60) 

pygame.quit() 
