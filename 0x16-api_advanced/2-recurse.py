#!/usr/bin/python3

"""
This module provides a recursive function to query the Reddit API and return a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively query the Reddit API and return a list containing the titles of all hot articles for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list of hot article titles (default is an empty list).

    Returns:
        list or None: The list containing the titles of hot articles, or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': None}
    headers = {'User-Agent': 'Mozilla/5.0'}  # Custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            if data['data']['after'] is not None:
                params['after'] = data['data']['after']
                recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None  # No posts or unexpected data structure
    else:
        return None  # Invalid subreddit or server error

if __name__ == "__main__":
    subreddit_name = 'learnprogramming'
    hot_articles = recurse(subreddit_name)
    if hot_articles is not None:
        print(f"All hot articles in r/{subreddit_name}:")
        for article in hot_articles:
            print(article)
    else:
        print("No results found.")
