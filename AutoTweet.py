import tweepy
import time

auto_message_greet = 'AUTO TWEET: '

target_time = "16:54:00"
message = 'Step 1: create auto tweeter that works.'

auth = tweepy.OAuthHandler()
auth.set_access_token()


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
            api.update_status(auto_message_greet + message)
        except tweepy.TweepError as e:
            print(e.reason)      
tweet_func()
    
#api.update_status(line)
#api.update_status("test")






