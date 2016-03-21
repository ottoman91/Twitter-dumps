#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv 
import sys 
import time

#Twitter API credentials
consumer_key = "FJrDMni4HoNVbm9QKQa9ca7dw"
consumer_secret = "xvMM8hFFfd5KeA4g46XwrZfdaGgQAxuEGGTNIuF4HPVtlp28at"
access_key = "57895109-m3hb5Y0xPT3UKqbs1aax37u1Pb9qRxV992t4J9gWp"
access_secret = "gYjOqC279TWSmR2NrPSIlXxkIQSqVpAGF9Q7nGd16bSq7"


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
	
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
	
    #initialize a list to hold all the followers 
    ids = []	
	
	
    for page in tweepy.Cursor(api.followers, screen_name=screen_name).items():
        # ids.extend(page.screen_name) 
        print page.screen_name
        time.sleep(60)

	
	


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets(sys.argv[1])

