
# todo :
# - fix the function get_top_users_stats() time complexity
# - better function names
# - add progress bar for functions that takes extra time


import pandas as pd
import time
import statistics as st
from coderhub import CoderHub


class CoderHubStats(CoderHub):
    # this function will return a pandas.DataFrame containing
    # all challenges count(easy, medium and hard) and its percentages
    def get_challenges_summary_stats(self):
        load_data = CoderHub.get_challenges(self)
        df = pd.json_normalize(load_data['result'])

        all_challenges_count = len(df)
        easy_challenges_count = len(df[df["type_of_level.name"] == "سهل"])
        med_challenges_count = len(df[df["type_of_level.name"] == "متوسط"])
        hard_challenges_count = len(df[df["type_of_level.name"] == "صعب"])

        easy_challenges_percentage = (easy_challenges_count/all_challenges_count)*100
        med_challenges_percentage = (med_challenges_count/all_challenges_count)*100
        hard_challenges_percentage = (hard_challenges_count/all_challenges_count)*100

        # rounding numbers
        easy_challenges_percentage = round(easy_challenges_percentage, 2)
        med_challenges_percentage = round(med_challenges_percentage, 2)
        hard_challenges_percentage = round(hard_challenges_percentage, 2)

        challenges_summary_stats = {
            'all_challenges': all_challenges_count,
            'easy_challenges': easy_challenges_count,
            'medium_challenges': med_challenges_count,
            'hard_challenges': hard_challenges_count,
            'easy_challenges_percentage': easy_challenges_percentage,
            'medium_challenges_percentage': med_challenges_percentage,
            'hard_challenges_percentage': hard_challenges_percentage
        }
        return pd.DataFrame().from_dict(challenges_summary_stats, orient='index')

    # return all programing languages names available in coderhub.sa
    def get_languages_names(self):
        load_data = CoderHub.get_languages(self)
        languages = [i['name'] for i in load_data['result']]
        return languages

    # this function will return a DataFrame containing top 10 users and their points
    def get_leaderboard_datatable(self):
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

    # based on get_leaderboard_datatable() this function will get solved challenges count for every
    # user and append it to the given DataFrame and return it
    def get_top_users_stats(self):
        leaderboard_datatable = self.get_leaderboard_datatable()

        users_lst = leaderboard_datatable['users']
        languages_lst = leaderboard_datatable['language']

        total_solved_challenges = []  # total solved challenges for every user in top 10 leaderboard

        start_timer = time.perf_counter()

        for index, user in enumerate(users_lst):
            try:
                for user_languages in self.get_user_statistics(user)['total_solved_per_programming_language']:
                    if user_languages['programming_language_name'].lower() == languages_lst[index].lower():
                        total_solved_challenges.append(user_languages['total_solved'])
                        break
                    else:
                        continue
            except Exception as e:
                # this exception will happen if user is private
                total_solved_challenges.append("private")
                continue

        end_timer = time.perf_counter()

        leaderboard_datatable.insert(4, "total_challenges_solved", total_solved_challenges)

        print(f"total time : {end_timer - start_timer} seconds")

        return leaderboard_datatable

