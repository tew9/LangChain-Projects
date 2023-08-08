import os
from datetime import datetime, timezone
import logging

import tweepy

logger = logging.getLogger("twitter")

# handle authentication
twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_SECRET"],
)


def scrape_user_tweets(username, num_tweets):
    """
    Scrape a Twitter user's origial (i.e. not retweets or replies) and return them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url" (to the tweet).
    """
    user_id = twitter_client.get_user(username=username).data.id

    tweets = twitter_client.get_users_tweets(
        id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
    )
    tweet_list = []

    for tweet in tweets:
        if "RT 0" not in tweet.text and not tweet.text.startswith("@"):
            tweet_dic = {}
            tweet_dic["time_posted"] = str(
                datetime.now(timezone.utc) - tweet.created_at
            )
            tweet_dic["text"] = tweet.text
            tweet_dic["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
            tweet_list.append(tweet_dic)

    return tweet_list
