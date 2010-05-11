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

from pygame import display, event
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from filehandler import *
from GameBase import *

def game(puzzlenum, screen, solved):
    #########################
    ### Loading resources ###
    bgc = (255, 255, 255)
    r = 1
    L = Load()
    S = Save()
    square = L.data("square.png", "img", 1)
    empty_sq = L.data("empty_sq.png", "img", 1)
    clues = (L.data("clue_top.png", "img", 1), L.data("clue_right.png", "img", 1))
    ############################
    ### Drawing first screen ###
    screen.fill(bgc)
    puzzlesize, puzzlefilename = PuzzleLoader("pz"+str(puzzlenum)+".txt")
    baserects = Make_sqrect(puzzlesize)
    Coll_squares = Make_sqrect(puzzlesize, 1) #TODO: Needs to be at center of the window
    blit = screen.blit
    for sqrect in baserects:
        blit(square, sqrect)
    winlist = DrawClues(puzzlesize, screen, clues, puzzlefilename)
    filledlist = []
    display.update()
    ##################
    ### Event loop ###
    while r:
        for ev in event.get():
            if ev.type == QUIT: quitprogram()
            if ev.type == MOUSEBUTTONDOWN: #If mouse button is pressed
                if ev.button == 1:
                    filledlist = MouseClicks(Coll_squares, screen, 1, filledlist, bgc)
                elif ev.button == 3:
                    MouseClicks(Coll_squares, screen, 0, filledlist, bgc, empty_sq)
                elif ev.button == 2:
                    MouseClicks(baserects, screen, 0, filledlist, bgc, square)
                r = PuzzleChecker(filledlist, winlist, puzzlenum, screen, bgc)
                display.update()
    solved.append(puzzlenum)
    s.solvedpuzzles(solved)
    wait(1.5)
    return puzzlenum, solved

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    wait(1.5)
    quitprogram()
