import sys
import pygame
from pygame.locals import *

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

player = pygame.Rect((300,250,50,50))

while True:

  pygame.draw.rect(screen, (255,0,0), player)

  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()