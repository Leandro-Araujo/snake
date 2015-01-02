import pygame
import random
from pygame.locals import *

def isPointInsideRect(x, y, rect):
	if (x >= rect.left) and (x <= rect.right) and (y >= rect.top) and (y <= rect.bottom):
		return True
	else:
		return False

pygame.init()

black = [ 0 , 0 , 0]
white = [255 ,255 ,255]
foodx = random.randrange(0, 100)
foody = random.randrange(0, 100)
snakex = []
snakey = []
snakex.append(0)
snakey.append(0)

size =[1000 ,600]
screen = pygame.display.set_mode( size )
pygame.display.set_caption( "Snake" )
screen.fill(white)
clock = pygame.time.Clock()

done = False

cont = 0
dir = 'dir'
b = pygame.draw.rect(screen, black, [foodx*5, foody*5, 20, 20], 0)
while done == False :
	screen.fill(white)
	b = pygame.draw.rect(screen, black, [foodx*5, foody*5, 20, 20], 0)

	


	for event in pygame.event.get() : # User did something
		if event.type == pygame.QUIT : # If user clicked close
			done = True 
	
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			snakex.append(snakex[len(snakex) - 1] - 5)
			snakey.append(snakey[len(snakey) - 1])
			snakex.pop(0)
			snakey.pop(0)
			print snakex, snakey
			dir = 'left'

		if event.key == pygame.K_RIGHT:
			snakex.append(snakex[len(snakex) - 1] + 5)
			snakey.append(snakey[len(snakey) - 1])
			snakex.pop(0)
			snakey.pop(0)
			print snakex, snakey
			dir = 'right'

		if event.key == pygame.K_UP:
			snakex.append(snakex[len(snakex) - 1])
			snakey.append(snakey[len(snakey) - 1] - 5)
			snakex.pop(0)
			snakey.pop(0)
			print snakex, snakey
			dir = 'up'

		if event.key == pygame.K_DOWN:
			snakex.append(snakex[len(snakex) - 1])
			snakey.append(snakey[len(snakey) - 1] + 5)
			snakex.pop(0)
			snakey.pop(0)
			print snakex, snakey
			dir = 'down'

	else:
		if dir == 'left':
			snakex.append(snakex[len(snakex) - 1] - 5)
			snakey.append(snakey[len(snakey) - 1])
			snakex.pop(0)
			snakey.pop(0)
			print snakex, snakey
			dir = 'left'

		if dir == 'right':
			snakex.append(snakex[len(snakex) - 1] + 5)
			snakey.append(snakey[len(snakey) - 1])
			snakex.pop(0)
			snakey.pop(0)
			print snakex, snakey
			dir = 'right'

		if dir == 'up':
			snakex.append(snakex[len(snakex) - 1])
			snakey.append(snakey[len(snakey) - 1] - 5)
			snakex.pop(0)
			snakey.pop(0)
			print snakex, snakey
			dir = 'up'

		if dir == 'down':
			snakex.append(snakex[len(snakex) - 1])
			snakey.append(snakey[len(snakey) - 1] + 5)
			snakex.pop(0)
			snakey.pop(0)
			print snakex, snakey
			dir = 'down'


	for i in range(len(snakex)):
		a = pygame.draw.rect(screen, black, [snakex[i], snakey[i], 20, 20], 0)

	
	if(isPointInsideRect(a.left, a.top, b) or isPointInsideRect(a.left, a.bottom, b) or isPointInsideRect(a.right, a.top, b) or isPointInsideRect(a.right, a.bottom, b)):
		if dir == 'left':
			snakex.append(snakex[len(snakex) - 1] - 5)
			snakey.append(snakey[len(snakey) - 1])
			
			dir = 'left'

		if dir == 'right':
			snakex.append(snakex[len(snakex) - 1] + 5)
			snakey.append(snakey[len(snakey) - 1])
			
			dir = 'right'

		if dir == 'up':
			snakex.append(snakex[len(snakex) - 1])
			snakey.append(snakey[len(snakey) - 1] - 5)
			
			dir = 'up'

		if dir == 'down':
			snakex.append(snakex[len(snakex) - 1])
			snakey.append(snakey[len(snakey) - 1] + 5)
			
			dir = 'down'
		foodx = random.randrange(0, 100)
		foody = random.randrange(0, 100)
		b = pygame.draw.rect(screen, black, [foodx*5, foody*5, 20, 20], 0)
	pygame.display.flip()
	clock.tick(20)

