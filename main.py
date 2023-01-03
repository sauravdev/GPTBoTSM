# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:20:18 2023

@author: saurava
"""

import openai
import tweepy
import re


def generate_response(prompt, temperature):
    # Set the API key and model
    openai.api_key = ""
    model_engine = "text-davinci-002"

    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, temperature=temperature, max_tokens=2048, top_p=1, frequency_penalty=0, presence_penalty=0)
    response = completion.choices[0].text

    # Return the response
    return response


def get_popular_tweets(query):
    # Set the API key and secret
    consumer_key = ""
    consumer_secret = ""

    # Set the access token and secret
    access_token = ""
    access_token_secret = ""

    # Set up the API client
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Search for tweets and sort them by popularity
    tweets = tweepy.Cursor(api.search, q=query+ " -filter:retweets", lang="en", result_type ="mixed",tweet_mode='extended').items(30)

    # Return the list of tweets
    return tweets


def generate_summary(text, min_length, max_length):
    # Set the API key and model
    openai.api_key = "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"
    model_engine = "text-davinci-002"
    prompt=f"Please summarize this text between {min_length} and {max_length} words: {text}",
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, temperature=0, max_tokens=2048, top_p=1, frequency_penalty=0, presence_penalty=0)
    response = completion.choices[0].text
    # Return the response
    return response



# Test the function
tweets = get_popular_tweets("data science OR #datascience")


appended_posts = ""

for tweet in tweets:
    if 'media' not in tweet.entities or 'urls' not in tweet.entities:
        text=tweet.full_text
        # Remove URLs
        text = re.sub(r'https?://\S+', '', text)
        # Remove hashtags
        text = re.sub(r'#\S+', '', text)
        # Remove mentions
        text = re.sub(r'@\S+', '', text)
        # Remove special characters
        text = re.sub(r'[^\w\s]', '', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        appended_posts = appended_posts + " "+text



# Run the functions

temperature = 0.5

summary_response =  generate_summary(appended_posts, 10, 25)


post = generate_response("Write a viral linkedin post on the following text: "+summary_response, temperature)
print("Here is your next viral LinkedIn post : "+post)
tweet = generate_response("Write a viral tweet on the following text: "+summary_response, temperature)
print("Here is your next viral Tweet- "+tweet)

