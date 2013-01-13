#!/usr/bin/python

"""
send the starwars episode 4 ascii art to a friend on skype
"""

import time
import sys
import telnetlib
import Skype4Py

if len(sys.argv) < 2:
        print """usage: starwars2skype.py USERNAME

USERNAME is the user you want to delight with some
star wars episode iv ascii art
"""
        sys.exit()

username = sys.argv[1]

s = Skype4Py.Skype()
s.FriendlyName = 'starwars2skype'
s.Attach()

tn = telnetlib.Telnet("towel.blinkenlights.nl")

while True:
        txt = tn.read_very_eager()
        if txt != "":
                s.SendMessage( username, txt )
        time.sleep(1)
