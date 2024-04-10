#!/usr/bin/python3

"""
This module provides a function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0  # Invalid subreddit or data structure
    else:
        return 0  # Invalid subreddit or server error

if __name__ == "__main__":
    subreddit_name = 'learnprogramming'
    subscribers = number_of_subscribers(subreddit_name)
    print(f"The subreddit r/{subreddit_name} has {subscribers} subscribers.")

