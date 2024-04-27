import pygame
import sys
import random
from math import *
pygame.init()
 
width = 200
height = 1000

# Загрузка фотографии место (где будет происходить)

background_image = pygame.image.load("photo\\mesto.jpg")
background_image = pygame.transform.scale(background_image, (width, height))
 
# Загрузка призрака изображений 

ghost_image = pygame.image.load("photo\\Prizrak.jpg")


display = pygame.display.set_mode((width, height))
pygame.display.set_caption("CopyAssignment - ghost Shooter Game")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
 
margin = 100
lowerBound = 100
 
score = 0
 
white = (230, 230, 230)
lightBlue = (4, 27, 96)
red = (231, 76, 60)
lightGreen = (25, 111, 61)
darkGray = (40, 55, 71)
darkBlue = (64, 178, 239)
green = (35, 155, 86)
yellow = (244, 208, 63)
blue = (46, 134, 193)
purple = (155, 89, 182)
orange = (243, 156, 18)
 
font = pygame.font.SysFont("Arial", 25)

# Загрузка музыки 
pygame.mixer.music.load("Effects\\effekt-quotprivideniyaquot-28433.mp3")
pygame.mixer.music.play(-1)
 
# Страшные звуки в игре (место где будет это происходить)
burst_sound = pygame.mixer.Sound("Effects\\prizrak-byistro-proletel.mp3")
 
# Шрифт
instruction_font = pygame.font.Font(None, 30)
heading_font = pygame.font.Font(None, 50)
def instructions():
    instruction_text = [
        "Инструкция:",
        "1. Ипользуйте мышь, чтобы прицеливаться и нажать, чтобы стрелять в призраков",
        "2. Уничтожьте как можно больше призраков, прежде чем они достигнут вершину",
        "3. Избегайте попадения на нижнию платформу или попадания мимо призраков",
        "4. Нажмите 'Q' чтобы выйти из игры",
        "5. Нажмите 'R' чтобы перезагрузить игру",
        "",
        "Нажмите в любом месте,чтобы начать игру"
    ]