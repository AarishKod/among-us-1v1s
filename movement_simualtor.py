import pygame
import os
import time
import sys

pygame.font.init()

width_x, height_x = 1440, 900
char_x, char_y = 50, 50
nush_x, nush_y = 200, 40
other_char_x, other_char_y = 800, 50

WIN = pygame.display.set_mode((width_x, height_x))
pygame.display.set_caption('Movement Simulator')
font = pygame.font.SysFont('comicSans', 50)


# assets import
backGround = pygame.transform.scale(pygame.image.load(os.path.join('assets/images', 'poop.png')), (width_x, height_x))
character = pygame.image.load(os.path.join('assets/images', 'meep2.png'))
leg_piece = pygame.image.load(os.path.join('assets/images', 'oof.jpg'))
other_character = pygame.image.load(os.path.join('assets/images', 'loop.png'))

def renderMeNow():
    pressSpace = font.render(f'Press the space button', 1, (255, 255, 255))
    name = font.render(f"I'm Sus", 1, (255, 0, 0))
    WIN.blit(backGround, (0, 0))
    WIN.blit(pressSpace, (50, 10))
    WIN.blit(other_character, (other_char_x, other_char_y))
    WIN.blit(name, (nush_x, nush_y))
    WIN.blit(character, (char_x, char_y))
    # WIN.blit(leg_piece, (char_x, char_y))
    pygame.display.update()



while True:
    renderMeNow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_SPACE]:
        char_y -= 5
        nush_y -= 5
    if pygame.key.get_pressed()[pygame.K_UP]:
        char_y -= 1
        nush_y -= 1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        char_y += 1
        nush_y += 1
    if pygame.key.get_pressed()[pygame.K_DOWN] and pygame.key.get_pressed()[pygame.K_SPACE]:
        char_y += 5
        nush_y += 5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        char_x -= 1
        nush_x -= 1
    if pygame.key.get_pressed()[pygame.K_LEFT] and pygame.key.get_pressed()[pygame.K_SPACE]:
        char_x -= 5
        nush_x -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        char_x += 1
        nush_x += 1
    if pygame.key.get_pressed()[pygame.K_RIGHT] and pygame.key.get_pressed()[pygame.K_SPACE]:
        char_x += 5
        nush_x += 5
    if pygame.key.get_pressed()[pygame.K_u]:
        WIN.blit(leg_piece, (char_x, char_y))
        print('NUSH')
    
