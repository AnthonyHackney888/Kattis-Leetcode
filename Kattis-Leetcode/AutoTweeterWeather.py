import tweepy
import time
import matplotlib.pyplot as plt
import numpy as np
import pyowm

auto_message_greet = 'AUTO TWEET: '

target_time = "17:18:00"
message = 'Step 1: create auto tweeter that works.'

auth = tweepy.OAuthHandler('GVBrIeelqRvm6fBV2YJR2TEi5', 'WjmtcfT3GxLE0N9BA6kAdgLeL1I5PcTFQG5FMNKh3z1QYwD4AA')
auth.set_access_token('1260637407042588678-y6ItYJ4G0MdWRsJYfsT9Iogsl7qVmX', 'POUqeaW31khpNS00mzclcKfHKvvWrBfD6tVsnai0MfZmD')


def weatherObserver():
    #API key

    #name
    #TrialKey
    openWeatherApi = 
    #my api key will need to create an account with OpenWeather
    owm = pyowm.OWM(openWeatherApi)
    #search for weather in Grand Rapids MI
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Grand Rapids,US')
    w = observation.weather
    a=w.temperature('fahrenheit').get("temp")
    b=w.temperature('fahrenheit').get("temp_max")
    c=w.temperature('fahrenheit').get("temp_min")
    d=w.temperature('fahrenheit').get("feels_like")
    e=("Current temp: "+str(a)+"f Max temp: "+str(b)+"f Min temp: "+str(c)+"f feels like: "+str(d)+"f")
    #in case I need to visualize the weather data
    '''
    names = ['Current temp','Max temp','Min temp', 'Feels like']
    values = [a,b,c,d]
    plt.figure(figsize=(9,3))
    plt.subplot(131)
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=2.0, hspace=0.25,
                    wspace=0.35)
    plt.bar(names, values)
    plt.suptitle('Grand Rapids temp')
    plt.savefig('GrandRapidstemp.png')
    '''
    return(e)

def time_set():
  return time.strftime("%H:%M:%S")

def check_credentials():
    api = tweepy.API(auth)
    if api.verify_credentials() == False:
        print('auth failed')
    else:
        print('auth ok')

def tweet_func():
  api = tweepy.API(auth)
  check_credentials()
  while time_set != target_time:
    time.sleep(.001)
    if time_set() == target_time:
        try:
            api.update_status(auto_message_greet + weatherObserver())
        except tweepy.TweepError as e:
            print(e.reason)      
tweet_func()
    
#api.update_status(line)
#api.update_status("test")





