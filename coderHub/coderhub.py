# -*- coding: utf-8 -*-
import requests
from typing import Optional, Union


class CoderHub:
    def __init__(self):
        self.host = "https://api.coderhub.sa/api"
        self.get_challenge_url = self.host + "/challenges/detail/{}"
        self.challenges_url = (
            self.host + "/challenges/filtered-list/?page_size=9999999999&query="
        )
        self.programming_languages_url = self.host + "/challenges/programming-languages"
        self.leaderBoard_url = (
            self.host + "/leaderboard/?language={0}&offset=0&limit=10&type={1}"
        )
        self.profile_url = self.host + "/profile/public/{}"
        self.user_statistics = self.host + "/profile/public/get-user-statistics/{}"

    def get_challenges(self, difficulty: Optional[Union[str, None]] = None) -> dict:
        """ارجاع جميع التحديات او عبر مستوى صعوبتها.

        المتغيرات:
            difficulty (str, None, optional): مستوى صعوبة التحديات. Defaults to None.

        الاخطاء:
            Exception: مستوى صعوبة خاطئ

        المخرجات:
            dict: قاموس يحتوي التحديات
        """
        # حلب جميع التحديات
        challenges = requests.get(self.challenges_url).json()
        # انشاء مصفوفة بمستوى صعوبة التحديات
        difficulty_list = set(
            map(
                lambda challenge: challenge["type_of_level"]["name"],
                challenges["result"],
            )
        )
        # اذا تم طلب مستوى صعوبة معين
        if difficulty:
            # اذا كان مستوى الصعوبة المطلوب في مصفوفة المستويات
            if difficulty in difficulty_list:
                # عمل فلتر للتحديات وجلب فقط الحديات التي لديها نفس مستوى الصعوبة
                result = list(
                    filter(
                        lambda challenge: challenge["type_of_level"]["name"]
                        == difficulty,
                        challenges["result"],
                    )
                )
                # ارجاع التحديات مع عددها
                return {"count": len(result), "result": result}
            else:
                # اظهار خطأ اذا كان مستوى الصعوبة غير موجود
                raise Exception(f"difficulty must be {' or '.join(difficulty_list)}")
        else:
            # ارجاع جميع التحديات مع عددها
            return challenges

    def search_challenges(self, word: str) -> dict:
        """البحث عن تحدي

        المتغيرات:
            word (str): الكلمة او النص الذي تريد البحث عنه

        الاخطاء:
            Exception: عدم وجود نتائج جول الكلمة التي تبحث عنها

        المخرجات:
            dict: قاموس يحتوي النتائج
        """
        data = requests.get(self.challenges_url + word).json()
        if data["count"]:
            return data
        else:
            raise Exception("There are no challenges available about '%s'" % word)

    def get_challenge_by_id(self, challenge_id: str) -> dict:
        """ارجاع محتوى التحدي عبر الايدي الخاص به

        المتغيرات:
            id (str): ايدي التحدي

        الاخطاء:
            Exception: ايدي تحدي خاطئ

        المخرجات:
            dict: محتوى التحدي
        """
        challenge_response = requests.get(self.get_challenge_url.format(challenge_id))
        if challenge_response.ok:
            return challenge_response.json()
        else:
            raise Exception("Invalid challenge id: %s not found" % challenge_id)

    def get_languages(self, language: Optional[Union[str, None]] = None) -> dict:
        """ارجاع جميع لغات البرمجة التي يدعمها الموقع او لغة محددة

        المتغيرات:
            language (str, None, optional): اللغة التي تريدها. Defaults to None.

        الاخطاء:
            Exception: اللغة غير موجودة

        المخرجات:
            dict: اللغة او اللغات
        """
        languages = list(
            map(
                lambda lang: {
                    "id": lang["id"],
                    "name": lang["name"].lower(),
                    "version": lang["version"],
                },
                requests.get(self.programming_languages_url).json(),
            )
        )
        if language:
            languages = list(
                filter(lambda lang: lang["name"] == language.lower(), languages)
            )
            if languages:
                return languages[0]
            else:
                raise Exception(f"Invalid language, '{language}' not found")
        else:
            return {"result": languages}

    def get_leaderBoard(
        self, language: str, search_type: Optional[Union[str]] = "ALL"
    ) -> dict:
        """ارجاع اول 10 في لوحة المتصدرين
            نوع البحث يجب ان يكون من هاذه المصفوفة [ALL, DAILY, WEEKLY]

        المتغيرات:
            language (str): لغة البرمجة التي تريد منها المتصدرين
            search_type (Optional[Union[str]], optional): نوع البحث. Defaults to "ALL".

        الاخطاء:
            Exception: Unknown language, لغة برمجة غير موجودة
            Exception: invalid search type, نوع البحث غير موجود

        المخرجات:
            dict: قاموس يحتوي المتصدرين
        """
        language, search_type = language.lower(), search_type.upper()
        types = ["ALL", "DAILY", "WEEKLY"]
        languages = self.get_languages()
        languages_names = list(map(lambda lang: lang["name"], languages["result"]))
        languages_ids = list(map(lambda lang: lang["id"], languages["result"]))
        if language in languages_names:
            if search_type in types:
                id = languages_ids[languages_names.index(language)]
                leaderboard = requests.get(
                    self.leaderBoard_url.format(id, search_type)
                ).json()["leaderboard"]
                return {"leaderboard": leaderboard}
            else:
                raise Exception(
                    "Invalid search type, '%s' not found, search_type should be  %s"
                    % (search_type, " or ".join(types))
                )
        else:
            raise Exception(
                "Unknown language, '%s' not found, language should be  %s"
                % (language, " or ".join(languages_names))
            )

    def get_profile(self, username: str) -> dict:
        """ارجاع الملف التعريفي الخاص باسم المستخدم

        المتغيرات:
            username (str): اسم المستخدم الذي تريد الملف التعريفي الخاص به

        الاخطاء:
            Exception: ['user profile is not public', 'user profile is not found']

        المخرجات:
            dict: قاموس يحتوي الملف التعريفي
        """
        data = requests.get(self.profile_url.format(username.lower())).json()
        if "detail" in data.keys():
            raise Exception(data["detail"])
        else:
            return data

    def get_user_statistics(self, username: str) -> dict:
        """ارجاع إحصائيات المستخدم

        المتغيرات:
            username (str): اسم المستخدم الذي تريد إحصائياته

        المخرجات:
            dict: قاموس يحتوي إحصائيات المستخدم
        """
        user_id = self.get_profile(username=username)["user_information"]["id"]
        data = requests.get(self.user_statistics.format(user_id)).json()
        return data
