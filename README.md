# Auto Tweet Quote

Tech Stack used:
- Python
- Twitter API
- Quotable API
- Github Action

### Purpose: 
Create a scheduled job to generate a random quote and tweet it via Twitter.
Visit my [Twitter](https://twitter.com/garbuja_p) for the result. (Note: all tweets are auto-generated via API.)

### Instruction:
 - Create a Twitter [developer](https://developer.twitter.com/) account (if you don't already have).
 - To get started with Twitter API you can refer to this [documentation](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/quick-start).
 - Retrieve the following key and keep it safe.
     - API Key (Consumer Key)
     - API Secret Key (Consumer Secret Key)
     - Access Token (Make sure you have at least [write permission](https://developer.twitter.com/en/docs/apps/app-permissions) in order to post a tweet.)
     - Access Token Secret
  - Make sure to use [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) to protect your keys.
  - The keys can be assigned via secret as an environmental variable from [my workflow](.github/workflows/tweet_scheduler.yml).
    ```
    CONSUMER_KEY: ${{ secrets.TWITTER_CONSUMER_KEY }}
    CONSUMER_SECRET: ${{ secrets.TWITTER_CONSUMER_SECRET }}
    ACCESS_TOKEN: ${{ secrets.TWITTER_ACCESS_TOKEN }}
    ACCESS_TOKEN_SECRET: ${{ secrets.TWITTER_ACCESS_TOKEN_SECRET }}
    ```
  - The environmental variable is used in our python file - [generate_quote_tweet.py](generate_quote_tweet.py)
    ```python
    import os
    
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    ```
  -  Random Quote is generated via [Quotable API](https://github.com/lukePeavey/quotable)

  ```python
    def get_random_quote():
      response = requests.get('https://api.quotable.io/random')
      data = response.json()
      return f'"{data["content"]}" - {data["author"]}'
  ```
  - Create a schedule job using [cron expression](https://github.com/Cron/Cron) in Github Action [Workflow](.github/workflows/tweet_scheduler.yml).
  - For further optimization, a {caching mechanism}(https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows) can be performed to speedup workflow. (Note: Caching is only useful when dependencies rarely change.)
  
    


