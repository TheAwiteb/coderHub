<h1 align="center">
  <br>
  <a><img src="./img/coderHub.sa.png" alt="quran_suras - img"></a>
  <br>
  coderHub
  <br>
</h1>


<p align="center">A python method based on the API of the <a href=https://coderhub.sa>coderHub.sa</a>, which helps you to fetch the challenges and more
<p align="center">
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

Use [GitHub](https://github.com) to install coderHub.

```bash
git clone https://github.com/Awiteb/coderHub
```

## Features

* get all challenges or by difficulty
* get challenge by id

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

**get challenge by id:**
```python
from coderHub import CoderHub

coder_hub = CoderHub()
print(coder_hub.get_challenge_by_id('3e420f85-f4e9-4e7a-b6bc-f35a8db70cb4'))
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


## LICENSE
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)