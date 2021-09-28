<h1 align="center">
  <br>
  <a><img src="https://user-images.githubusercontent.com/59842932/128586067-615bcc79-078d-4748-b421-c385cd84cd37.png" alt="coderHub.sa - img"></a>
  <br>
  coderHub
  <br>
</h1>


<p align="center">A python library built on the API of the <a href=https://coderhub.sa>coderHub.sa</a>, which helps you to fetch the challenges, get stats and more
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
  <a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
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
<summary> Example Result</summary>

```json
{"count": 99, "result": [{...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, ...]}
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

**get the count of all challenges available(easy, medium and hard):**
```python
from coderHub import CoderHubStats
coderhub_stats = CoderHubStats()

print(coderhub_stats.get_challenges_summary_stats()) # return a DataFrame
```
<details>
<summary> Example Result</summary>

```bash
all_challenges                98.00
easy_challenges               56.00
medium_challenges             31.00
hard_challenges               11.00
easy_challenges_percentage    57.14
medium_challenges_percentage  31.63
hard_challenges_percentage    11.22

```

</details>
<br><br>


**get all programming languages names available:**
```python
from coderHub import CoderHubStats
coderhub_stats = CoderHubStats()

print(coderhub_stats.get_languages_names()) # return a list
```
<details>
<summary> Example Result</summary>

```bash
['swift', 'python', 'javascript', 'java', 'c#', 'kotlin']
```

</details>
<br><br>

**get top 10 users and thier points in the leaderboard for every programming language:**
```python
from coderHub import CoderHubStats
coderhub_stats = CoderHubStats()

print(coderhub_stats.get_leaderboard_datatable()) # return a DataFrame
```
<details>
<summary> Example Result</summary>

```bash
                users  points  rank    language
0           ahmed0ksa   921.0     1       swift
1             alxd7my   911.0     2       swift
2               iX901   906.0     3       swift
3           ahmadajr1   906.0     4       swift
4              vdotup   906.0     5       swift
5      LulwahAlmisfer   906.0     6       swift
6          iam.that.1   901.0     7       swift
7              fayadh   891.0     8       swift
8           eengmaher   826.0     9       swift
9           f.babkoor   820.0    10       swift
10          TheAwiteb   926.0     1      python
11           hamoud47   926.0     2      python
12           dssaggaf   921.0     3      python
13     fahad.alharthi   916.0     4      python
14             maldum   916.0     5      python
15       snap-aaa.saq   911.0     6      python
16          thenajjar   906.0     7      python
17             nnoaid   906.0     8      python
18             asma94   906.0     9      python
19           saud1983   906.0    10      python
20        shuruqsaeed   931.0     1  javascript
21  Ibrahim_Alrubayyi   931.0     2  javascript
22               x7md   931.0     3  javascript
23           ghadyana   926.0     4  javascript
24              masha   921.0     5  javascript
25          qabdull4h   916.0     6  javascript
26     salehalibrahim   911.0     7  javascript
27            aisha_j   911.0     8  javascript
28                lum   911.0     9  javascript
29     abdulrahmansbq   906.0    10  javascript
30          sircaesar   916.0     1        java
31         musaadtech   916.0     2        java
32         abdullahmq   911.0     3        java
33       haider_dev94   911.0     4        java
34           alsenani   911.0     5        java
35            alharbi   911.0     6        java
36          jstsercuz   911.0     7        java
37               arwa   911.0     8        java
38      bandaralrooqi   911.0     9        java
39             asma94   906.0    10        java
40             salman    91.0     1          c#
41        shuruqsaeed    91.0     2          c#
42            amjad.a    91.0     3          c#
43          ib.subaie    91.0     4          c#
44             golag7    91.0     5          c#
45           reham721    91.0     6          c#
46     abdulrahmansbq    91.0     7          c#
47          TheAwiteb    91.0     8          c#
48             asma94    91.0     9          c#
49           dssaggaf    91.0    10          c#
50             salman    91.0     1      kotlin
51     abdulrahmansbq    91.0     2      kotlin
52             golag7    91.0     3      kotlin
53           reham721    91.0     4      kotlin
54        ahmadshahal    91.0     5      kotlin
55            amjad.a    91.0     6      kotlin
56              amira    91.0     7      kotlin
57            sal7one    91.0     8      kotlin
58       haider_dev94    91.0     9      kotlin
59          TheAwiteb    91.0    10      kotlin

```

</details>
<br><br>

**get top 10 users, thier points and thier total solved challenges in the leaderboard for every programming language :**
```python
from coderHub import CoderHubStats
coderhub_stats = CoderHubStats()

print(coderhub_stats.get_top_users_stats()) # return a DataFrame
```
<details>
<summary> Example Result</summary>

```bash
                users  points  rank    language total_challenges_solved
0           ahmed0ksa   921.0     1       swift                     107
1             alxd7my   911.0     2       swift                     106
2               iX901   906.0     3       swift                     105
3           ahmadajr1   906.0     4       swift                     105
4              vdotup   906.0     5       swift                     105
5      LulwahAlmisfer   906.0     6       swift                     105
6          iam.that.1   901.0     7       swift                     105
7              fayadh   891.0     8       swift                     103
8           eengmaher   826.0     9       swift                     100
9           f.babkoor   820.0    10       swift                     100
10          TheAwiteb   926.0     1      python                     108
11           hamoud47   926.0     2      python                     108
12           dssaggaf   921.0     3      python                     107
13     fahad.alharthi   916.0     4      python                     107
14             maldum   916.0     5      python                     107
15       snap-aaa.saq   911.0     6      python                     106
16          thenajjar   906.0     7      python                     105
17             nnoaid   906.0     8      python                 private
18             asma94   906.0     9      python                     105
19           saud1983   906.0    10      python                 private
20        shuruqsaeed   931.0     1  javascript                     109
21  Ibrahim_Alrubayyi   931.0     2  javascript                     109
22               x7md   931.0     3  javascript                     109
23           ghadyana   926.0     4  javascript                     108
24              masha   921.0     5  javascript                     108
25          qabdull4h   916.0     6  javascript                     106
26     salehalibrahim   911.0     7  javascript                 private
27            aisha_j   911.0     8  javascript                     106
28                lum   911.0     9  javascript                 private
29     abdulrahmansbq   906.0    10  javascript                     105
30          sircaesar   916.0     1        java                     107
31         musaadtech   916.0     2        java                     107
32         abdullahmq   911.0     3        java                     106
33       haider_dev94   911.0     4        java                     106
34           alsenani   911.0     5        java                     106
35            alharbi   911.0     6        java                     106
36          jstsercuz   911.0     7        java                     106
37               arwa   911.0     8        java                     106
38      bandaralrooqi   911.0     9        java                     106
39             asma94   906.0    10        java                     105
40             salman    91.0     1          c#                       6
41        shuruqsaeed    91.0     2          c#                       6
42            amjad.a    91.0     3          c#                       6
43          ib.subaie    91.0     4          c#                 private
44             golag7    91.0     5          c#                 private
45           reham721    91.0     6          c#                 private
46     abdulrahmansbq    91.0     7          c#                       6
47          TheAwiteb    91.0     8          c#                       6
48             asma94    91.0     9          c#                       6
49           dssaggaf    91.0    10          c#                       6
50             salman    91.0     1      kotlin                       6
51     abdulrahmansbq    91.0     2      kotlin                       6
52             golag7    91.0     3      kotlin                 private
53           reham721    91.0     4      kotlin                 private
54        ahmadshahal    91.0     5      kotlin                 private
55            amjad.a    91.0     6      kotlin                       6
56              amira    91.0     7      kotlin                 private
57            sal7one    91.0     8      kotlin                       6
58       haider_dev94    91.0     9      kotlin                       6
59          TheAwiteb    91.0    10      kotlin                       6

```

</details>
<br><br>


## LICENSE
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)
