"""
Name: Play Button
Author: Jordan Mensah
Purpose: Defines the button that starts the game
Date: 10/31/26
Source Code:
"""
import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    """Class to manage the button that starts the game"""

    def __init__(self, game: 'AlienInvasion', msg) -> None:
        """Initializes the button with the game instance and message"""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.font = pygame.font.Font(self.settings.font_file,
            self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._preg_msg(msg)

    def _preg_msg(self, msg) -> None:
        """Prepares the message to be displayed on the button"""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draws the button on the screen"""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        """Checks if the button was clicked based on the mouse position"""
        return self.rect.collidepoint(mouse_pos)