#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:11:46 2018

@author: Konstantin Shuxtelinsky
"""

# HTTP client for Python
#import urllib3

# facebook SDK
import facebook

# Requests is an Apache2 Licensed HTTP library, written in Python and 
# you don’t have to manually add query strings to URLs
#import requests

# regular expressions 
import re


# expiring on April 18th 2018
userToken = 'EAACTlWJB8fYBAMtotg4frQeHvT1wvgMwXqdIyIwqo8PIrp7E2nYAU3R5XY3b6HnUN8ZCw2IJzIeY1xr2615l741cwUcdNcYBZCvyXXmNzANg08upy2uVJr5lmIk2D0PYrTdZCNcZBE5uDd9bo4kzizorEGk7Q28ZD'

# Request to Facebook 
graph = facebook.GraphAPI(access_token=userToken, version = 2.10, timeout = 120)
events = graph.request("147206572004188?fields=events")
feeds = graph.request("147206572004188?fields=feed")

# normelize all found events
def eventHandling(event):
    
    listOfkeys = ["start","end","title","description","location","adress"]
    listOfvalues = "event['start_time'],event['end_time'],\
    event['name'],event['description'],event['place']['location'],\
    event['place']['name']"
    
    result = {}
    
    for countVar in range(0,len(listOfkeys)):        
        try:            
            result[listOfkeys[countVar]] = eval(re.split(',',listOfvalues)[countVar])
        except KeyError:
            pass
    return(result)


# generator Function finds all Id's from feeds that are events
def findEventIDs_genFunc(feedsAll):
    
    # regEx to find events 
    prog = re.compile(r"event")
    
    countFeeds = 0
    
    while True:
        try:
            if(prog.search(feedsAll["feed"]["data"][countFeeds]["story"]) != None):
                yield feedsAll["feed"]["data"][countFeeds]['id'], countFeeds
        except KeyError:
            pass
        except IndexError:
            return
        
        countFeeds += 1


# function calling 
identities = findEventIDs_genFunc(feeds)


eventPosts = {}

# go throug all found events 
for counter,identity in enumerate(identities):
    feedEvent = graph.request(identity[0]+'?fields=attachments')
    event = graph.request(feedEvent['attachments']['data'][0]['target']['id'])
    eventPosts[counter] = eventHandling(event)
    
    # delete double postings
    try:
        if(eventPosts[counter - 1] == eventPosts[counter]):
            del eventPosts[counter]
    except KeyError:
        pass

    


#ident = next(identities)
#
#feedEvent = graph.request(ident[0]+'?fields=attachments')
#event = graph.request(feedEvent['attachments']['data'][0]['target']['id'])
#print(identity)
#try:
#    event['event_times']
#except KeyError:
#    pass
#
#feedEvent['attachments']['data'][0]['target']['id']
#
#event
#feedEvent = graph.request(identity[0]+'?fields=attachments')
#event = graph.request(feedEvent['attachments']['data'][0]['target']['id'])
#print (event)
#
##prog.search(feeds["feed"]["data"][0]["story"])
#
#feeds["feed"]["data"][0]
#
#feeds["feed"]["data"][0]['id']
#
##feeds["feed"]["data"][0]["story"] == ["story"]
#
##stam = graph.request('/oauth/access_token?grant_type=fb_exchange_token&client_id={162269807899126}&client_secret={2a8e0dd875bc7d333de8912b8378b7e6}&fb_exchange_token={EAACTlWJB8fYBAPmm44xzzMZA6tQoTD0AuprMiFvmuZB3C6DDf32EskCPREZA9oXbU0JQMgNpahGjcZBftUgtVJHmkWcovD3gpuCYhDR8Clcm2XspOqGbeDXZCkkOOXZAkIbyFsMCtaDmSV0V0oEEVffCisnXLGJT4jhbzj7DLpfZBlNSIkkg9OyZCNZBNeiZBuKc0ZD}')
#
##stam
#events
#feeds
##eventList = events['data']
#
