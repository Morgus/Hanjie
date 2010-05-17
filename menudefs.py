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
from random import randint
from datetime import datetime
from pygame import mouse, font
import game

def create_menu(screen, text, menustrings): #Screen for blitting, text for the font and menustrings for the strings that are going to be written
    menubuttons = []
    append = menubuttons.append
    blit = screen.blit
    sr = screen.get_rect()
    c = -70
    for strs in menustrings:
        t = text(strs, True, (50, 50, 50))
        tr = t.get_rect()
        tr = tr.move(sr.centerx-t.get_width()/2, sr.centery-t.get_height()/2+c)
        blit(t, tr)
        append(tr)
        c += 70
    return menubuttons

def selectedpuzzle():
    pass

def randompuzzle(solved, screen, end): # Remove allpuz, menubg, text, end ## MAY CHANGE ##
    puzzlenum = randint(1, end)
    solved = game.game(puzzlenum, screen, solved)
    return True

def MouseClicksMain(buttons):
    """Handles mouse clicks"""
    mpos = mouse.get_pos()
    i = 1
    a = 0
    for rect in buttons:
        if rect.collidepoint(mpos):
            a = i
        i += 1
    return a

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    wait(1.5)
    quitprogram()
