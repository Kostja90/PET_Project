#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:11:46 2018

@author: Konstantin Shuxtelinsky
"""

# HTTP client for Python
import urllib3

# facebook SDK
import facebook

# Requests is an Apache2 Licensed HTTP library, written in Python and 
# you don’t have to manually add query strings to URLs
import requests

# regular expressions 
import re


# Create a UserToken to access the Group page 
#class UserToken:
#    def __init__(self):

# expiring on April 18th 2018
userToken = 'EAACTlWJB8fYBAMtotg4frQeHvT1wvgMwXqdIyIwqo8PIrp7E2nYAU3R5XY3b6HnUN8ZCw2IJzIeY1xr2615l741cwUcdNcYBZCvyXXmNzANg08upy2uVJr5lmIk2D0PYrTdZCNcZBE5uDd9bo4kzizorEGk7Q28ZD'



# Request to Facebook 
graph = facebook.GraphAPI(access_token=userToken, version = 2.10, timeout = 120)
#events = graph.request("https://graph.facebook.com/groups/ELESBerlinPotsdam/")
events = graph.request("147206572004188?fields=events")
feeds = graph.request("147206572004188?fields=feed")

events['events']

# find if event 
prog = re.compile(r"event")

# generator Function 
def findIDs_genFunc(feedsAll):
    
    countFeeds = 0
    
    while True:
        try:
            prog.search(feedsAll["feed"]["data"][countFeeds]["story"])
            yield feedsAll["feed"]["data"][countFeeds]['id'], countFeeds
        except KeyError:
            pass
        except IndexError:
            return
        
        countFeeds += 1


identities = findIDs_genFunc(feeds)


for identity in identities:
    feedEvent = graph.request(identity[0]+'?fields=attachments')
    event = graph.request(feedEvent['attachments']['data'][0]['target']['id'])
    print (event)
print

event
    feedEvent = graph.request(identity[0]+'?fields=attachments')
    event = graph.request(feedEvent['attachments']['data'][0]['target']['id'])
    print (event)

prog.search(feeds["feed"]["data"][0]["story"])

feeds["feed"]["data"][0]

feeds["feed"]["data"][0]['id']

feeds["feed"]["data"][0]["story"] == ["story"]

#stam = graph.request('/oauth/access_token?grant_type=fb_exchange_token&client_id={162269807899126}&client_secret={2a8e0dd875bc7d333de8912b8378b7e6}&fb_exchange_token={EAACTlWJB8fYBAPmm44xzzMZA6tQoTD0AuprMiFvmuZB3C6DDf32EskCPREZA9oXbU0JQMgNpahGjcZBftUgtVJHmkWcovD3gpuCYhDR8Clcm2XspOqGbeDXZCkkOOXZAkIbyFsMCtaDmSV0V0oEEVffCisnXLGJT4jhbzj7DLpfZBlNSIkkg9OyZCNZBNeiZBuKc0ZD}')

#stam
events
feeds
#eventList = events['data']

