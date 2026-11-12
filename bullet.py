"""
Name: Alien Invasion
Author: Jordan Mensah
Purpose: Defines the bullet fired from the arsenal
Date: 10/18/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741609_1/overview?linkContentId=_28741609_1&courseId=_238744_1
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Class that manages fired bullets from the players ship
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initalizes a bullet object at the current midtop position

        Args:
            game (AlienInvasion): Reference to the active alien invasion instance
            x (int): The x coordinate of the bullet.
            y (int): The y coordinate of the bullet.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.bullet_w, self.settings.bullet_h)
        )

        self.rect = self.image.get_rect()

        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Moves the bullet up the screen based on currently configured bullet speed
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Draws the bullet onto the screen
        """
        self.screen.blit(self.image, self.rect)

class EnemyBullet(Sprite):
    """Class that manages fired bullets from the alien fleet"""

    def __init__(self, game: 'AlienInvasion', x, y) -> None: # Temp replace alien with x,y coord for testing, add back later
        """Initalizes a bullet object at the current midbottom position

        Args:
            game (AlienInvasion): Reference to the active alien invasion instance
            x (int): The x coordinate of the enemy bullet.    
            y (int): The y coordinate of the enemy bullet.
        """

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_w, self.settings.bullet_h))

        self.rect = self.image.get_rect()

        self.rect.midbottom = (x, y) # alien.rect.midbottom replaced with x,y for testing, add back later
        self.y = float(self.rect.y)
    
    def update(self) -> None:
        """Moves the bullet down the screen based on currently configured bullet speed"""
        self.y += self.settings.enemy_bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Draws the bullet onto the screen"""
        self.screen.blit(self.image, self.rect)




        