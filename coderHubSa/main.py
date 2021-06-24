
import requests
import typing

get_challenge_url = "https://api.coderhub.sa/api/challenges/detail/{}"
challenges_url = "https://api.coderhub.sa/api/challenges/filtered-list/"


class CoderHub():
    def __init__(self):
        pass

    def get_challenge_by_id(self, id: int):
        """ Returns challenge object by id

        Args:
            id (int): id of challenge

        Raises:
            Exception: Invalid challenge id

        Returns:
            dict: object of challenge
        """
        request = requests.get(get_challenge_url.format(str(id)))
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Invalid challenge id: challenge id not found")