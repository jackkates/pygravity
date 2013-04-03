import pygame, sys

pygame.init()

size = width, height = 500, 500
bg_color = (0, 0, 0)

screen = pygame.display.set_mode(size)

done = False
while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill(bg_color)

pygame.quit()
sys.exit()
