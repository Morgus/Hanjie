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

from pygame import display, event, key
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_ESCAPE
from gamedefs import *
from extradefs import *
from filehandler import *

def game(puzzleNumber, gameWindow, solvedPuzzles):
    backGroundColor = (255, 255, 255)
    running = 1
    puzzle = LoadPuzzle(puzzleNumber)
    load = LoadData()
    save = SaveData()
    baseSquare = load.load("square.png", "img", 1)
    crossSquare = load.load("empty_sq.png", "img", 1)
    clueImages = (load.load("clue_top.png", "img", 1),
                    load.load("clue_right.png", "img", 1))

    gameWindow.fill(backGroundColor)
    baseGameArea = Make_sqrect(puzzle.puzzleSize) #TODO: Needs to be at the
    CollisionSquares = Make_sqrect(puzzle.puzzleSize, 1) # center of the window
    blit = gameWindow.blit
    for square in baseGameArea:
        blit(baseSquare, square)
    DrawClues(puzzle.puzzleSize, gameWindow, clueImages, puzzle.leftClues,
                                            puzzle.topClues, puzzle.puzzleTitle)
    filledSquares = []
    display.update()

    while running:
        for ev in event.get():
            if ev.type == QUIT: quitprogram()
            elif ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    filledSquares = MouseClicks(CollisionSquares, gameWindow, 1,
                                                filledSquares, backGroundColor)
                elif ev.button == 2:
                    filledSquares = MouseClicks(CollisionSquares, gameWindow, 2,
                                                filledSquares, backGroundColor)
                elif ev.button == 3:
                    filledSquares = MouseClicks(CollisionSquares, gameWindow, 3,
                                    filledSquares, backGroundColor, crossSquare)
                running = PuzzleChecker(filledSquares, puzzle.winSquares,
                                    puzzleNumber, gameWindow, backGroundColor)
                display.update()
            elif ev.type == KEYDOWN:
                keys = key.get_pressed()
                if keys[K_ESCAPE]:
                    return solvedPuzzles

    save.saveSolvedPuzzles(solvedPuzzles, puzzleNumber)
    wait(1.5)
    return solvedPuzzles

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    wait(1.5)
    quitprogram()
