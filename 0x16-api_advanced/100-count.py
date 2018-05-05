#!/usr/bin/python3
"""
   This module contains a function which will recursively query the Reddit API
   and print a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after="", word_dict={}):

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    user_agent = {"User-Agent": "JDawg 1.0"}
    temp_list = []

    if len(word_dict) == 0:
        for word in word_list:
            word_dict[word] = 0

    if after is not None:
        url = url + "&after={}".format(after)
    else:
        for key in word_dict.keys():
            if word_dict[key] > 0:
                print("{}: {}".format(key, word_dict[key]))
        return

    req = requests.get(url, headers=user_agent)
    JSON = req.json()

    try:
        children_list = JSON["data"]["children"]
    except:
        return None

    hot_list = helper(children_list, 0, temp_list)
    for title in hot_list:
        word_list = title.split()
        for word in word_list:
            if word.lower() in word_dict:
                word_dict[word.lower()] += 1

    return count_words(subreddit, word_list, JSON["data"]["after"], word_dict)


def helper(children_list, pos, temp_list):

    if pos >= len(children_list):
        return temp_list

    temp_list.append(children_list[pos]["data"]["title"])
    return helper(children_list, pos + 1, temp_list)
