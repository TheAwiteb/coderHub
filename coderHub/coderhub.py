# -*- coding: utf-8 -*-
import requests
from typing import Optional, Union


class CoderHub():
    def __init__(self):
        self.get_challenge_url = "https://api.coderhub.sa/api/challenges/detail/{}"
        self.challenges_url = "https://api.coderhub.sa/api/challenges/filtered-list/?page_size=9999999999"
        self.programming_languages_url= "https://api.coderhub.sa/api/challenges/programming-languages"
        self.leaderBoard_url = "https://api.coderhub.sa/api/leaderboard/?language={0}&offset=0&limit=10&type={1}"

    def get_challenges(self, difficulty: Optional[Union[str, None]] = None):
        """ Returns all challenges by difficulty, if difficulty not None, else he will return all challenges
        difficulty should be in ['easy', 'normal', 'hard']

        Args:
            difficulty (Optional[Union[str, None]], optional): difficulty of challenges. Defaults to None.
        
        Raises:
            Exception: Invalid difficulty
        
        Returns:
            dict: dictionary of challenges
        """
        challenges = requests.get(self.challenges_url).json()
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
            return {'result':challenges['result']}

    def get_challenge_by_id(self, id: str):
        """ Returns challenge object by id

        Args:
            id (str): id of challenge

        Raises:
            Exception: Invalid challenge id

        Returns:
            dict: object of challenge
        """
        request = requests.get(self.get_challenge_url.format(id))
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

    def get_leaderBoard(self, language: Optional[Union[str, "java"]] = "java",
                        type: Optional[Union[str, "ALL"]] = "ALL"):
        """ Returns the first 10 ranks in leader boards objects of java language and for ALL time
            if language = "java" or type="ALL" , else object by specific language or at different type of times

              Args:
                  language (Optional[Union[str, "java"]], "java"): language you want. Defaults to "java".
                  type (Optional[Union[str, "ALL"]], "ALL"): language you want. Defaults to "ALL".

              Raises:
                  Exception: Language or Type not found

              Returns:
                  dict: object of the first 10 ranks in leader boards objects for java language all the time
                        or the first 10 ranks in leader boards objects for other language and other type of times
              """
        languages = list(map(
            lambda lang: {'id': lang['id'],
                          'name': lang['name'].lower(), },
            requests.get(self.programming_languages_url).json()))
        types = ['ALL', 'DAILY', 'WEEKLY']

        if language:
            languages = list(filter(
                lambda lang: lang['name'] == language.lower(),
                languages
            ))
            if languages:
                lang = str(languages[0]['id'])
            else:
                raise Exception(f"Invalid language, '{language}' not found")
        if type:
            if not (type in types):
                raise Exception(f"Invalid type, '{type}' not found")

        request = requests.get(self.leaderBoard_url.format(lang, type)).json()
        return request
