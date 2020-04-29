# import twitter as tw
import os
import csv
import tweepy
import datetime

from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
#This function automatically loads any information from .env files into the local environment at runtime!
consumer_key = os.getenv('CKEY', '0')
consumer_secret = os.getenv('CSECRET', '0')
access_token = os.getenv('ATOKEN', '0')
access_token_secret = os.getenv('ASECRET', '0')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def save_hashtag_to_csv(hashtag, days, file):
    csvFile = open(file, 'w', newline='', encoding='utf8')
    csvWriter = csv.writer(csvFile)
    print(os.path.getsize(file))
    if os.path.getsize(file) ==0:
        csvWriter.writerow(
            [
                "tweet.id",
                "tweet.created_at",
                "tweet.text",
                "tweet.user.name",
                "tweet.user.screen_name",
                "tweet.user.location",
                "tweet.user.id",
                "tweet.user.followers_count",
                "tweet.user.friends_count",
                "tweet.user.favourites_count",
                "tweet.user.description"
            ]
        )
        csvFile.flush()
    base = datetime.date.today()+ datetime.timedelta(days=1)
    for day in [base - datetime.timedelta(days=x) for x in range(days)]:
        print(str(day), str(day - datetime.timedelta(days=1)))
        for tweet in tweepy.Cursor(
                api.search,
                q=hashtag,
                lang="en",
                until=str(day),
                since=str(day- datetime.timedelta(days=1)),
                result_type= "mixed").items(100):
            print(tweet.created_at, tweet.text)
            csvWriter.writerow(
                [
                    tweet.id,
                    tweet.created_at,
                    tweet.text.replace('\n', ' ').replace('\r', ''),
                    tweet.user.name,
                    tweet.user.screen_name,
                    tweet.user.location,
                    tweet.user.id,
                    tweet.user.followers_count,
                    tweet.user.friends_count,
                    tweet.user.favourites_count,
                    tweet.user.description.replace('\n', ' ').replace('\r', '')
                ]
            )

save_hashtag_to_csv("#covid", 7, "data/covid.csv")
save_hashtag_to_csv("#quarantine", 7, "data/quarantine.csv")

