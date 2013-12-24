#!/usr/bin/python

#Imports
import requests
import re
import traceback 
import time
from datetime import datetime

from logger import get_logger

#
def blink(lites='off'):
    if lites =='on':
        for i in range(50):
            r = requests.get('http://10.0.1.212/on')
            r = requests.get('http://10.0.1.212/off')
            time.sleep(.2)

def check_for_snow():
    location = 'http://www.weather.com/weather/today/Boston+MA+USMA0046'
    req = requests.get(location)
    allHTML = req.content
    snowMentions = re.findall("wx-phrase.*?Snow", allHTML)
    if snowMentions:
        blink(lites='on')
        return True
    else:
        return False


def cycle():
    treeOn = False
    now = datetime.now().hour
    srt = 15
    stp = 23
    if now>int(srt):
        r = requests.get('http://10.0.1.212/on')
        treeOn = True
        if now==int(stp):
            r = requests.get('http://10.0.1.212/off')
            treeOn = False
    return treeOn

logger = get_logger()
isThereSnow = check_for_snow()
logger.debug("We checked for snow and this is what we got: %s" % isThereSnow)
isTreeOn = cycle()
logger.debug("The tree is on: %s" % isTreeOn)
