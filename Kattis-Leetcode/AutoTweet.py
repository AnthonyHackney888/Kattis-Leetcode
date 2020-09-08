import tweepy
import time
from tkinter import filedialog
from tkinter import *


auto_message_greet = 'AUTO TWEET: '
target_time = "19:06:00"

def time_set():
  return time.strftime("%H:%M:%S")


def open_dialog():
  auth = tweepy.OAuthHandler()
  auth.set_access_token()
  api = tweepy.API(auth)
  r.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
  with open(r.filename, 'r') as f:
    while True:
      while time_set() != target_time:
        time.sleep(.01)
      if time_set() == target_time:
        print('got here 2')
        try:
          api.verify_credentials()
          print('auth OK')
        except:
          print('error sorry B')
      try:
        test1 = f.readline()
        print(test1)
        if f != '\n':
          print('a')
          api.update_status(auto_message_greet + test1)
          break
      except tweepy.TweepError as e:
          print(e.reason)
    #api.update_status(line)
    #api.update_status("test")



r = Tk()
r.title('choose text file')
button = Button(r, text='open', width=25,command=open_dialog)
button.pack()
r.mainloop()



