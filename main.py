import pygame
import sys
from settings import *
from player import Player
from car import Car


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.bg = pygame.image.load("./graphics/main/map.png").convert()
        self.fg = pygame.image.load("./graphics/main/overlay.png").convert_alpha()

    def customize_draw(self):

        self.offset.x = player.rect.centerx - window_width / 2
        self.offset.y = player.rect.centery - window_height / 2

        display_surface.blit(self.bg, -self.offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            display_surface.blit(sprite.image, offset_pos)

        display_surface.blit(self.fg, -self.offset)

# basic setup
pygame.init()
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# groups
all_sprites = AllSprites()

# sprites
player = Player((600, 400), all_sprites)
car = Car((100, 200), all_sprites)

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
    #all_sprites.draw(display_surface)
    all_sprites.customize_draw()

    # update
    all_sprites.update(dt)

    # update the display surface
    pygame.display.update()
