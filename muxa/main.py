import pygame, sys
from classes import *
from process import *

 #Creates the Screen/Page of the Game!

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 25
total_frames = 0


bug = Bug(0, SCREENHEIGHT - 40, "images/bug.png")


# ---------- Main Program Loop (All of the Drawing and other main Stuff!) ---------
while True:
 
	pygame.display.set_caption('Fly Swatter - XanonDevelopment')


	process(bug, FPS, total_frames)
	#PROCESSES

	#LOGIC       
	bug.motion(SCREENWIDTH, SCREENHEIGHT)
	Fly.update_all(SCREENWIDTH, SCREENHEIGHT)
	BugProjectile.movement()
	total_frames += 1 
#Code Bellow randomises background color, Commented as is pretty useless.
	#i += 1
	#if i > 255:
	#	i %= 255

	
	#LOGIC

	#DRAW
	screen.blit(background, (0, 0))
	BaseClass.allsprites.draw(screen)
	BugProjectile.List.draw(screen)
	pygame.display.flip()
	#DRAW

	clock.tick(FPS)