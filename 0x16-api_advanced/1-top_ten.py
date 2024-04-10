#!/usr/bin/python3

"""
This module provides a function to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'test23'}  # Custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("No posts found.")  # No posts or unexpected data structure
    else:
        print("Invalid subreddit.")  # Invalid subreddit or server error

if __name__ == "__main__":
    subreddit_name = 'learnprogramming'
    print(f"Top 10 posts in r/{subreddit_name}:")
    top_ten(subreddit_name)
