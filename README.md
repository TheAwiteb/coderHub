<h1 align="center">
  <br>
  <a><img src="https://pbs.twimg.com/media/E43nR_kX0AMalxJ?format=jpg&name=small" alt="coderHub.sa - img"></a>
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
print(coder_hub.get_challenges(difficulty="easy"))
```
<details>
<summary> Example for first Result</summary>

```json
{
  "result":[
    {
    'id': '3e420f85-f4e9-4e7a-b6bc-f35a8db70cb4', 
    'title': 'طرح عددين', 
    'challenge_tags': [{'name': 'Math'}], 
    'points': 5, 
    'created_by': 
    {'username': 'CoderHub', 'public': False}, 
    'creator_role': 'admin', 
    'hint_text': None, 
    'hint_points': None, 
    'challenge_programming_languages': [], 
    'type_of_level': {'id': 2, 'name': 'سهل'}
    }
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
{'count': 2,
 'result': [{'challenge_programming_languages': [],
             'challenge_tags': [{'name': 'Date'}, {'name': 'String'}],
             'created_by': {'public': False, 'username': 'CoderHub'},
             'creator_role': 'admin',
             'hint_points': None,
             'hint_text': None,
             'id': 'c93a5e09-2578-42ec-95db-88d1e87d6459',
             'points': 10,
             'title': 'تاريخ اليوم',
             'type_of_level': {'id': 3, 'name': 'متوسط'}},
            {'challenge_programming_languages': [],
             'challenge_tags': [{'name': 'Date'}, {'name': 'String'}],
             'created_by': {'public': False, 'username': 'CoderHub'},
             'creator_role': 'admin',
             'hint_points': None,
             'hint_text': None,
             'id': 'a2df08ef-faa1-4aaf-bbd5-66f7e021855a',
             'points': 10,
             'title': 'تعديل صيغة التاريخ',
             'type_of_level': {'id': 3, 'name': 'متوسط'}}]}

```
</details>
<br><br>

**get challenge by id:**
```python
from coderHub import CoderHub

coder_hub = CoderHub()
print(coder_hub.get_challenge_by_id(id='3e420f85-f4e9-4e7a-b6bc-f35a8db70cb4'))
```
<details>
<summary> Example Result</summary>

```json
{
    'id': '3e420f85-f4e9-4e7a-b6bc-f35a8db70cb4', 
    'title': 'طرح عددين', 
    'description': '### وصف التحدي\r\nقم بكتابة `function` تستقبل عددين، العدد الأول يمثل رقماً صحيحاً `integer` والعدد الثاني يمثل أيضا رقماً صحيحاً `integer` ، ثم قم بإرجاع حاصل **طرح** هذين العددين.\r\n\r\n### المخرجات المتوقعة\r\n| Output  | b  | a |\r\n|----|----|----|\r\n| 5 | 5  | 10 |\r\n| 6 | -3  | 3 |\r\n| -5 | 1 | -4 |\r\n| 1 | -1 | 0 |\r\n| 0 | 0 | 0 |\r\n| -92 | -4 | -96 |', 
    'timed': True, 
    'time_limit': 5, 
    'points': 5
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
  'result': [
  {'id': 6, 'name': 'swift', 'version': 'swift 4.2.2'}, 
  {'id': 3, 'name': 'python', 'version': 'python 3.5.3'}, 
  {'id': 2, 'name': 'javascript', 'version': 'SMonkey 68.6.0'}, 
  {'id': 1, 'name': 'java', 'version': 'jdk 8u51'}, 
  {'id': 8, 'name': 'c#', 'version': 'Mono 4.0.2'}
  ]
}

// language by name
{
  'id': 3, 
  'name': 'python', 
  'version': 
  'python 3.5.3'
}
```

</details>
<br><br>

</details>
<br><br>

**get leaderboard:**
```python
from coderHub import CoderHub

coder_hub = CoderHub()

print(coder_hub.get_leaderBoard(language="Python", search_type="DAILY"))
```
<details>
<summary> Example Result</summary>

```json
{
  'leaderboard': 
  [
    {'points': 5, 'total_time': 12.155752, 'user_id': '8e0d0f0c-6884-4a9e-a28a-b9d6f3094407', 'rank': 1, 'user_info': {'username': 'ismm', 'public': False}
    }
  ]
}

```

</details>
<br><br>

**get user profile:**
```python
from coderHub import CoderHub

coder_hub = CoderHub()

print(coder_hub.get_profile(username="thamermashni"))
```
<details>
<summary> Example Result</summary>

```json
{'preferred_language': 'Python',
 'user_badges': [],
 'user_information': {'are_you_a_trainer': None,
                      'bio': 'Computer Science fresh graduate from King Fahad '
                             'University of Petroleum & Minerals',
                      'certificates': [{'expired': False,
                                        'expires_at': '2021-02-01T00:00:00+00:00',
                                        'institution': 'Udacity',
                                        'is_training_certificate': False,
                                        'name': 'Full-Stack Developer '
                                                'Nanodegree',
                                        'received_at': '2020-12-04T00:00:00+00:00'}],
                      'city': 'ابها',
                      'country_name': 'المملكة العربية السعودية',
                      'education': [{'end_at': '2020-02-17T00:00:00+00:00',
                                     'institution': 'جامعة الملك فهد للبترول '
                                                    'والمعادن',
                                     'major': 'Computer Science',
                                     'name': 'bachelor',
                                     'start_at': '2014-02-17T00:00:00+00:00'}],
                      'extra_public_fields': [],
                      'first_name': 'ثامر',
                      'id': 'fd0c7a26-e1de-40f8-af51-8be885a59e3b',
                      'is_looking_for_job': None,
                      'last_name': 'مشني',
                      'looking_for_job_type': None,
                      'occupation': None,
                      'preferred_language': None,
                      'programming_languages': [{'experience': 'أقل من سنة',
                                                 'programming_language': 'Java'},
                                                {'experience': 'أقل من سنة',
                                                 'programming_language': 'JavaScript'},
                                                {'experience': 'أقل من سنة',
                                                 'programming_language': 'Python'},
                                                {'experience': 'أقل من سنة',
                                                 'programming_language': 'SQL'},
                                                {'experience': 'أقل من سنة',
                                                 'programming_language': 'C#'}],
                      'public_profile': True,
                      'social_links': [{'handle': 'ThamerMashni',
                                        'site': 'GITHUB'},
                                       {'handle': 'thamermashni',
                                        'site': 'LINKEDIN'},
                                       {'handle': '', 'site': 'TWITTER'}],
                      'username': 'thamermashni'}}

```

</details>
<br><br>


**get user statistics:**
```python
from coderHub import CoderHub
coder_hub = CoderHub()

print(coder_hub.get_user_statistics(username='thamermashni'))
```
<details>
<summary> Example Result</summary>

```json
{'programming_languages': [{'name': 'سهل',
                            'programming_language_name': 'Python',
                            'solved_challenges': 58},
                           {'name': 'صعب',
                            'programming_language_name': 'Python',
                            'solved_challenges': 11},
                           {'name': 'متوسط',
                            'programming_language_name': 'Python',
                            'solved_challenges': 31},
                           {'name': 'متوسط',
                            'programming_language_name': 'JavaScript',
                            'solved_challenges': 1}],
 'total_solved_challenges': 101,
 'total_solved_per_programming_language': [{'programming_language_name': 'JavaScript',
                                            'total_solved': 1},
                                           {'programming_language_name': 'Python',
                                            'total_solved': 100}]}
```

</details>
<br><br>

## LICENSE
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)