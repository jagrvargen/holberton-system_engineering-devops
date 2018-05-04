#!/usr/bin/python3
"""
   This module contains a function which will query the Reddit API and return
   the total number of subscribers for a given subreddit.
"""
import requests
from sys import argv


subreddit = argv[1]


def number_of_subscribers(subreddit):
    query_string = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "JDawg's Agent 1.0"}

    req = requests.get(query_string, headers=user_agent)
    JSON = req.json()

    if "message" in JSON and JSON["message"] == "Not Found":
        return 0

    total_subscribers = JSON["data"]["subscribers"]

    return total_subscribers
