from textblob import TextBlob
import pandas as pd
import re
import preprocessor as p
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv("./data/sts_gold_tweets.csv")
df = df.sort_values(by=['polarity'])

reals = []
preds = []

for index, row in df.iterrows():
    tweet = row["tweet.text"]
    # tweet = re.sub(r'^https?:\/\/.*[\r\n]*', '', tweet, flags=re.MULTILINE)
    tweet = p.clean(tweet)
    print(tweet, row["tweet.text"])
    tb = TextBlob(tweet)
    print(row["polarity"], 4 if tb.polarity > 0 else 0, tb.subjectivity)
    reals.append(row["polarity"])
    preds.append(4 if tb.polarity > 0 else 0)

# default accuracy is 72% - NICE!
print(accuracy_score(reals, preds))
print(confusion_matrix(reals, preds))
print(classification_report(reals, preds))
