import tweepy as tw
import os

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

query_search = '#socialinnovation' + '-filter:retweets'


cursor_tweets = tw.Cursor(api.search, q=query_search).items(10)
for tweet in cursor_tweets:
    print(tweet.text)
