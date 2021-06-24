"""
This will be the file that is the main file, to work on the coderHubSa project, 
the project will be a library that helps you access the contents of the coderHub.sa site
"""

import requests
import typing

get_challeng_url = "https://api.coderhub.sa/api/challenges/detail/{}"
challenges_url = "https://api.coderhub.sa/api/challenges/filtered-list/"

class CoderHub():
    def __init__(self):
        pass