<h1 align="center">
  <br>
  <a><img src="https://user-images.githubusercontent.com/59842932/128586067-615bcc79-078d-4748-b421-c385cd84cd37.png" alt="coderHub.sa - img"></a>
  <br>
  coderHub
  <br>
</h1>


<p align="center">A python method based on the API of the <a href=https://coderhub.sa>coderHub.sa</a>, which helps you to fetch the challenges and more
<p align="center">
  <a href="https://pypi.org/project/coderHub/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/coderHub?color=9cf">
  </a>
  <a href="https://pypi.org/project/coderHub/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/coderHub?color=9cf">
  </a>
  <a href="https://www.gnu.org/licenses/gpl-3.0.html">
    <img src="https://img.shields.io/pypi/l/quran-suras?color=9cf&label=License" alt="License">
  </a>
</p>


<p align="center">
  <a href="#installation">Installation</a>
  •
  <a href="#features">Features</a>
  •
  <a href="#usage">Usage</a>
  •
  <a href="#license">License</a>
</p>

> This project is a personal effort and CoderHub has nothing to do with the content of this project.

## Installation

Use [pypi](https://pypi.org) to install coderHub.

```bash
pip3 install coderHub
```

## Features

* get all challenges or by difficulty
* search for challenges
* get challenge by id
* get all languages info or by language name
* get top 10 leaderboard by programming language
* get user profile info
* get user statistics info

## Usage

**get all challenges or by difficulty:**
```python
from coderHub import CoderHub

coder_hub = CoderHub()
# get all challenges
print(coder_hub.get_challenges())

#get by difficulty
print(coder_hub.get_challenges(difficulty="سهل"))
```
<details>
<summary> Example for first Result</summary>

```json
{
    "result": [
        {
            "challenge_tags": [{"name": "Math"}],
            "created_by": {"username": "CoderHub"},
            "id": "3e420f85-f4e9-4e7a-b6bc-f35a8db70cb4",
            "points": 5,
            "title": "طرح عددين",
            "type_of_level": {"name": "سهل"}
        }
    ]
}
```
</details>
<br><br>

**search for challenges:**
```python
from coderHub import CoderHub
coder_hub = CoderHub()

print(coder_hub.search_challenges(word="تاريخ"))
```
<details>
<summary> Example Result</summary>

```json
{
    "count": 2,
    "result":
        [
            {
                "challenge_tags": [{"name": "Date"}, {"name": "String"}],
                "created_by": {"username": "CoderHub"},
                "id": "c93a5e09-2578-42ec-95db-88d1e87d6459",
                "points": 10,
                "title": "تاريخ اليوم",
                "type_of_level": {"name": "متوسط"}
                },
            {
                "challenge_tags": [{"name": "Date"}, {"name": "String"}],
                "created_by": {"username": "CoderHub"},
                "id": "a2df08ef-faa1-4aaf-bbd5-66f7e021855a",
                "points": 10,
                "title": "تعديل صيغة التاريخ",
                "type_of_level": {"name": "متوسط"}
                }
            ]
}

```
</details>
<br><br>

**get challenge by id:**
```python
from coderHub import CoderHub

coder_hub = CoderHub()
print(coder_hub.get_challenge_by_id(challenge_id="3e420f85-f4e9-4e7a-b6bc-f35a8db70cb4"))
```
<details>
<summary> Example Result</summary>

```json
{
    "id": "3e420f85-f4e9-4e7a-b6bc-f35a8db70cb4", 
    "title": "طرح عددين", 
    "description": "### وصف التحدي\r\nقم بكتابة `function` تستقبل عددين، العدد الأول يمثل رقماً صحيحاً `integer` والعدد الثاني يمثل أيضا رقماً صحيحاً `integer`, ثم قم بإرجاع حاصل **طرح** هذين العددين.\r\n\r\n### المخرجات المتوقعة\r\n| Output  | b  | a |\r\n|----|----|----|\r\n| 5 | 5  | 10 |\r\n| 6 | -3  | 3 |\r\n| -5 | 1 | -4 |\r\n| 1 | -1 | 0 |\r\n| 0 | 0 | 0 |\r\n| -92 | -4 | -96 |", 
    "points": 5
    // and more ...
}
```

</details>
<br><br>

**get languages:**
```python
from coderHub import CoderHub

coder_hub = CoderHub()

# all languages
print(coder_hub.get_languages())

# language by name
print(coder_hub.get_languages(language="python"))
```
<details>
<summary> Example Result</summary>

```json
// all languages
{
    "result": [
        {"id": 6, "name": "swift", "version": "swift 4.2.2"},
        {"id": 3, "name": "python", "version": "python 3.5.3"},
        {"id": 2, "name": "javascript", "version": "SMonkey 68.6.0"}, 
        {"id": 1, "name": "java", "version": "jdk 8u51"}, 
        {"id": 8, "name": "c#", "version": "Mono 4.0.2"}
    ]
}
```
```json
// language by name

{"id": 3, "name": "python", "version": "python 3.5.3"}
```

</details>
<br><br>

</details>
<br><br>

**get leaderboard:**
```python
from coderHub import CoderHub

coder_hub = CoderHub()

print(coder_hub.get_leaderBoard(language="Python", search_type="ALL"))
```
<details>
<summary> Example Result</summary>

```json
{
    "leaderboard": [
        {
            "points": 835.0,
            "user_id": "b45cf6da-c2aa-4347-a3da-fbf951a4183b",
            "rank": 1, 
            "user_info": {"username": "hamoud47", "public": true}
        }, 
        {
            "points": 830.0, 
            "user_id": "5eb4d6ea-1f0e-4cb9-b365-44518ddf5667",
            "rank": 2,
            "user_info": {"username": "awiteb", "public": false}
        }
    // 8 more
    ]
}

```

</details>
<br><br>

**get user profile:**
```python
from coderHub import CoderHub

coder_hub = CoderHub()

print(coder_hub.get_profile(username="x7md"))
```
<details>
<summary> Example Result</summary>

```json
{
    "preferred_language": "JavaScript", 
    "user_information": {
        "id": "eab8c73c-9ae2-4595-a321-3de9faa72721", 
        "public_profile": true, 
        "first_name": "حمد", 
        "last_name": "بنقالي", 
        "username": "x7md", 
        "bio": "شاب سعودي، مهتم بالبرمجة، والتصميم الرقمي.", 
        "country_name": "المملكة العربية السعودية", 
        "city": "مكة المكرمة", 
        "social_links": [
            {"site": "GITHUB", "handle": "x7md"},
            {"site": "TWITTER", "handle": "anb9"}
            ],
        "education": [
            {
                "name": "highSchool", 
                "major": "", 
                "institution": "عكرمة بن عمرو", 
                "start_at": "2019-03-31T00:00:00+00:00", 
                "end_at": "2021-03-31T00:00:00+00:00"
                }
            ],
        "certificates": [
            {
                "name": "التوعية بمخاطر الأمن السيبراني", 
                "institution": "دروب - صندوق تنمية الموارد البشرية", 
                "received_at": "2020-04-23T00:00:00+00:00", 
                "expires_at": "2020-04-23T00:00:00+00:00", 
                "expired": false, 
                "is_training_certificate": false
                }
            ], 
        "programming_languages": [
            {"programming_language": "JavaScript", "experience": "1 - 2 سنوات"}, 
            {"programming_language": "Shell", "experience": "أقل من سنة"}, 
            {"programming_language": "SQL", "experience": "أقل من سنة"}
                ],
        "extra_public_fields": [
            "are_you_a_trainer", "looking_for_job_type", "occupation"
                ], 
        "is_looking_for_job": null, 
        "looking_for_job_type": "training", 
        "are_you_a_trainer": false,
        "occupation": "college student",
        "preferred_language": "JavaScript"
            },
    "user_badges": []
}
```

</details>
<br><br>


**get user statistics:**
```python
from coderHub import CoderHub
coder_hub = CoderHub()

print(coder_hub.get_user_statistics(username="x7md"))
```
<details>
<summary> Example Result</summary>

```json
{
    "programming_languages": [
        {"programming_language_name": "JavaScript", "name": "سهل", "solved_challenges": 59}, 
        {"programming_language_name": "JavaScript", "name": "صعب", "solved_challenges": 11}, 
        {"programming_language_name": "JavaScript", "name": "متوسط", "solved_challenges": 32}, 
        {"programming_language_name": "Java", "name": "سهل", "solved_challenges": 12}
            ], 
    "total_solved_per_programming_language": [
        {"programming_language_name": "Java", "total_solved": 12}, 
        {"programming_language_name": "JavaScript", "total_solved": 102}
            ], 
    "total_solved_challenges": 114
}
```

</details>
<br><br>

## LICENSE
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)
