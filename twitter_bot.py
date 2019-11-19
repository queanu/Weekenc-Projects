import tweepy as tp
import time
import os

# Get your private api access keys from twitter developer site 
Consumer_API_key = 'Consumer_API_key'
Consumer_API_secret_key = 'Consumer_API_secret_key'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

# With the tweepy api, initiate the class and populate it with the keys/secrets
auth = tp.OAuthHandler(Consumer_API_key, Consumer_API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth)

# Create a directory if one is not created and populate with random images from specified url
if not os.path.exists('twitter_post'):
    os.makedirs('twitter_post')
os.chdir('twitter_post')

# Post images to twitter and have the bot sleep for specified amount i.e 30 seconds
for image in os.listdir('.'):
    api.update_with_media(image)
    time.sleep(30)
    
