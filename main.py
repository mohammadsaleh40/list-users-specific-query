import tweepy
from time import sleep
import json
import numpy as np
import pandas as pd

#search query
qu=""#To be changed

client = tweepy.Client(bearer_token="",
                       consumer_key="",
                       consumer_secret="",
                       access_token="",
                       access_token_secret="")

user_dict={}
page=0
search=client.search_recent_tweets(qu,max_results=10 ,expansions="author_id")
while True:
    try:
        page+=1
        print("page : ",page)
        for i in search.includes['users']:
            if i['username'] in user_dict:
                user_dict[i['username']]+=1
            else:
                user_dict[i['username']]=1
        search=client.search_recent_tweets(qu,next_token=search.meta['next_token'], max_results=10 ,expansions="author_id")

    except:
        break

# sort the dictionary by value
sorted_x = sorted(user_dict.items(), key=lambda kv: kv[1], reverse=True)
f=open("user_dict"+qu+".json","w")
json.dump(sorted_x ,f,indent=4)
f.close()