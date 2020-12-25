import pygame
import numpy as np

class Const:
  """
  常量
  """
  def __init__(self):
    self.SCREEN_WIDTH = 500
    self.SCREEN_HEIGHT = 400
    self.SIZE = 4
    self.TILE_X = 10
    self.TILE_Y = 10
    self.TILE_WIDTH = 100
    self.TILE_HEIGHT = 90
PARAM = Const()

class Library:
  """
  图片库
  """
  def __init__(self):
    self.tile = pygame.image.load("assets/tile.png").convert_alpha() # 地砖
    self.hero = pygame.image.load("assets/hero.png").convert_alpha() # 英雄
    self.monster = pygame.image.load("assets/monster.png").convert_alpha() # 怪物
    self.pit = pygame.image.load("assets/pit.png").convert_alpha() # 陷阱
    self.gold = pygame.image.load("assets/gold.png").convert_alpha() # 黄金

class Game():
  """
  游戏
  """
  lib = {}
  def __init__(self):
    self.fpsClock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((PARAM.SCREEN_WIDTH, PARAM.SCREEN_HEIGHT))
    self.map = np.zeros(PARAM.SIZE * PARAM.SIZE - 3)
    self.map[0] = 10
    self.map[1] = 21
    self.map[2] = 22
    self.map[3] = 22
    self.map[4] = 22
    np.random.shuffle(self.map)
    self.map = np.insert(self.map, 0, 1)
    self.map = np.insert(self.map, 1, 0)
    self.map = np.insert(self.map, PARAM.SIZE, 0)
    self.map.resize((PARAM.SIZE, PARAM.SIZE))
    self.lib = Library()
  def show(self):
    self.screen.fill((0,0,0))
    for m, row in enumerate(self.map):
      for n, col in enumerate(row):
        x = PARAM.TILE_X + n * PARAM.TILE_WIDTH
        y = PARAM.TILE_Y + m * PARAM.TILE_HEIGHT
        self.screen.blit(self.lib.tile, (x, y))
        if col == 10:
          self.screen.blit(self.lib.gold, (x, y))
        elif col == 21:
          self.screen.blit(self.lib.monster, (x, y))
        elif col == 22:
          rect = self.lib.pit.get_rect()
          x += (PARAM.TILE_WIDTH - rect.width) / 2
          y += (PARAM.TILE_HEIGHT - rect.height) / 2
          self.screen.blit(self.lib.pit, (x, y))
        elif col == 1:
          self.screen.blit(self.lib.hero, (x, y))
  def run(self):
    running = True
    while running:
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
