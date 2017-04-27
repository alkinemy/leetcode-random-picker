#/usr/bin/env python

import requests

import os

SLACK_BOT_URL = os.environ.get('SLACK_BOT_URL')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL')


def random_pick_problem():
    random_pick_url = 'https://leetcode.com/problems/random-one-question/algorithms'
    response = requests.get(random_pick_url)
    return response.url

def notify_slack(message):
    url = SLACK_BOT_URL + '&channel=%23' + SLACK_CHANNEL 
    requests.post(url, data=message)


if __name__ == '__main__':
    picked_url = random_pick_problem()
    notify_slack(picked_url)
