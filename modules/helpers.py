#!/usr/bin/env python
# coding: utf8
from gluon import *
import time;

def get_greeting():
    localtime = time.localtime(time.time())
    if localtime[3] < 12:
        return 'Good morning!'
    elif localtime[3] < 18:
        return 'Good afternoon!'
    else:
        return 'Good evening!'
