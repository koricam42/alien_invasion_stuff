"""
Name: Powerups
Author: Jordan Mensah
Purpose: Powerups for the alien invasion game
Date: 11/14/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741564_1/attempt/create?courseId=_238744_1
"""
import pygame 
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Powerup(Sprite):
    """Class to manage falling powerups"""

    def __init__(self, game: 'AlienInvasion', x) -> None:
        """Initalizes a powerup at a random point at the top of the screen"""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        
        self.type =  random.choice(['spread', 'shield'])

        self.image = pygame.image.load(self.settings.powerup_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.powerup_w, self.settings.powerup_h)
            )

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = x
        self.rect.top = self.screen_rect.top
        
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Moves the powerup down the screen"""
        self.y += self.settings.powerup_drop_speed
        self.rect.y = self.y

    def draw_powerup(self) -> None:
        """Draws the powerup to the screen"""
        self.screen.blit(self.image, self.rect)