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
    site = 'https://burst.shopify.com/coffee'
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    os.chdir('twitter_post')
    urls = [img['src'] for img in img_tags]

    x = 0
    for url in urls:
        try:
            with open('images-' + str(x) + '.jpg', 'wb') as f:
                if 'http' not in url:
                    url = '{}{}'.format(site, url)
                f.write(requests.get(url).content)
                f.close()
                x += 1
        except:
            pass
        
os.chdir('twitter_post')

# Post images to twitter and have the bot sleep for 
# specified amount i.e 30 seconds within a loop function
for image in os.listdir('.'):
    try:
        api.update_with_media(image)
        time.sleep(30)
    except:
        pass
    
