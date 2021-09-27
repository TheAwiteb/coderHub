# -*- coding: utf-8 -*-
import requests
from typing import Optional, Union

EMPTY = ""


class CoderHub:
    def __init__(self):
        # الـ API
        self.host = "https://api.coderhub.sa/api"

        # جلب تحدي يتم وضع ايدي التحدي
        self.get_challenge_url = self.host + "/challenges/detail/{challenge_id}"

        # جلب جميع التحديات او عبر البحث (يتم وضع المراد البحث عنه في word)
        self.challenges_url = (
            self.host + "/challenges/filtered-list/?page_size=9999999999&query={word}"
        )

        # جلب جميع لغات البرمجة
        self.programming_languages_url = self.host + "/challenges/programming-languages"

        # جلب لوحة المتصدرين تستقبل ايدي اللغة ورقم الصفحة حقت المتصدرين ونوع البحث
        # البحث يكون ["ALL", "DAILY", "WEEKLY"]
        self.leaderBoard_url = (
            self.host
            + "/leaderboard/?language={lang_id}&offset={page}&limit=10&type={search_type}"
        )

        # جلب الملف التعريفي الخاص باسم المستخدم
        self.profile_url = self.host + "/profile/public/{username}"

        # جلب احصائيات المستخدم (تستقبل ايدي المستخدم)
        self.user_statistics = (
            self.host + "/profile/public/get-user-statistics/{user_id}"
        )

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
        challenges = requests.get(self.challenges_url.format(word=EMPTY)).json()
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
        # جلب التحديات التي تحتوي على الكلمة او النص الذي تبحث عنه
        data = requests.get(self.challenges_url.format(word=word)).json()
        # اذ لم يكن العدد يساوي صفر
        if data.get("count"):
            # ارجاع التحديات
            return data
        else:
            # ارجاع خطاء بعدم وجود تحديات متطابقة
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
        # حلب التحدي عبر الايدي الخاص به
        challenge_response = requests.get(
            self.get_challenge_url.format(challenge_id=challenge_id)
        )
        # اذا كان الرسبونس صحيح
        if challenge_response.ok:
            # ارحاع محتوى التحدي
            return challenge_response.json()
        else:
            # ارجاع خطاء الايدي غير صحيح
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
        # جلب جميع لغات البرمجة التي بالموقع
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
        # اذا تم طلب لغة معينة
        if language:
            # عمل فلتر باسم اللغة المطلوبة
            languages = list(
                filter(lambda lang: lang["name"] == language.lower(), languages)
            )
            # اذا لم تكن المصفوفة فارغة
            if languages:
                return languages[0]
            else:
                # ارجاع خطاء اللغة المطلوبة غير موجودة
                raise Exception(f"Invalid language, '{language}' not found")
        else:  # اذ لم يتم طلب لغة يتم ارجاع حميع اللغات
            return {"result": languages}

    def get_leaderBoard(
        self,
        language: str,
        search_type: Optional[Union[str]] = "ALL",
        page: Optional[Union[int]] = 0,
    ) -> dict:
        """ارجاع 10 متصدرين من كل صفحة
            نوع البحث يجب ان يكون من هاذه المصفوفة [ALL, DAILY, WEEKLY]

        المتغيرات:
            language (str): لغة البرمجة التي تريد منها المتصدرين
            search_type (Optional[Union[str]], optional): نوع البحث. Defaults to "ALL".
            page (Optional[Union[int]], optional): رقم الصفحة التي تريد جلب المتصدرين منها. Defaults to 0.

        الاخطاء:
            Exception: Unknown language, لغة برمجة غير موجودة
            Exception: invalid search type, نوع البحث غير موجود

        المخرجات:
            dict: قاموس يحتوي المتصدرين
        """
        # جعل اسم اللغة بحروف صغير وجعل نوع البحث بحروف كبيرة
        language, search_type = language.lower(), search_type.upper()
        # تعريف مصفوفة تحتوي انواع البحث
        types = ["ALL", "DAILY", "WEEKLY"]
        # جلب اللغات الموجودة بالموقع
        languages = self.get_languages()
        # استخراج اسم كل لغة
        languages_names = list(map(lambda lang: lang["name"], languages["result"]))
        # استخراج ايدي كل لغة
        languages_ids = list(map(lambda lang: lang["id"], languages["result"]))
        # اذا كانت اللغة موجودة في لغات الموقع
        if language in languages_names:
            # اذا كان نوع البحث المطلوب بين الانواع الموجودة
            if search_type in types:
                # جلب ايدي اللغة المطلوبة
                id = languages_ids[languages_names.index(language)]
                # جلب قائمة المتصدرين
                leaderboard = requests.get(
                    self.leaderBoard_url.format(
                        lang_id=id, page=page, search_type=search_type
                    )
                ).json()["leaderboard"]
                return {"leaderboard": leaderboard}
            else:
                # ارجاع خطاء بعدم وجود هذا النوع
                raise Exception(
                    "Invalid search type, '%s' not found, search_type should be  %s"
                    % (search_type, " or ".join(types))
                )
        else:
            # ارجاع خطاء بعدم وجود اللغة
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
        # جلب البروفايل باسم المستخدم المعطى
        data = requests.get(self.profile_url.format(username=username.lower())).json()
        # اذا كان هناك وصف للخطاء
        if "detail" in data.keys():
            # ارجاع الوصف
            raise Exception(data["detail"])
        else:
            # اذ لم يوجد خطاء يتم ارجاع البروفايل
            return data

    def get_user_statistics(self, username: str) -> dict:
        """ارجاع إحصائيات المستخدم

        المتغيرات:
            username (str): اسم المستخدم الذي تريد إحصائياته

        المخرجات:
            dict: قاموس يحتوي إحصائيات المستخدم
        """
        # لم يتم التاكد من اسم المستخدم لان يتم التحقق في دالة جلب البروفايل
        # جلب ايدي المستخدم
        user_id = self.get_profile(username=username)["user_information"]["id"]
        # جلب احصائيات المستخدم عبر الايدي الخاص به
        data = requests.get(self.user_statistics.format(user_id=user_id)).json()
        # ارجاع البروفايل
        return data
