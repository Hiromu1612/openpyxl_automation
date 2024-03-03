import tweepy
#twitterのAPIの認証情報
api_key="DEdbw91S1DH3RrYOMW4lworTA"
api_secret="Ht85UXjMizRmyzPQbVlELBJqLlUYCuvtonBxD0SJoqh9HNIsQL"
access_token="1500855684706942978-YffQaywRHu0zvvw1F3NggtN63p45CW"
access_token_secret="C802cMYmczUuGgOtk4vyxvnU9AKIIgjYxzOXN6FYMKKyb"
bearer_token="AAAAAAAAAAAAAAAAAAAAAOVEsgEAAAAATRrVZ7oGHcJ%2FJGpnDEuKKYPMy1A%3Dg2EYU8mJVwbnxbkI233bZtlVPkYxHUgn0Ohi4VkaHFcuMMFmkc"

#twitterオブジェクトの生成
# auth=tweepy.OAuthHandler(api_key,api_secret)
# auth.set_access_token(access_token,access_token_secret)
# api=tweepy.API(auth)

client = tweepy.Client(api_key,api_secret,access_token,access_token_secret,bearer_token)

#ツイートの投稿
client.create_tweet(text="ツイート文")
print("ツイートしました")