# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:52:40 2016

@author: burgoonl
"""

class Aop(object):
    
    def __init__(self, aop_wiki_id, long_name, short_name, url):
        self.aop_wiki_id = aop_wiki_id
        self.long_name = long_name
        self.short_name = short_name
        self.url = url
        self.key_events = []
        self.key_event_relationships = {}
        
        
    def add_key_event(self, key_event):
        self.key_events.append(key_event)
        
    def add_key_event_relationship(self, start_key_event, end_key_event):
        if(start_key_event in self.key_event_relationships):
            end_key_events = self.key_event_relationships[start_key_event]
            end_key_events.append(end_key_event)
            self.key_event_relationships[start_key_event] = end_key_events
        else:
            end_key_events = [end_key_event]
            self.key_event_relationships[start_key_event] = end_key_events
            
            
