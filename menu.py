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

# TODO: Redo this file
from pygame import event, display
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from menudefs import *
from extradefs import *
from filehandler import *

def menu(screen):
    data = LoadData()
    running = 1
    init = 1
    blit = screen.blit
    #######################
    ## Loading resources ##
    text = data.load("EHSMB.TTF", "font", fontSize=60)
    menubg = data.load("menubg.png", "img")
    allpuzzles, num = data.load(fileType="pzcount")
    solved = data.loadSolvedPuzzles()
    puzzlenum = 0
    menuType = "main"
    ## Menu loop ##
    while running:
        if init == 1:
            blit(menubg, screen.get_rect())
            menubuttons = create_menu(screen, text,
                                ["Play random puzzle", "Puzzle select", "Exit"]) #There may be some more return values for this sometime
            display.update()
            init = 0
        if menuType == "main": # Testing #
            for ev in event.get():
                if ev.type == QUIT: quitprogram()
                if ev.type == MOUSEBUTTONDOWN:
                    if ev.button == 1:
                        ##menuButtonClicked = 0
                        menuButtonClicked = MouseClicksMenu(menubuttons)
                        if menuButtonClicked == 1:
                            init = randompuzzle(solved, allpuzzles, menubg, screen, text, num)
                        elif menuButtonClicked == 2:
                            print "Function not yet implemented" #CHANGE
                            menuType = "select" #CHANGE
                        elif menuButtonClicked == 3:
                            quitprogram()
                        display.update()
        if menuType == "select": # Testing #
            ##menuButtonClicked = 0 # Testing #
            print "I'm in another menu!" # Testing #
            menuType = "main" # Testing #

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    wait(1.5)
    quitprogram()
