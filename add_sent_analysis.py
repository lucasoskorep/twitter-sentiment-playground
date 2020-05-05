from textblob import TextBlob
import pandas as pd
import preprocessor as p
from pathlib import Path
from glob import glob

def add_sent_analysis(file, dest):
    df = pd.read_csv(file)
    pol = []
    subj = []
    for index, row in df.iterrows():
        tweet = row["tweet.text"]
        tweet = p.clean(tweet)
        tb = TextBlob(tweet)
        pol.append(tb.polarity)
        subj.append(tb.subjectivity)

    df["pred_polarity"] = pol
    df["pred_subj"] = subj
    df.to_csv(dest, quoting=2, index=False)

for file in glob("./data/*"):
    print(file)
    print()
    add_sent_analysis(file, "./processed_data/" + Path(file).name)
# default accuracy is 72% - NICE!