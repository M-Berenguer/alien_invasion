"""
This file contains the settings for the the Alien Invasion.
"""

class Settings:
    """
    This class contains the settings for the Alien Invasion.
    """

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.caption = "Alien Invasion"

        # Ship settings
        self.ship_speed = 1.5
