import pygame
import sys
from settings import *
from player import Player

# basic setup
pygame.init()
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# groups
all_sprites = pygame.sprite.Group()

# sprites
player = Player((600, 400), all_sprites)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick() / 1000

    # draw background
    display_surface.fill('black')

    # draw
    all_sprites.draw(display_surface)

    # update
    all_sprites.update(dt)

    # update the display surface
    pygame.display.update()
