#!/usr/bin/python3
"""
   This module contains a function that recursively queries the Reddit API for
   all hot articles of a given subreddit and returns a list containing their
   titles.
"""
import requests
from sys import argv


subreddit = argv[1]


def recurse(subreddit, hot_list=[], after=""):

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    user_agent = {"User-Agent": "JDawg 1.0"}

    if after is not None:
        url = url + "&after={}".format(after)
    else:
        return hot_list

    req = requests.get(url, headers=user_agent)
    JSON = req.json()
    for item in JSON["data"]["children"]:
        hot_list.append(item["data"]["title"])

    return recurse(subreddit, hot_list, JSON["data"]["after"])
