"""
Name: Alien Invasion
Author: Jordan Mensah
Purpose: Holds...
Date: 10/25/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741609_1/overview?linkContentId=_28741609_1&courseId=_238744_1
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion    

class GameStats():

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self) -> None:
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
     
    def update(self, collisions) -> None:
        # update score
        self._update_score(collisions) 
        # update max score
        self._update_max_score()
        # update hi-score


    def _update_max_score(self) -> None:
        if self.score > self.max_score:
            self.max_score = self.score

        # print(f"Max: {self.max_score})")

    def _update_score(self, collisions) -> None:
        for aliens in collisions.values():
            self.score += self.settings.alien_points

        # print(f"Basic: {self.score}")

    def update_level(self) -> None:
        self.level += 1
        print(self.level)


    