import os 
import random 
import math 
import pygame 
from os import listdir #return list file in folder cụ thể
from os.path import isfile, join 

pygame.init()

pygame.display.set_caption('Platformer')

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite): 
    COLOR = (255, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None

    def move(self, dx, dy): 
        self.rect.x += dx 
        self.rect.y += dy

def get_background(name):
    image = pygame.image.load(join("assets", "background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1): 
        for j in range(HEIGHT // height + 1): 
            pos = [i * width, j * height]
            tiles. append(pos)
    return tiles, image

def draw(window, background, bg_image): 
    for tile in background:
        window.blit(bg_image, tile)
    
    pygame.display.update()

def main(window): 
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)
    pygame.quit()
    quit()

if __name__ == "__main__": #Code will run as main program (not a module which was imported from other program)
    main(window)