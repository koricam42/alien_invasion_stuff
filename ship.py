"""
Name: Alien Invasion
Author: Jordan Mensah
Purpose: Manages ship position, boundaries of movement, weapon firing, and rendering
Date: 10/18/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741609_1/overview?linkContentId=_28741609_1&courseId=_238744_1
"""
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import ShipArsenal

class Ship:
    """Class to manage the players ship
    """
    def __init__(self, game: "AlienInvasion", arsenal: 'ShipArsenal') -> None:
        """Initalizes the ship, loads its assets, set its starting position, and give its arsenal

        Args:
            game (AlienInvasion): The reference to the active game instance
            arsenal (ShipArsenal): The weapon arsenal instance attached to the ship
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update(self) -> None:
        """
        Updates ships movement and its arsenal
        """
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self) -> None:
        """Moves ship left or right while keeping it within screen boundaries
        """
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right <  self.boundaries.right:
            self.x += temp_speed
        elif self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self) -> None:
        """Draws the arsenals bullets with the ship at current location
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Attempts to fire a bullet from the arsenal

        Returns:
            bool: True if bullet was fired, else false if 5 bullet ammo limit was reached
        """
        return self.arsenal.fire_bullet()
        