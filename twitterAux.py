import sys
sys.path.append('./GetOldTweets')
import got

def getCount(query):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('query').setSince("2017-02-17").setUntil("2017-02-18").setMaxTweets(5000)
    return len(got.manager.TweetManager.getTweets(tweetCriteria))
