#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles of all
hot articles for a givensubreddit. If no results are found for
the given subreddit, the function returns None.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    headers = {
        "User-Agent": "linux:alx-holberton.advanced_api"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    parameters = {"limit": 50, "after": after, "count": count}
    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    children = results.get("children")
    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
