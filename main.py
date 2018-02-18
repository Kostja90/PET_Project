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


# Create a UserToken to access the Group page 
#class UserToken:
#    def __init__(self):

# expiring on April 18th 2018
userToken = 'EAACTlWJB8fYBAJhmTiW0Dunh4DzgXOviQNbJOAgZBGIM1JDmqhdU1kwB8vZBbW1vcjTIoxZCLXejUk3hb0la6m74QGxFSUngguyaRM4P727YmoLgLbShLX5vXBkoOQNQJCh8ee7lWyOD3FNOGsJ8eQZBXZA1knjQfkKJ18w8mZBwZDZD'



# Request to Facebook 
graph = facebook.GraphAPI(access_token=userToken, version = 2.10, timeout = 120)
#events = graph.request("https://graph.facebook.com/groups/ELESBerlinPotsdam/")
events = graph.request("147206572004188?fields=events")
feeds = graph.request("147206572004188?fields=feed")

stam = graph.request('/oauth/access_token?grant_type=fb_exchange_token&client_id={162269807899126}&client_secret={2a8e0dd875bc7d333de8912b8378b7e6}&fb_exchange_token={EAACTlWJB8fYBAPmm44xzzMZA6tQoTD0AuprMiFvmuZB3C6DDf32EskCPREZA9oXbU0JQMgNpahGjcZBftUgtVJHmkWcovD3gpuCYhDR8Clcm2XspOqGbeDXZCkkOOXZAkIbyFsMCtaDmSV0V0oEEVffCisnXLGJT4jhbzj7DLpfZBlNSIkkg9OyZCNZBNeiZBuKc0ZD}')

stam
events
feeds
#eventList = events['data']

