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

# TODO: Redo this file!
from pygame import display, event
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from filehandler import *
from GameBase import *

def game(puzzleNumber, gameWindow, solvedPuzzles):
    #########################
    ### Loading resources ###
    backGroundColor = (255, 255, 255)
    running = 1
    puzzle = LoadPuzzle(puzzleNumber)
    data = LoadData()
    save = SaveData()
    square = data.load("square.png", "img", 1)
    empty_sq = data.load("empty_sq.png", "img", 1)
    clues = (data.load("clue_top.png", "img", 1), data.load("clue_right.png", "img", 1))
    ############################
    ### Drawing first screen ###
    gameWindow.fill(backGroundColor)
##    puzzlesize, puzzlefilename = PuzzleLoader("pz"+str(puzzlenum)+".txt")
    baserects = Make_sqrect(puzzle.puzzleSize)
    Coll_squares = Make_sqrect(puzzle.puzzleSize, 1) #TODO: Needs to be at center of the window
    blit = gameWindow.blit
    for sqrect in baserects:
        blit(square, sqrect)
    winlist = DrawClues(puzzle.puzzleSize, gameWindow, clues, puzzle.puzzleFileName)
    filledlist = []
    display.update()
    ##################
    ### Event loop ###
    while running:
        for ev in event.get():
            if ev.type == QUIT: quitprogram()
            if ev.type == MOUSEBUTTONDOWN: #If mouse button is pressed
                if ev.button == 1:
                    filledlist = MouseClicks(Coll_squares, gameWindow, 1, filledlist, backGroundColor)
                elif ev.button == 3:
                    MouseClicks(Coll_squares, screen, 0, filledlist, backGroundColor, empty_sq)
                elif ev.button == 2:
                    MouseClicks(baserects, screen, 0, filledlist, backGroundColor, square)
                running = PuzzleChecker(filledlist, winlist, puzzleNumber, gameWindow, backGroundColor)
                display.update()
    solvedPuzzles.append(puzzleNumber)
    save.saveSolvedPuzzles(solvedPuzzles)
    wait(1.5)
    return puzzleNumber, solvedPuzzles

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    wait(1.5)
    quitprogram()
