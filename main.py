from traitlets.config.application import import_item
from typing_extensions import dataclass_transform
import urllib
from requests_oauthlib import OAuth1Session, OAuth1
import requests
import sys
import tweepy
import os
import random
import time
CK = ""
CKS = ""
AT = ""
ATS = ""
auth = tweepy.OAuthHandler(CK, CKS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)
api.update_status("かやだよ～")