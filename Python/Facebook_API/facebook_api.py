import requests
import json

#Insert facebook token here
access_token=""

def comment_on_posts(posts, amount):
    """Comment on top * posts"""
    counter = 0
    for post in posts:
        if counter >= amount:
            break
        else:
            counter = counter + 1
        url = "https://graph.facebook.com/{0}/comments".format(post['id'])
        message = "Hi, I'm bot no {0}, ignore this message".format(counter)
        parameters = {'access_token' : access_token, 'message' : message}
        s = requests.post(url, data = parameters)
        print s.status_code

def get_posts():
    """ Get posts"""
    payload = {'access_token' : access_token}
    r = requests.get('https://graph.facebook.com/me/feed', params=payload)
    print r.status_code
    result = json.loads(r.text)
    return result['data']

def hello(message):
    """ Publish a post"""
    payload = {
        "access_token" : access_token,
        "message" : message
    }
    url = "https://graph.facebook.com/me/feed?"
    r = requests.post(url, json=payload)
    print r.status_code

if __name__ == "__main__":
    posts = get_posts()
    comment_on_posts(posts, 25)
