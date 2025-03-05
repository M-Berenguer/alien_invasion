"""
From the book "Python Crash Course" by Eric Matthes

Alien Invasion is a game where the player controls a ship that can move left and right. 
The player can shoot bullets to destroy the aliens that are moving left and right across the screen. 
The player must destroy all the aliens to move to the next level. If the aliens reach the bottom of 
the screen, the player loses a ship. If the player loses all their ships, the game is over.

"""

import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """General class to manage game resources and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60) # Limit the game to 60 frames per second.

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    # Create an instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()
