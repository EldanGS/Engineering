import requests
import json
from collections import defaultdict

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da' \
               '72454d235c274f1a2be5f45ee711'

V = '5.71'


def get_user_id(uid: str) -> int:
    """Function return user id by username and user_id"""
    payload = {'v': V,
               'access_token': ACCESS_TOKEN,
               'user_ids': uid}
    response = requests.get('https://api.vk.com/method/users.get',
                            params=payload)
    try:
        response_json = response.json()
        print(response_json)
        response = response_json['response']
        user = response[0]
        return user['id']
    except (json.JSONDecodeError, IndexError, KeyError):
        raise


def get_friends(user_id: int) -> list:
    """Function return list of friends"""
    payload = {'v': V,
               'access_token': ACCESS_TOKEN,
               'user_id': user_id,
               'fields': 'bdate'}
    response = requests.get('https://api.vk.com/method/friends.get',
                            params=payload)

    try:
        response_json = response.json()
        response = response_json['response']
        friends = response['items']
        return friends
    except (json.JSONDecodeError, IndexError, KeyError):
        raise


def calc_age(uid: str):
    user_id = get_user_id(uid)
    if not user_id:
        return

    friends = get_friends(user_id)
    if not friends:
        return

    years = defaultdict(int)
    for friend in friends:
        bdate = friend.get('bdate', None)
        if not bdate:
            continue

        bdate = bdate.split('.')  # "25.8.1993"
        if len(bdate) != 3:
            continue

        day, month, year = map(int, bdate)
        diff = 2019 - year
        years[diff] += 1

    return sorted(years.items(), key=lambda x: (x[1], -x[0]), reverse=True)


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
