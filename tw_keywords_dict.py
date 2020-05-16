import tweepy as tw
import os

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)
#public_tweets = api.home_timeline()

#for tweet in public_tweets:
    #try:
        #print(tweet.text)
    #except:
        #print(status)

query_search = '#ENEM' + '-filter:retweets'

tweets_dict = {}

cursor_tweets = tw.Cursor(api.search, q=query_search).items(10)
for tweet in cursor_tweets:
    twkeys = tweet._json.keys()
    tweets_dict = tweets_dict.fromkeys(twkeys)
    for key in tweets_dict.keys():
        try:
            twkey = tweet._json[key]
            tweets_dict[key].append(twkey)
        except KeyError:
            twkey = ''
            tweets_dict[key].append('')
        except:
            tweets_dict[key] = [twkey]
        print('tweets_dict[key]: {} - tweet[key]: {}'.format(tweets_dict[key], twkey))
