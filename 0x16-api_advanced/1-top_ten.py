#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    headers = {
        "User-Agent": "linux:alx-holberton.advanced_api"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    parameters = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=parameters, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    res = response.json().get("data")
    for child in res.get("children"):
        print(child.get("data").get("title"))
