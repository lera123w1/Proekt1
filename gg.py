import pygame
import sys
import random
from math import *
pygame.init()
 
width = 200
height = 1000

# Загрузка фотографии место (где будет происходить)

background_image = pygame.image.load("assets\\images\\Gost.jpg")
background_image = pygame.transform.scale(background_image, (width, height))
 
# Загрузка призрака изображений 

ghost_image = pygame.image.load("assets\\images\\Prizrak.jpg")


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