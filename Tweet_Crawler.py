import tweepy
from tweepy import OAuthHandler
import pandas as pd
import time

access_token = '868158714-mthcwpcduyPODo1iYcBx0dYpdJjieE5bPZDyC5S8'
access_token_secret = 'XH2nB56BFkWJLWhMv3KIpQzer9VRJOZsnOCioYP7UCC0B'
consumer_key = 'utJ8k3max3uLccjZfwN8v7E4Z'
consumer_secret = 'zwrFCfafBuNYC1Erq41SP28vL5otNYK77FNn4dcTjUSespwhsu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# text_query = '#enoughvit'
# count = 150

text_query = input("Enter the Tweet or Search word : ")
count = int(input("Count : "))


try:
 # Creation of query method using parameters
 tweets = tweepy.Cursor(api.search,q=text_query).items(count) #, since='2021-06-07' 
 
 # Pulling information from tweets iterable object
 # tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
 # tweets_list = [[tweet.user.name, tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
 tweets_list = [[tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'], tweet.user._json['created_at']] for tweet in tweets]
 
 # Creation of dataframe from tweets list
 # Add or remove columns as you remove tweet information
 tweets_df = pd.DataFrame(tweets_list, columns =['Tweet Created At','Tweet ID','Search Result','Username','Profile Name','User Account Created At'])
 # print(tweets_df)
 tweets_df.to_excel(text_query + '.xlsx')
 print("The Scraple data is save as "+text_query + '.xlsx :>')
	
 
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)


# https://realpython.com/twitter-bot-python-tweepy/ - More methods!!!!