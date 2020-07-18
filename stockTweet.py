from textblob import TextBlob
import tweepy
import statistics

consumer_key = "ptXDbfj2Knfku6S92dCd9iGXJ"
consumer_secret = "d9Ugs1UuMMrzHay8IMJn0wFh5gJCIq3NW929ulGy3TAL1Rt5Jx"

access_token = "1189546996631330818-BUnfrfjboBlIEGM9UBntl19ksl0nBX"
secret_token = "hTDUpOSiJrs3sG91JQgcejbaZzk3nfJegb99p6q28qSiv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_token)
candList = ['CROX','American International Group','CPB','SGEN','AAPL','ZURVY','S&P500', 'VIX','ROKU','SNAP','SKX','Crocs']
d = {}
finishedDict = {}

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
