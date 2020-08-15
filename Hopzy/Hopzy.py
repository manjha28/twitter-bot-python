import tweepy
access_token_secret = "NTOTmuKeCWxQhDrG1ljFAqmau6mIpSmLhM7VH9BZe3TPS"
access_token = "1233747821481738241-dxXV9DlnozmkHBcnjyJayvsqfPOaWn"
consumer_key = "gjBgvtBurqP4T6U0Ps7Hrfa9m"
consumer_secret = "y7F2I6OvFxS8QXHY84n3gA08zcEYAM18ZYG0rPDyo5KfN8Duem"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.get_user('twitter')
public_tweets = api.home_timeline()
print( user.screen_name)
print (user.followers_count)
for friend in user.friends():
   print (friend.screen_name)