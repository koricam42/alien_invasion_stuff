"""
Name: Alien Invasion
Author: Jordan Mensah
Purpose: Manages the ships arsenal of active bullets with firing limits, updating positions 
and the drawing and removal of bullets
Date: 10/18/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741609_1/overview?linkContentId=_28741609_1&courseId=_238744_1
"""

import pygame
import random
from bullet import Bullet, EnemyBullet
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion    

class ShipArsenal:
    """Class to manage ships arsenal and active bullets""" 

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initalizes the arsenal and creates empty sprite group for the bullets

        Args:
            game (AlienInvasion): Reference to active game instance
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

        self.fire_mode = 'normal'

    def update_arsenal(self) -> None:
        """Updates position of bullets and remove bullets that went offscreen
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Removes bullets from sprite group once they have gone offscreen"""
        
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draws the active bullets onto the screen""" 

        for bullet in self.arsenal.sprites():
            bullet.draw_bullet()

    def fire_bullet(self): # Split firing modes into seperate methods later
        """Fires a bullet(s) depending on current firing mode
        Returns:
            bool: True if bullet was created/fired, False otherwise
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            if self.fire_mode == 'normal':
                new_bullet = Bullet(self.game)
                self.arsenal.add(new_bullet)
            elif self.fire_mode == 'spread':
                spread_speed = self.settings.bullet_spread_speed

                left_bullet = Bullet(self.game, x_speed=-spread_speed)
                center_bullet = Bullet(self.game)
                right_bullet = Bullet(self.game, x_speed=spread_speed)

                self.arsenal.add(left_bullet, center_bullet, right_bullet)

            return True
        return False

class EnemyArsenal:
    """Class to manage the alien fleet's arsenal and active bullets"""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initalizes the arsenal and creates empty sprite group for the bullets
        
        Args:
            game (AlienInvasion): Reference to active game instance
        """

        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def spawn_test_bullet(self) -> None:
        """Spawns a test bullet at a random top position for testing"""

        if random.randint(0, 100) <= 2:
            x = random.randint(0, self.settings.screen_w)
            y = 0
            new_bullet = EnemyBullet(self.game, x, y)

            self.arsenal.add(new_bullet)

    def update(self) -> None:
        """Updates position of bullets and remove bullets that went offscreen"""

        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Removes bullets from the sprite group once they have gone offscreen"""

        for bullet in self.arsenal.copy():
            if bullet.rect.top >= self.settings.screen_h:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draws the active enemy bullets onto the screen"""

        for bullet in self.arsenal.sprites():
            bullet.draw_bullet()
