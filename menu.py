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

from pygame import event, display
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from menudefs import *
from extradefs import *
from filehandler import *

def menu(gameWindow):
    load = LoadData()
    running = 1
    init = True
    menuFont = load.load("EHSMB.TTF", "font", fontSize=60)
    menuBackground = load.load("menubg.png", "img")
    backGroundColor = 255, 255, 255
    puzzleList, maxPuzzleNumber = load.load(fileType="pzcount")
    solvedPuzzles = load.loadSolvedPuzzles()
    puzzleNumber = 1
    mainMenuButtons = ["Play random puzzle", "Puzzle select", "Exit"]
    menuType = "main"

    while running:
        if menuType == "main":
            if init:
                gameWindow.blit(menuBackground, gameWindow.get_rect())
                menuButtons = create_menu(gameWindow, menuFont, mainMenuButtons)
                display.update()
                init = False
            for ev in event.get():
                if ev.type == QUIT: quitprogram()
                elif ev.type == MOUSEBUTTONDOWN:
                    if ev.button == 1:
                        menuButtonClicked = MouseClicksMain(menuButtons)
                        if menuButtonClicked == 1:
                            init = randompuzzle(solvedPuzzles, gameWindow,
                                                maxPuzzleNumber)
                        elif menuButtonClicked == 2:
                            print "Function not yet implemented" # Testing #
                            init = True
                            menuType = "select"
                        elif menuButtonClicked == 3:
                            quitprogram()
                        display.update()
        elif menuType == "select":
            if init:
                gameWindow.fill(backGroundColor)
                display.update()
                init = False
                print "I'm in another menu!" # Testing #
            for ev in event.get():
                if ev.type == QUIT: quitprogram()
                elif ev.type == MOUSEBUTTONDOWN:
                    menuType = "main"
                    init = True

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    wait(1.5)
    quitprogram()
