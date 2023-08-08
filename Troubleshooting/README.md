### 1. Key Doesn't Error
- This because if you're using pipenv, the activated virtual environment hasn't loaded the .env file.
  ### Solution:
  1. run  ```pipenv shell``` and then rerun the app.
  2. Delete the shell you're  working on and then rerun the above commands.

### 2. Wrong Key 
  ### Solution.
  - Make sure you clear your browser if you verified that the key is right.
  - Or Restart your computer.

### 3. raise Forbidden(response)
tweepy.errors.Forbidden: 403 Forbidden
When authenticating requests to the Twitter API v2 endpoints, you must use keys and tokens from a Twitter developer App that is attached to a Project. You can create a project via the developer portal.
  ### Solution:
    - This is because of the free tier, it's only allowed to Posting tweets with the Twitter API v2, anything else we would have to have atleast basic tier.
    source: [stackoverflow](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)