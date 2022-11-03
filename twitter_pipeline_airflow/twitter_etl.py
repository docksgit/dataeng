import pandas as pd 
import snscrape.modules.twitter as sntwitter
import s3fs 

def run_twitter_etl(username='jack', num_tweets=100):
    '''
    Output: .csv data of specific Twitter user
    '''
    # Creating list to append tweet data to
    tweets_list = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{}'.format(username)).get_items()):
        if i>num_tweets:
            break
        tweets_list.append([tweet.date, 
                            tweet.id, 
                            tweet.content, 
                            tweet.replyCount, 
                            tweet.retweetCount,
                            tweet.likeCount,
                            tweet.quoteCount,
                            tweet.user.username])
        
    # Creating a dataframe from the tweets list above 
    df = pd.DataFrame(tweets_list, columns=['datetime', 
                                            'tweet_id', 
                                            'text', 
                                            'reply_count', 
                                            'retweet_count', 
                                            'like_count',
                                            'quote_count', 
                                            'username'])
    df.to_csv('{}_tweets.csv'.format(username), index=False)

# username = 'ecommurz'
# run_twitter_etl(username)