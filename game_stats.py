"""
Name: Game Stats
Author: Jordan Mensah
Purpose: Holds the game statistics and handles saving and loading scores
Date: 10/25/26
Source Code: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741609_1/overview?linkContentId=_28741609_1&courseId=_238744_1
"""
# from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion    

class GameStats():
    """Class to track the game statistics"""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initializes the game statistics with the game instance"""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self) -> None:
        """Initializes the saved scores from the scores file"""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            # save the file

    def save_scores(self) -> None:
        """Saves the current high score to the scores file"""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"Error: File not found: {e}")

    def reset_stats(self) -> None:
        """Resets the game stats to their initial values"""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
     
    def update(self, collisions) -> None:
        """Updates the game statistics based on collisions"""
        # update score
        self._update_score(collisions) 
        # update max score
        self._update_max_score()
        # update hi-score
        self._update_hi_score()

    def _update_max_score(self) -> None:
        """Updates the max score if the current score exceeds it"""
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f"Max: {self.max_score})")

    def _update_hi_score(self) -> None:
        """Updates the high score if the current score exceeds it"""
        if self.score > self.hi_score:
            self.hi_score = self.score
        # print(f"Max: {self.hi_score})")

    def _update_score(self, collisions) -> None:
        """"Updates the score based on the number of aliens hit

        Args:
            collisions (dict): The collisions that occurred in the game,
            used to update the score based on the number of aliens hit.
        """
        for aliens in collisions.values():
            self.score += self.settings.alien_points * len(aliens)

        # print(f"Basic: {self.score}")

    def update_level(self) -> None:
        """Increases the level by 1"""
        self.level += 1
        print(self.level)


    