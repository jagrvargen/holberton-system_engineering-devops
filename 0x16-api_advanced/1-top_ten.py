#!/usr/bin/python3
"""
   This module contains a function that queries the Reddit API and returns the
   top 10 posts for a given subreddit.
"""
import requests


def top_ten(subreddit):

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    user_agent = {"User-Agent": "JDawg 1.0"}

    req = requests.get(url, headers=user_agent)

    if req.status_code == 301:
        print("None")
        return None

    JSON = req.json()

    try:
        for item in JSON["data"]["children"]:
            for key, value in item["data"].items():
                if key == "title":
                    print(value)
    except:
        print("None")
        return None
