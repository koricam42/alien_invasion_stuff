"""
Name: Alien Invasion
Author: Jordan Mensah
Purpose: Main module for the alien invasion game that handles the loop, displaying the window
user input events, and updating the screen
Date: 10/18/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741609_1/overview?linkContentId=_28741609_1&courseId=_238744_1
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import ShipArsenal
# from alien import Alien
from alien_fleet import AlienFleet

class AlienInvasion:
    """Class to manage game state and behavior
    """
    def __init__(self) -> None:
        """Initalizes the game, settings, display, audio mixer, and ship
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        self.ship = Ship(self, ShipArsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

    def run_game(self) -> None:
        """Starts and runs the game loop at a set frame rate
        """
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien_fleet.update_fleet()
            self._check_collisons()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisons(self) -> None:
        # check collsions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._reset_level()
            # Subtract one life if possible

        # check collisions for alien and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._reset_level()
            
        # check collisons of projectiles and aliens
        collisions = self.alien_fleet.check_collisons(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
        

            
    def _reset_level(self) -> None:
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _update_screen(self) -> None:
        """Redrawss the screen and ship, then flips it to the new display
        """
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_events(self) -> None:
        """Checks for keypresses and game quit events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event) -> None:
        """Responds to keypresses to stop ship movement

        Args:
            event (pygame.event): Pygame keyup event containing the released key
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _check_keydown_events(self, event) -> None:
        """Responds to keypresses for movement, game exiting, and firing lasers

        Args:
            event (pygame.event): Pygame keydown event with the pressed key
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play() 
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit

if __name__ == '__main__':
    """Creates a game instance to run the game
    """
    ai = AlienInvasion()
    ai.run_game()