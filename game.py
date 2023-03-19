import pygame as pg
from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = Lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get.random.position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

while True:
  for event in pg.event():
    if event.type == pg.QUIT:
         exit()
    if event.type == pg.KEYDOWN:
       if event.key == pg.K_w:
         snake_dir = (0, - TILE_SIZE)
       if event.key == pg.K_s:
         snake_dir = (0, - TILE_SIZE)
       if event.key == pg.K_s:
         snake_dir = (-TILE_SIZE, 0)
       if event.key == pg.K_d:
         snake_dir = (TILE_SIZE, 0)
     # draw snake
     [pg.draw.rect(screen, 'green', segment) for segment in segments]
     # move snake
     snake.move_ip(snake_dir)
     segments.append(snake.copy())
     segments= segments[-length:]
     screen.fill('black')
     pg.display.flip()
     clock.tick(60)
