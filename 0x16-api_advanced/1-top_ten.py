#!/usr/bin/python3
"""
   This module contains a function that queries the Reddit API and returns the
   top 10 posts for a given subreddit.
"""
import requests
from sys import argv


subreddit = argv[1]


def top_ten(subreddit):

    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    user_agent = {"User-Agent": "JDawg 1.0"}

    req = requests.get(url, headers=user_agent)
    for item in req.history:
        if "301" in item:
            print("None")
            exit

    JSON = req.json()
    if not JSON["data"]["children"]:
        print("None")
        exit

    for item in JSON["data"]["children"]:
        for key, value in item["data"].items():
            if key == "title":
                print(value)
