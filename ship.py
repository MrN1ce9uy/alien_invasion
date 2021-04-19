import game

class Ship():

	def __init__(self, screen):
		"""Initialize the ship and set its starting position."""
		self.screen = screen
		
		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_ret = screen.get_rect()
		
		# Start each new ship at teh bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)