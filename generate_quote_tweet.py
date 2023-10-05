from requests_oauthlib import OAuth1Session
import requests
import os
import json

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Function to get a random quote
def get_random_quote():
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    return f'"{data["content"]}" - {data["author"]}'

#Insert tweet in payload.
payload = {"text": get_random_quote()+"\n #quote #autotweet #quotebot #quoteOfTheDay"}
print("Payload: %s" % payload)

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
