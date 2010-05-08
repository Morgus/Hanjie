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

from pygame import image#, mixer
from os import path
from sys import exit as sysexit
from time import sleep

def load_img(name, alpha=0):
    join = path.join
    load = image.load
    try:
        imgname = join("data", "img", name)
        img = load(imgname)
        if alpha == 1:
            img.convert_alpha()
        else:
            img.convert()
    except:
        print "Can't load image: "+imgname
        sleep(1.5)
        sysexit()
    return img

##def load_snd(name):
##    join = path.join
##    sound = mixer.Sound
##    #try:
##    sndname = join("data", "snd", name)
##    print "Loading "+sndname
##    snd = sound(sndname)
##    #except:
##    #    print "Can't load sound: "+sndname
##    #    sleep(1.5)
##    #    sysexit()
##    return snd

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    sleep(1.5)
    sysexit()