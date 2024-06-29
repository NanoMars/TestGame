import sys
import pygame
from pygame.locals import *

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

player = pygame.Rect((300,250,50,50))

while True:

  screen.fill((0,0,0))
  
  pygame.draw.rect(screen, (255,0,0), player)

  key = pygame.key.get_pressed()
  if key[pygame.K_a] == True:
      player.move_ip(-1,0)
  if key[pygame.K_d] == True:
      player.move_ip(1,0)
  if key[pygame.K_w] == True:
      player.move_ip(0,-1)
  if key[pygame.K_s] == True:
      player.move_ip(0,1)
      
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()