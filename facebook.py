#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:11:46 2018

@author: Konstantin Shuxtelinsky
"""
# facebook SDK
import facebook

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