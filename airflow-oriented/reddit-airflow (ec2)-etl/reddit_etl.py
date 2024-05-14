import praw
import pandas as pd
import json
from datetime import datetime
import s3fs
import datetime
import pytz



USERNAME = 'Similar_Assignment59'
PASSWORD = 'Dehifi02!'
REDDIT_ID= 'EFB1dQ5JOX0PRi5GzlInNg'
REDDIT_SECRET = '01gYahIoPLEyVbZePLH3sXSsrqKDTw'


def run_reddit_etl():
    # convert the UTC time to Kyiv time
    kyiv_tz = pytz.timezone('Europe/Kyiv')

    # Define user agent
    user_agent = "praw_scraper_1.0"

    # Create an instance of reddit class
    reddit = praw.Reddit(
        username= USERNAME ,
        password= PASSWORD,
        client_id= REDDIT_ID,
        client_secret= REDDIT_SECRET,
        user_agent=user_agent
    )


    # Create sub-reddit instance
    subreddit_name = "dataengineering"
    subreddit = reddit.subreddit(subreddit_name)

    df = pd.DataFrame() # creating dataframe for displaying scraped data

    # creating lists for storing scraped data
    titles=[]
    scores=[]
    utc_time=[]


    # looping over posts and scraping it
    for submission in subreddit.top(limit=50):
        titles.append(submission.title)
        scores.append(submission.score) 
        utc_time.append(datetime.datetime.utcfromtimestamp(submission.created_utc).astimezone(kyiv_tz)) #"%Y-%m-%d %H:%M:%S" Kyiv timezone    
        

    df['Title'] = titles
    df['utc_time'] = utc_time
    df['Upvotes'] = scores 

    #print(df.head())

    df.to_csv("dataengineering_posts.csv")