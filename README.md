# GPTBoTSM
This is a Twitter bot that extracts data from twitter , generates a summary of popular tweets containing a specific query and then generates a viral LinkedIn post/ Tweet based on the summary.

## Requirements

- tweepy
- openai
- re

## Usage

To use the bot, you will need to provide your own API keys for Twitter and OpenAI. You can set these keys in the following variables:

```
openai.api_key = "YOUR_API_KEY"
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

You can then call the get_popular_tweets function to search for popular tweets containing a specific query, and the generate_summary and generate_response functions to generate a summary and a LinkedIn post based on the tweets.

For example:

```
tweets = get_popular_tweets("data science OR #datascience")
summary_response = generate_summary(tweets, 10, 25)
post = generate_response("Write a viral LinkedIn post on the following text: " + summary_response, temperature)
```

The get_popular_tweets function takes a query string as input and returns a list of tweets containing the query. The generate_summary function takes a list of tweets and a minimum and maximum length for the summary, and returns a summary of the tweets based on the most important and relevant information. The generate_response function takes a prompt string and a temperature value as input and generates a response based on the prompt and temperature.

You can then use the summary_response and post variables to access the summary and LinkedIn post generated by the bot.

## Additional Information

The get_popular_tweets function searches for tweets and sorts them by popularity. The generate_summary function uses the OpenAI API to generate a summary of the tweets based on the most important and relevant information. The generate_response function uses the OpenAI API to generate a LinkedIn post based on the summary. The temperature parameter controls the randomness of the generated text, with lower values resulting in more deterministic output and higher values resulting in more random output.

I hope this helps! Let me know if you have any further questions or need additional
