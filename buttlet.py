import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage butllets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) using pygame.Rect(). 
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        
        # Set bullet correct position. 
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float. 
        # float = float(integer)
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet. 
        # move up to decreasing y-coordinate value.
        self.y -= self.settings.bullet_speed
        # Update the rect position. 
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)