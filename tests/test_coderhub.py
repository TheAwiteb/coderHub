from coderHub import CoderHub
from random import choice
from string import ascii_lowercase

coderhub = CoderHub()
RANDOM_TEXT = "".join(choice(ascii_lowercase) for i in range(16))


def try_catch(func, *args):
    """Returns True if there is an error

    Args:
        func (function): The function you want to test should return an error
    """
    try:
        func(*args)
    except Exception:
        assert True
    else:
        assert False


def test_get_challenges():
    challenge = coderhub.get_challenges(difficulty=None)
    assert challenge
    assert coderhub.get_challenges(difficulty="سهل")
    assert coderhub.get_challenges(difficulty="متوسط")
    assert coderhub.get_challenges(difficulty="صعب")
    try_catch(coderhub.get_challenges, RANDOM_TEXT)
    return challenge["result"][0]["id"]


def test_search_challenges():
    assert coderhub.search_challenges(word="ترتيب")
    try_catch(coderhub.search_challenges, RANDOM_TEXT)
    try_catch(coderhub.search_challenges)


def test_get_challenge_by_id():
    challenge_id = test_get_challenges()
    assert coderhub.get_challenge_by_id(challenge_id=challenge_id)
    try_catch(coderhub.get_challenge_by_id, RANDOM_TEXT)


def test_get_languages():
    assert coderhub.get_languages(language=None)
    assert coderhub.get_languages(language="python")
    assert coderhub.get_languages(language="PyThOn")
    assert coderhub.get_languages(language="java")
    assert coderhub.get_languages(language="swift")
    try_catch(coderhub.get_languages, RANDOM_TEXT)


def test_get_leaderBoard():
    assert coderhub.get_leaderBoard(language="Python", search_type="ALL")
    assert coderhub.get_leaderBoard(language="Python", search_type="WEEKLY")
    assert coderhub.get_leaderBoard(language="Python", search_type="DAILY")
    assert coderhub.get_leaderBoard(language="Python", page=2)
    assert coderhub.get_leaderBoard(language="Python", page=999_999_999)
    try_catch(coderhub.get_leaderBoard, RANDOM_TEXT, "ALL")
    try_catch(coderhub.get_leaderBoard, "Python", RANDOM_TEXT)


def test_get_profile():
    assert coderhub.get_profile(username="x7md")
    assert coderhub.get_profile(username="masha")
    try_catch(coderhub.get_profile, "Awiteb")
    try_catch(coderhub.get_profile, RANDOM_TEXT)


def test_get_user_statistics():
    assert coderhub.get_user_statistics(username="x7md")
    try_catch(coderhub.get_user_statistics, "Awiteb")
    try_catch(coderhub.get_user_statistics, RANDOM_TEXT)
