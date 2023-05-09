#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print("None")
