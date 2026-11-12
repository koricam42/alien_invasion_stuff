"""
Name: Game Settings
Author: Jordan Mensah
Purpose: Stores game speeds, filepaths, dimensions, and configurables
Date: 10/18/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741609_1/overview?linkContentId=_28741609_1&courseId=_238744_1
"""
from pathlib import Path  

class Settings:
    """Class to store game settings"""

    def __init__(self) -> None:
        """Initalizes the games settings and asset filepaths"""
        self.name: str = 'Alien Invasion - Track 1 Mechanics'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2    
        self.fleet_direction = 1  

        self.button_w =  200
        self.button_h = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' /'Audiowide-Regular.ttf'

    def initialize_dynamic_settings(self) -> None:
        """Initalizes settings that change throughout the game"""
        self.ship_speed = 5
        self.starting_ship_count = 3
        
        self.bullet_speed = 7
        self.bullet_amount = 5
        self.bullet_w = 25
        self.bullet_h = 80

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self) -> None:
        """Increases the speed of the game and the points for each alien"""
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
