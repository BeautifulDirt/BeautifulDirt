from datetime import timedelta, datetime
import requests

from core.config import app_settings


def get_playlist():

    playlist = list()

    payload = {
        'access_token': app_settings.access_token,
        'user_id': app_settings.user_id,
        'group_id': app_settings.group_id,
        'count': '1',
        'v': '5.199'
    }

    resp = requests.get(url='https://api.vk.com/method/messages.getHistory',
                        params=payload)

    if resp.status_code == 200:
        info = resp.json()['response']['items'][0]['attachments']

        for audio in info:
            delta = timedelta(seconds=audio['audio']['duration'])
            playlist.append(f" - 🎵 [{str(delta).replace('0:', '')}]"
                            f" {audio['audio']['artist']}"
                            f" - {audio['audio']['title']}")
    return playlist


def get_experience():

    internship = 117
    begin_work = datetime(2021, 8, 11, 0, 0, 0)

    experience = datetime.now() - timedelta(days=internship) - begin_work

    return experience.days
