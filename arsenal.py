"""
Name: Alien Invasion
Author: Jordan Mensah
Purpose: Manages the ships arsenal of active bullets with firing limits, updating positions 
and the drawing and removal of bullets
Date: 10/18/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741609_1/overview?linkContentId=_28741609_1&courseId=_238744_1
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion    

class ShipArsenal:
    """Class to manage ships arsenal and active bullets
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initalizes the arsenal and creates empty sprite group for the bullets

        Args:
            game (AlienInvasion): Reference to active game instance
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Updates position of bullets and remove bullets that went offscreen
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Removes bullets from sprite group once they have gone offscreen
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draws the active bullets onto the screen
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Creates and new bullet and adds to the arsenal if bullet limit is not reached

        Returns:
            bool: True if bullet was created/fired, False otherwise
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    
        
