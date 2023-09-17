import http
import tweepy
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect



#Supriya Contribution#

def index(request):
    if request.method== 'POST':
        content=request.POST.get('content','')
        ID=request.POST.get('ID','')
        getQuery=request.POST.get('getQuery','')
        consumer_key=settings.API_KEY
        consumer_secret=settings.API_KEY_SECRET
        access_token=settings.ACCESS_TOKEN
        access_token_secret=settings.ACCESS_TOKEN_SECRET
        if content:
            print('content:', content)
            client= tweepy.Client(
            consumer_key=consumer_key,consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
            )
            response = client.create_tweet(
            text=content
            )
            tweeturl= "https://twitter.com/user/status/{}".format(str(response.data['id']))
            
            print(tweeturl)
            context ={"tweeturl":tweeturl}
            return render(request,'feed/successful.html',context)
        
        # Mohana Contribution #
        if ID:
            print('ID:', ID)
            client= tweepy.Client(
            consumer_key=consumer_key,consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
            )
            response = client.delete_tweet(ID)
            print(response)
            print("Tweet deleted")
            return redirect('delete.html')

        # Varun Contribution #

        if getQuery:
            print('getQuery',getQuery)
            bearer_token = settings.BEARER_TOKEN         
            client = tweepy.Client(bearer_token)
            response=client.search_recent_tweets(getQuery,max_results=10)
            
            tweets=response.data
            tweet_dict={}
            for tweet in tweets:
                tweet_dict.update({int(tweet.id):tweet.text})
            
            tmp_dict = {"tweet_dict":tweet_dict}
            
            return render(request,'feed/returntweets.html',tmp_dict)
        

    return render(request,'feed/index.html')
#Kevin Contribution#
def successful(request):
    return render(request,'feed/successful.html')

def delsuccessful(request):
    return render(request,'feed/delete.html')
def gettweets(request):
    return render(request,'feed/returntweets.html')



    
