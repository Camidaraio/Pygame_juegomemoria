import pygame, random
import re

from pygame.sprite import _Group

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mose((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imagen.png").convert()
        
