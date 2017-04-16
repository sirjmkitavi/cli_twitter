#!/usr/bin/env python3
from twitter import *
import sys
import json

# new app kit Africa Security
consumer_key= ''
consumer_secret = ''
token = ''
token_secret = ''


t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

count = 10
if len(sys.argv) > 1:
    first = str(sys.argv[1])
    second = ""
    third = ""
if len(sys.argv) > 2:
    second = str(sys.argv[2])
    third = ""
if len(sys.argv) > 3:
    third = str(sys.argv[3])

if first == "timeline":
    if second and second.isdigit() is True:
        count = int(second)
    if second.isdigit() is True or second == "":
        for x in t.statuses.home_timeline(count=count):
            print(x['user']['screen_name'] + ":  :" + x['text'])

    if second and second != "":
        if third and third.isdigit() is True:
            count = int(third)
        if third.isdigit() is True or third == "":
            for x in t.statuses.user_timeline(screen_name=second, count=count):
                print(x['user']['screen_name'] + ":  :" + x['text'])
elif first == "user":
	print(t.screen_name)

elif len(sys.argv) ==2 and first != "timeline":
	t.statuses.update(status=sys.argv[1])

else:
	print("Come on please just do it right?")

# for x in t.users.lookup(screen_name=','.join(), _timeout=1):
# 	print(x['user']['screen_name'])
# 	t.statuses.update(status=sys.argv[1])
# # for x in t.statuses.home_timeline(count=1):
# 	for y in x['entities']['user_mentions']:
# 		print(str(y))
    # print( x['entities']['user_mentions'][0]['screen_name'] + ": -" + x['text'])
