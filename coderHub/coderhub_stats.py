"""

the purpose of this file is to collect data from coderhub.sa API, prepare and group it
to make it easier to start analysing the data

"""

import pandas
import pandas as pd
import time
from coderhub import CoderHub
import threading


class CoderHubStats(CoderHub):
    users_data = {}
    threads_lst = []

    def get_challenges_stats(self) -> pandas.DataFrame:
        """
        get easy challenges count, medium challenges count, hard
            challenges count and aal challenges together count

        Example result :
            all_challenges                98.00
            easy_challenges               56.00
            medium_challenges             31.00
            hard_challenges               11.00
            easy_challenges_percentage    57.14
            medium_challenges_percentage  31.63
            hard_challenges_percentage    11.22

        Returns:
            pandas.Dataframe
        Exceptions :
            - requests.exceptions.ConnectionError
        """
        load_data = CoderHub.get_challenges(self)
        df = pd.json_normalize(load_data['result'])

        # count challenges
        all_challenges_count = len(df)
        easy_challenges_count = len(df[df["type_of_level.name"] == "سهل"])
        med_challenges_count = len(df[df["type_of_level.name"] == "متوسط"])
        hard_challenges_count = len(df[df["type_of_level.name"] == "صعب"])

        # calculate challenges percentages
        easy_challenges_percentage = (easy_challenges_count/all_challenges_count)*100
        med_challenges_percentage = (med_challenges_count/all_challenges_count)*100
        hard_challenges_percentage = (hard_challenges_count/all_challenges_count)*100

        # rounding numbers
        easy_challenges_percentage = round(easy_challenges_percentage, 2)
        med_challenges_percentage = round(med_challenges_percentage, 2)
        hard_challenges_percentage = round(hard_challenges_percentage, 2)

        challenges_stats = {
            'all_challenges': all_challenges_count,
            'easy_challenges': easy_challenges_count,
            'medium_challenges': med_challenges_count,
            'hard_challenges': hard_challenges_count,
            'easy_challenges_percentage': easy_challenges_percentage,
            'medium_challenges_percentage': med_challenges_percentage,
            'hard_challenges_percentage': hard_challenges_percentage
        }
        return pd.DataFrame().from_dict(challenges_stats, orient='index')

    def get_languages_names(self):
        """
        Returns:
            a list containing all programing languages names available in coderhub.sa
        Exceptions :
            - requests.exceptions.ConnectionError
        """
        load_data = CoderHub.get_languages(self)
        languages = [i['name'] for i in load_data['result']]
        return languages

    def get_leaderboard_datatable(self) -> pandas.DataFrame:
        """
        get top 10 users for every language, their rank and their point from the leaderboard

        Example result :
                            users  points  rank    language
            0           ahmed0ksa   921.0     1       swift
            1             alxd7my   911.0     2       swift
            2               iX901   906.0     3       swift
            3           ahmadajr1   906.0     4       swift
            4              vdotup   906.0     5       swift

        Returns:
            pandas.DataFrame
        Exceptions :
            - requests.exceptions.ConnectionError
        """
        leaderboard_df = pd.DataFrame()
        pts_lst = []
        rnk_lst = []
        lng_lst = []
        users_lst = []

        for lang in self.get_languages_names():
            top10_users = self.get_leaderBoard(lang)['leaderboard']
            for user in top10_users:
                pts_lst.append(user['points'])
                rnk_lst.append(user['rank'])
                lng_lst.append(str(lang))
                users_lst.append(user['user_info']['username'])
        leaderboard_df.insert(0, "language", lng_lst)
        leaderboard_df.insert(0, "rank", rnk_lst)
        leaderboard_df.insert(0, "points", pts_lst)
        leaderboard_df.insert(0, "users", users_lst)
        return leaderboard_df

    def fetch_user_data(self, user):
        """
        fetch user information (provided by the API) and append it to users_data dictionary, if user
        profile is private the value will be 'private' for that user
        Args:
            user:
                username that will be passed to get_user_statistics()
        Returns:
            None
        Exceptions :
        - requests.exceptions.ConnectionError
        """
        try:
            user_data = self.get_user_statistics(user)
            self.users_data[str(user)] = user_data
        except Exception :
            self.users_data[str(user)] = "private"

    def get_top_users_stats(self) -> pandas.DataFrame:
        """
        expand the data given from get_leaderboard_datatable() and add more information

        Example result :
                users	  points rank language	total_challenges_solved	 total_challenges_solved_all_languages  ...
            0	ahmed0ksa	921	  1	  swift	        107	                        107
            1	alxd7my	    911	  2	  swift	        106	                        114
            2	iX901	    906	  3	  swift	        105	                        105
            3	ahmadajr1	906	  4	  swift	        105	                        105
            4	nnoaid	    906	  8	  python	  private	                  private
            ...

        Returns:
            pandas.Dataframe

        Exceptions :
            - requests.exceptions.ConnectionError
        """
        leaderboard_datatable = self.get_leaderboard_datatable()

        users_lst = leaderboard_datatable['users']
        languages_lst = leaderboard_datatable['language']

        total_solved_challenges = []
        total_solved_challenges_all_languages = []
        total_easy_solved = []
        total_med_solved = []
        total_hard_solved = []
        total_points = []

        start_timer = time.perf_counter()

        for user in users_lst:
            x = threading.Thread(target=self.fetch_user_data, args=(user,))
            self.threads_lst.append(x)
            x.start()
        for thread in self.threads_lst:
            thread.join()

        for index, user in enumerate(users_lst):
            easy_challenges_counter = 0
            med_challenges_counter = 0
            hard_challenges_counter = 0
            user_data = self.users_data[str(user)]
            if user_data != "private":
                total_solved_challenges_all_languages.append(user_data['total_solved_challenges'])

                for user_language in user_data['programming_languages']:
                    if user_language['name'] == "سهل":
                        easy_challenges_counter = easy_challenges_counter + user_language['solved_challenges']
                    elif user_language['name'] == "متوسط":
                        med_challenges_counter = med_challenges_counter + user_language['solved_challenges']
                    else:
                        hard_challenges_counter = hard_challenges_counter + user_language['solved_challenges']

                total_easy_solved.append(easy_challenges_counter)
                total_med_solved.append(med_challenges_counter)
                total_hard_solved.append(hard_challenges_counter)

                points = (easy_challenges_counter*5) + (med_challenges_counter*10) + (hard_challenges_counter*20)

                total_points.append(points)

                for user_languages in user_data['total_solved_per_programming_language']:
                    if user_languages['programming_language_name'].lower() == languages_lst[index].lower():
                        total_solved_challenges.append(user_languages['total_solved'])
                        break
                    else:
                        continue
            else:
                # this exception will happen if user is private
                total_easy_solved.append("private")
                total_med_solved.append("private")
                total_hard_solved.append("private")

                total_points.append("private")

                total_solved_challenges.append("private")
                total_solved_challenges_all_languages.append("private")
                continue

        end_timer = time.perf_counter()

        leaderboard_datatable.insert(4, "total_challenges_solved", total_solved_challenges)
        leaderboard_datatable.insert(5, "total_challenges_solved_all_languages", total_solved_challenges_all_languages)
        leaderboard_datatable.insert(6, "total_easy_solved", total_easy_solved)
        leaderboard_datatable.insert(7, "total_medium_solved", total_med_solved)
        leaderboard_datatable.insert(8, "total_hard_solved", total_hard_solved)
        leaderboard_datatable.insert(9, "total_points_all_challenges", total_points)

        print(f"total time : {end_timer - start_timer} seconds")
        return leaderboard_datatable
