#!/bin/usr/python3
"""function that queries the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """methode"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid rate limiting issues
    headers = {'User-Agent': 'my-app'}
    
    try:

        response = requests.get(url, headers=headers, allow_redirects=False)
        

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
