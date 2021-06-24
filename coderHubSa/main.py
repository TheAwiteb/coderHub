"""
This will be the file that is the main file, to work on the coderHubSa project, 
the project will be a library that helps you access the contents of the coderHub.sa site
"""

import requests
from typing import Optional, Union

get_challenge_url = "https://api.coderhub.sa/api/challenges/detail/{}"
challenges_url = "https://api.coderhub.sa/api/challenges/filtered-list/?page_size=9999999999"

class CoderHub():
    def __init__(self):
        pass
    def get_challengs(self, difficulty: Optional[Union[str, None]] = None):
        """ Returns all challenges by difficulty, if difficulty not None, else he will return all challenges
        difficulty should be in ['easy', 'normal', 'hard']

        Args:
            difficulty (Optional[Union[str, None]], optional): difficulty of challenges. Defaults to None.
        
        Raises:
            Exception: Invalid difficulty
        
        Returns:
            dict: dictionary of challenges
        """
        challenges = requests.get(challenges_url).json()
        difficulty_list = ['easy', 'normal', 'hard']
        if difficulty:
            if difficulty in difficulty_list:
                difficulty_id = difficulty_list.index(difficulty) + 2 # coderHub count start from 2
                return {'result':list(filter(
                    lambda challenge: challenge['type_of_level']['id'] == difficulty_id,
                        challenges['result']))}
            else:
                raise Exception(f"difficulty must be {' or '.join(difficulty_list)}")
        else:
            return challenges['result']