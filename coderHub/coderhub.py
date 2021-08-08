# -*- coding: utf-8 -*-
import requests
from typing import Optional, Union


class CoderHub():
    def __init__(self):
        self.host = "https://api.coderhub.sa/api"
        self.get_challenge_url = self.host+"/challenges/detail/{}"
        self.challenges_url = self.host+"/challenges/filtered-list/?page_size=9999999999&query="
        self.programming_languages_url= self.host+"/challenges/programming-languages"
        self.leaderBoard_url = self.host+"/leaderboard/?language={0}&offset=0&limit=10&type={1}"
        self.profile_url = self.host+"/profile/public/{}"
        self.user_statistics = self.host+"/profile/public/get-user-statistics/{}"
        
    def get_challenges(self, difficulty: Optional[Union[str, None]] = None):
        """ Returns all challenges by difficulty, if difficulty not None, else he will return all challenges
        difficulty should be in ['سهل', 'متوسط', 'صعب']

        Args:
            difficulty (Optional[Union[str, None]], optional): difficulty of challenges. Defaults to None.
        
        Raises:
            Exception: Invalid difficulty
        
        Returns:
            dict: dictionary of challenges
        """
        challenges = requests.get(self.challenges_url).json()
        difficulty_list = ['سهل', 'متوسط', 'صعب']
        if difficulty:
            if difficulty in difficulty_list:
                return {'result':list(filter(
                    lambda challenge: challenge['type_of_level']['name'] == difficulty,
                        challenges['result']))}
            else:
                raise Exception(f"difficulty must be {' or '.join(difficulty_list)}")
        else:
            return {'result':challenges['result']}
    
    def search_challenges(self, word: str):
        data = requests.get(self.challenges_url+word).json()
        if data['count'] > 0:
            return data
        else:
            raise Exception("There are no challenges available about '%s'" % word)

    def get_challenge_by_id(self, challenge_id: str):
        """ Returns challenge object by id

        Args:
            id (str): id of challenge

        Raises:
            Exception: Invalid challenge id

        Returns:
            dict: object of challenge
        """
        request = requests.get(self.get_challenge_url.format(challenge_id))
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Invalid challenge id: challenge not found")
    
    def get_languages(self, language: Optional[Union[str, None]] = None):
        """ Returns all objects of languages if language = None, else object by language

        Args:
            language (Optional[Union[str, None]], optional): language you want. Defaults to None.

        Raises:
            Exception: Language not found
            
        Returns:
            dict: object of language or languages
        """
        languages = list(map(
                    lambda lang: {'id': lang['id'], 
                                        'name': lang['name'].lower(), 
                                            'version': lang['version']},
                    requests.get(self.programming_languages_url).json()))
        if language:
            if type(language) == str:
                languages = list(filter(
                    lambda lang: lang['name'] == language.lower(),
                    languages
                ))
            else:
                languages = [] # empty list, because invalid language
            if languages:
                return languages[0]
            else:
                raise Exception(f"Invalid language, '{language}' not found")
        else:
            return {'result':languages}

    def get_leaderBoard(self, language: str, search_type: Optional[Union[str]] = "ALL"):
        """ get first 10 users in leaderboard of language, in all time or by type
            type should be in [ALL, DAILY, WEEKLY]

        Args:
            language (str): The programming language you want to have its own leaderboard 
            search_type (Optional[Union[str]], optional): type of search. Defaults to "ALL".

        Raises:
            Exception: Unknown language, language not found
            Exception: invalid search type, type not found

        Returns:
            dict: dictionary of leaderboard
        """
        language, search_type = language.lower(), search_type.upper()
        types = ["ALL", "DAILY", "WEEKLY"]
        languages = self.get_languages()
        languages_names = list(map(lambda lang: lang['name'], languages['result']))
        languages_ids = list(map(lambda lang: lang['id'], languages['result']))
        if language in languages_names:
            if search_type in types:
                id = languages_ids[languages_names.index(language)]
                leaderboard = requests.get(self.leaderBoard_url.format(id, search_type)).json()['leaderboard']
                return {'leaderboard': leaderboard}
            else:
                raise Exception("Invalid search type, '%s' not found, search_type should be  %s"  % (search_type, ' or '.join(types)))
            
        else:
            raise Exception("Unknown language, '%s' not found, language should be  %s" % (language, ' or '.join(languages_names)))
    def get_profile(self, username:str):
        """ Returns profile for username

        Args:
            username (str): username of user

        Raises:
            Exception: ['user profile is not public', 'user profile is not found']

        Returns:
            dict: dictionary of user data
        """
        data = requests.get(self.profile_url.format(username.lower())).json()
        if "detail" in data.keys():
            raise Exception(data['detail'])
        else:
            return data
    def get_user_statistics(self, username:str):
        """ Returns user statistics

        Args:
            username (str): name of user

        Returns:
            dict: dictionary of user statistics
        """
        user_id = self.get_profile(username=username)['user_information']['id']
        data = requests.get(self.user_statistics.format(user_id)).json()
        return data