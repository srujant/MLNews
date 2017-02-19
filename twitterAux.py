import requests
import twitter
# Authentication details. To  obtain these visit dev.twitter.com

api = twitter.Api(
consumer_key = 'fwmJ3rjwvYiWUBYaODcBCXA0w',
consumer_secret = 'uWBMfQ9Ej4VHHhqHyisJCkQlRvBcFizoItEBPxLwfd9Fsb1X7e',
access_token_key = '372410203-TsJxHcqavJuCl6uGBtZ5DzJNOLiuGDfxYnf1g3B2',
access_token_secret = 'OcqxkvzsYiG0OwWBKyKrC57cUcNz3rhkfOzn3MphBa74L'
)

search = api.GetSearch(term='George Takei: On this Remembrance Day, I hear terrible echoes of the past', lang='en', result_type='recent', count=1000, max_id='')
print(len(search))
