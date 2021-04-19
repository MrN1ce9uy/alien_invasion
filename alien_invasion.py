import sys

import pygame

def run_game():
	#Initialize game and create a screen object
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Set the background color.
	bg_color = (220, 220, 220)
	
	# Start the main loop for the game.
	while True:
	
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		# Redraw the screen during each pass through the loop.
		screen.fill(ai_settings.bg_color)
				
		# Make the most recently drawn screeen visible.
		pygame.display.flip()
		
run_game()