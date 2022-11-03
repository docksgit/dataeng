import pandas as pd
import tweepy
import json
import s3fs
from datetime import datetime

api_key = 'a7rDZjuytb7rSbGV54tOOW1OU'
api_key_secret = '2fLk1HVMkEXO9wbeRnUKZhpE6QDKJ9NALYLzkt7ypFR28qItyP'
access_token = '1267302304899727361-OOQN1J0J1K3Xy3hrMR11sCg5pYApJx'
access_token_secret = '61D6EUn1Gub6o7AfKnQJxNLsmDv1eB1lakOTyfO8yDHy6'

# Twitter authentication

# Twitter API v1.1
# auth = tweepy.OAuthHandler(access_key, access_secret)
# auth.set_access_token(consumer_key, consumer_secret)

# tweets = api.user_timeline(screen_name='@PT_Transjakarta',
#                             count=200, # 200 is the maximum allowed count
#                             include_rts = False,
#                             # Necessary to keep full_text otherwise only the first 140 words are extracted
#                             tweet_mode = 'extended'
#                             )

# Twitter API v2
#

# Get users tweets
# tweets = client.get_users_tweets(
#     id='@elonmusk',
#     exclude='retweets',
#     max_results=100,
# )

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAALBkiwEAAAAAuo5dohXuumgpQBAspceTIIYciVg%3DdBDRVNBJsxnaMaWU6SORU2HPwcMUhfJW3J4VUT6HsJNMwPFINK')

# Replace with your own search query
query = 'from:sjahqi -is:retweet'

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

# for tweet in tweets.data:
#     print(tweet.text)
#     if len(tweet.context_annotations) > 0:
#         print(tweet.context_annotations)

print(tweets.data)