# Twitter-dumps
A repository with scripts for downloading data from Twitter

##How to run the scripts.
1. Create a Twitter Application on apps.twitter.com
2. In the python scripts in this repository, add the values of the consumer key, the consumer secret, the api key and the api secret from the application created. 

###Downloading all tweets from a user's account.
To download the tweets from a user account, run the script as follows: python tweet_dump.py "name_of_user" 
This would download all tweets from a user's account. However, there is an upper limit of around 3186 tweets with this method. 
The tweets are saved in a csv file called "name_of_user.csv" 

##Downloading names of followers of a user.
To download the names of the followers of a user, run the script as follows: python follower1.py > output.txt 
The names of the followers would be printed in the output.txt file. 
However, the python library used, tweepy, has a rate limit on the number of requests that can be made from the API. Therefore, a time delay function has been added in the 
script to ensure that the rate limt is not reached. However, a downside to this time delay is that the script takes a long time to download. 
