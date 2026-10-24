"""
Name: Alien Invasion
Author: Jordan Mensah
Purpose: Defines the alien...
Date: 10/21/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741609_1/overview?linkContentId=_28741609_1&courseId=_238744_1
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Class that manages fired bullets from the players ship
    """
    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """Initalizes a bullet object at the current midtop position

        Args:
            game (AlienInvasion): Reference to the active alien invasion instance
        """
        super().__init__()
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_w, self.settings.alien_h)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self) -> None:
        temp_speed = self.settings.fleet_speed

        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.y += self.settings.fleet_drop_speed

        self.x += temp_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)
        
      
    def draw_alien(self) -> None:
        """Draws the alien onto the screen
        """
        self.screen.blit(self.image, self.rect)
    