##    Hanjie - A nonogram puzzle game made with python
##    Copyright (C) 2010 - Aleksi Blinnikka
##
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, see <http://www.gnu.org/licenses/>.

from pygame import image, mixer
from os import path
from sys import exit as sysexit
from time import sleep
from cPickle import load, dump as pload, dump

class load:
    def __init__(self):
        # For puzzle loading #
        # Nothing yet...
        # For data loading #
        self.join = path.join
        self.imgload = image.load
        self.sndload = mixer.Sound
        self.musload = mixer.music
    def puzzle(self, num):
        pass
    def data(self, name="", ftype="", alpha=0):
        if ftype == "img":
            try:
                imgname = self.join("data", "img", name)
                img = self.imgload(imgname)
                if alpha == 1:
                    img.convert_alpha()
                else:
                    img.convert()
            except:
                print "Can't load image: "+imgname
                sleep(1.5)
                sysexit()
            return img
        elif ftype == "snd":
            try:
                sndname = self.join("data", "snd", name)
                print "Loading "+sndname
                snd = self.sndload(sndname)
            except:
                print "Can't load sound: "+sndname
                sleep(1.5)
                sysexit()
            return snd
        elif ftype == "mus":
            try:
                pass
            except:
                pass
        elif ftype == "font":
            pass
    def saved(self):
        pass

class save:
    def __init__(self):
        pass
if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    sleep(1.5)
    sysexit()