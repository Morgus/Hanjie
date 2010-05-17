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

from sys import exit as sysexit
from time import sleep
from datetime import datetime

def error(location, errorInfo):
    with open("error.log", "a") as errorlog:
        errorlog.write(str(datetime.now())+"\n")
        errorlog.write(location+" - "+errorInfo+"\n\n")
    sysexit()

def wait(time):
    sleep(time)

def quitprogram():
    #Might be some more things here
    sysexit()

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    wait(1.5)
    quitprogram()
