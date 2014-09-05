# What did I do?

Scrabble around on the internet and find this:

http://developer.neurosky.com/docs/doku.php?id=mindwave#installer_for_mac

(Linked from a dead link with www. in front of it - remove the www., profit!)


Ok so the MindWave (not Mobile) is RF, not Bluetooth. So install all the mono and crap...

Python hacking: https://ep2014.europython.eu/en/schedule/sessions/7/ https://github.com/akloster/python-mindwave


```
$ mkvirtualenv mindwave
$ mkdir mindwave
$ cd mindwave
$ pip install https://github.com/akloster/python-mindwave/archive/master.zip\#egg\=pymindwave

