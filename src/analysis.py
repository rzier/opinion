#!/usr/bin/env python


import pandas as pd
import os
import sys
vid = sys.argv[1] 
df = pd.read_csv("../data/%s/%s.csv"%(vid, vid), lineterminator='\n')

try:
    df.drop("Unnamed: 0", axis=1, inplace=True)
except:
    print("Already Deleted")
df["date"] = pd.to_datetime(df["date"])

import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
df.dropna(inplace=True)

neg = []
pos = []
comp = []
neu = []


for x in df["comment"]:
    score = sid.polarity_scores(x)
    comp += [ score["compound"] ]
    neu += [ score["neu"] ]
    pos += [ score["pos"] ]
    neg += [ score["neg"] ]


df["score_neg"] = neg
df["score_pos"] = pos
df["score_neu"] = neu
df["score_comp"] = comp
                                                                              

from matplotlib import pyplot as plt
import seaborn as sea

df["month"] = df["date"].apply(lambda x : x.strftime("%Y-%m"))
df["month"] = pd.to_datetime(df["month"])
sea.histplot(x="month", data=df, bins=8, kde=True)
plt.xticks(rotation=90)

plt.savefig("../data/%s/histplot_month.jpg"%vid)
plt.show()

sea.lineplot(x="month", y="score_pos", data=df, label="Positive")
sea.lineplot(x="month", y="score_neg", data=df, label="Negitive")
sea.lineplot(x="month", y="score_comp", data=df, label="Compound")
plt.ylabel("Emotion")

plt.savefig("../data/%s/sentiment_over_time.jpg"%vid)
plt.show()

counts = [df[df["score_neg"] >= 0.2].count()[0], df[df["score_pos"] >= 0.2].count()[0], df[df["score_neu"] >= 0.2].count()[0]]
classes = ["Negitive", "Positive", "Neutral"]

plt.pie(counts, labels=classes)
plt.savefig("../data/%s/sentiment_overall.jpg"%vid)
plt.show()

x=df[["like","replies","score_pos","score_neu"]]
sea.heatmap(data=x.corr(),annot=True)
plt.savefig("../data/%s/correlation.jpg"%vid)
plt.show()


sea.lineplot(data=df,x="like",y="replies")
plt.savefig("../data/%s/line_replies.jpg"%vid)
plt.show()

#sea.pairplot(df,  vars = ['like', 'replies'])
#plt.savefig("./line_replies_pair.jpg"%vid)
#plt.show()

