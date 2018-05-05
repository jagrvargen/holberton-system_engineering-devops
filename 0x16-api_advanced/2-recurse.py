#!/usr/bin/python3
"""
   This module contains a function that recursively queries the Reddit API for
   all hot articles of a given subreddit and returns a list containing their
   titles.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    user_agent = {"User-Agent": "JDawg 1.0"}
    temp_list = []

    if after is not None:
        url = url + "&after={}".format(after)
    else:
        return hot_list

    req = requests.get(url, headers=user_agent)
    JSON = req.json()

    try:
        children_list = JSON["data"]["children"]
    except:
        return None

    hot_list = hot_list + helper(children_list, 0, temp_list)

    return recurse(subreddit, hot_list, JSON["data"]["after"])

def helper(children_list, pos, temp_list):

    if pos >= len(children_list):
        return temp_list

    temp_list.append(children_list[pos]["data"]["title"])
    return helper(children_list, pos + 1, temp_list)
