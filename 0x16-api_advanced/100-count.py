#!/usr/bin/python3

"""
This module provides a recursive function to query the Reddit API, parse the titles of all hot articles, and print a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, counts={}):
    """
    Recursively query the Reddit API, parse the titles of all hot articles, and print a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): The list of keywords to count.
        counts (dict): A dictionary to store the counts of keywords (default is an empty dictionary).
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': None}
    headers = {'User-Agent': 'Mozilla/5.0'}  # Custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        if word.lower() in counts:
                            counts[word.lower()] += 1
                        else:
                            counts[word.lower()] = 1
            if data['data']['after'] is not None:
                params['after'] = data['data']['after']
                count_words(subreddit, word_list, counts)
            else:
                print_results(counts)
        else:
            print("No posts found.")  # No posts or unexpected data structure
    else:
        print("Invalid subreddit.")  # Invalid subreddit or server error

def print_results(counts):
    """
    Print the sorted count of keywords in descending order by count and alphabetically for tie-breakers.

    Args:
        counts (dict): A dictionary containing keyword counts.
    """
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")

if __name__ == "__main__":
    subreddit_name = 'learnprogramming'
    keywords = ['python', 'javascript', 'java']
    print(f"Count of keywords in r/{subreddit_name} hot articles:")
    count_words(subreddit_name, keywords)
