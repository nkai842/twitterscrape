from textblob import TextBlob
import tweepy
import statistics

consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
secret_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_token)
candList = ['CROX','American International Group','CPB','SGEN','AAPL','ZURVY','S&P500', 'VIX','ROKU','SNAP','SKX','TSLA']
d = {}
finishedDict = {}

# meanSent() searches twitter for stock, pull 3200 tweets into a list, performs sentiment analysis on each and creates a new list, finds the average sentiment from list, 
# then adds stock ticker and average sentiment to dictionary.  Finally, dictionary is printed.

def meanSent():
    pol = []
    for cand in candList:
        api = tweepy.API(auth)
        analysis = api.search(q = cand, count = 3200, lang = 'en')
        for tweet in analysis:
            newValue = TextBlob(tweet.text)
            analyze = newValue.sentiment.polarity
            pol.append(analyze)
        avg = statistics.mean(pol)
        d[cand] = avg
        pol = []
    print(d)
    print(max(d, key=d.get))
    print(min(d, key=d.get))




meanSent()
