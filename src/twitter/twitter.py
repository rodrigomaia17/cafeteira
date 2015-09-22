# -*- coding: utf-8 -*-

from datetime import datetime
from random import random
from twython import Twython
from credentials import *

class TwitterWrapper(Twython):
    def __init__(self):
        super(TwitterWrapper, self).__init__(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

class CoffeeTwitter(object):
    #ativa twitter
    TWITTER_ACTIVE = True

    def __init__(self):
        if self.TWITTER_ACTIVE:
            self.twitter = TwitterWrapper()

    def tweet(self):
        if self.TWITTER_ACTIVE:
            now = datetime.now()
            status = self.get_status()
            self.twitter.update_status(status = status % (now.hour, now.minute))

    def get_status(self):
        TWEETS = [
            "Olá, agora são %d hora(s) e %d minuto(s), o que acha de tomar um café? ThoughtWorks @ #CBSOFT2015",
            "%02d:%02d começando os preparativos para um café. ThoughtWorks @ #CBSOFT2015"
        ]

        return TWEETS[int(random()*len(TWEETS))]

    def tweet_panic(self):
        if self.TWITTER_ACTIVE:
            now = datetime.now()
            status = self.get_status_panic()
            self.twitter.update_status(status = status % (now.hour, now.minute))

    def get_status_panic(self):
        return "Olá, agora são %d hora(s) e %d minuto(s), deu treta na cafeteira, voltamos em alguns minutos!"
