import pandas as pd
import time
import statistics as st
from coderhub import CoderHub


class CoderHubEDA(CoderHub):
    # challenges difficulties are easy, medium and/or hard

    # this function will return a DataFrame containing
    # all challenges count(easy, medium, hard and all) and its percentages
    def get_challenges_summary_stats(self):
        load_data = CoderHub.get_challenges(self)
        df = pd.json_normalize(load_data['result'])

        all_chall_count = len(df)
        easy_chall_count = len(df[df["type_of_level.name"] == "سهل"])
        mid_chall_count = len(df[df["type_of_level.name"] == "متوسط"])
        hard_chall_count = len(df[df["type_of_level.name"] == "صعب"])

        easy_chall_perc = (easy_chall_count/all_chall_count)*100
        mid_chall_perc = (mid_chall_count/all_chall_count)*100
        hard_chall_perc = (hard_chall_count/all_chall_count)*100

        # rounding numbers
        easy_chall_perc = round(easy_chall_perc, 2)
        mid_chall_perc = round(mid_chall_perc, 2)
        hard_chall_perc = round(hard_chall_perc, 2)

        challenges_summary_stats = {
            'all_challenges': all_chall_count,
            'easy_challenges': easy_chall_count,
            'medium_challenges': mid_chall_count,
            'hard_challenges': hard_chall_count,
            'easy_challenges_percentage': easy_chall_perc,
            'medium_challenges_percentage': mid_chall_perc,
            'hard_challenges_percentage': hard_chall_perc
        }
        return pd.DataFrame().from_dict(challenges_summary_stats, orient='index')

    def get_languages_names(self):
        load_data = CoderHub.get_languages(self)
        languages = [i['name'] for i in load_data['result']]
        return languages

    # this function will return a DataFrame with all
    # languages leaderboard data
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

    # return top users on leaderboard per language, if user profile is private
     # it will
    def get_top_users_stats(self):
        # top 10 for every language
        leaderboard_datatable = self.get_leaderboard_datatable()
        users_lst = leaderboard_datatable['users']
        langs_lst = leaderboard_datatable['language']
        total_solved = []
        start_timer = time.perf_counter()
        for index, user in enumerate(users_lst):
            try:
                for user_langs in self.get_user_statistics(user)['total_solved_per_programming_language']:
                    if user_langs['programming_language_name'].lower() == langs_lst[index].lower():
                        total_solved.append(user_langs['total_solved'])
                        break
                    else:
                        continue
            except Exception as e:
                # user is private
                total_solved.append("private")
                continue
        end_timer = time.perf_counter()
        leaderboard_datatable.insert(4, "total_challenges_solved", total_solved)
        print(f"total time : {end_timer - start_timer} seconds")
        print(leaderboard_datatable)


eda = CoderHubEDA()
print(eda.get_challenges_summary_stats())
print("------------------")
print(eda.get_leaderboard_datatable())
print(eda.get_top_users_stats())


