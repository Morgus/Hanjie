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

from os import path
from sys import exit as sysexit
from sys import exc_info
from time import sleep
from cPickle import load as pickleload
from cPickle import dump
from pygame import image, mixer, font
from errors import error

class LoadData:
    """Handles all data loading from a file."""
    def __init__(self):
        self.join = path.join
        self.imageLoad = image.load
        self.soundLoad = mixer.Sound
        self.music = mixer.music

    def load(self, name="", fileType="", alpha=0, fontSize=0):
        if fileType == "img":
            try:
                imageFileName = self.join("data", "img", name)
                imageFile = self.imageLoad(imageFileName)
                if alpha == 1:
                    imageFile.convert_alpha()
                else:
                    imageFile.convert()
                return imageFile
            except:
                print "Can't load image: "+imageFileName
                raw_input("Press Enter to close")
                sysexit()
        elif fileType == "snd":
            try:
                soundFileName = self.join("data", "snd", name)
                soundFile = self.soundLoad(soundFileName)
                return soundFile
            except:
                print "Can't load sound: "+soundFileName
                raw_input("Press Enter to close")
                sysexit()
        elif fileType == "mus":
            try:
                pass
            except:
                pass
        elif fileType == "font":
            try:
                fontFileName = self.join("data", "font", name)
                fontFile = font.Font(fontFileName, fontSize)
                return fontFile.render
            except:
                print "Can't load font: "+fontFileName
                raw_input("Press Enter to close")
                sysexit()
        elif fileType == "pzcount":
            try:
                with open(self.join("data", "puzzles", "_pzcount")) as puzzleCount:
                    maxPuzzleNumber = int(puzzleCount.readline())
                counter = 1
                puzzleNumberList = []
                append = puzzleNumberList.append
                while counter <= maxPuzzleNumber:
                    append(counter)
                    counter += 1
                return puzzleNumberList, maxPuzzleNumber
            except:
                print "Can't load _pzcount"
                raw_input("Press Enter to close")
                sysexit()

    def loadSolvedPuzzles(self):
        try:
            with open("save", "r") as saveFile:
                solvedPuzzles = pickleload(saveFile)
        except EOFError:
            solvedPuzzles = []
        except IOError:
            solvedPuzzles = []
            f = open("save", "w")
            f.close()
            del f
        return solvedPuzzles

class LoadPuzzle:
    """Loads a puzzle file. You only need to initialize to get all values."""
    def __init__(self, puzzleNumber):
        self.puzzleFileName = path.join("data", "puzzles",
                                                "pz"+str(puzzleNumber)+".txt")
        try:
            self.loadFile()
            self.getSize()
            self.getLeftClues()
            self.getTopClues()
            self.getWinSquares()
        except:
            error("LoadPuzzle()", exc_info()[0])
            sysexit()

    def loadFile(self):
        with open(self.puzzleFileName, "r") as puzzleFile:
            read_line = puzzleFile.readline
            self.sizeString = read_line().rstrip()
            self.leftLine = read_line().rstrip()
            self.topLine = read_line().rstrip()
            self.winLine = read_line().rstrip()
            self.puzzleTitle = read_line().rstrip()

    def getSize(self):
        self.puzzleSize = []
        counter = 0
        sizeStringLength = len(self.sizeString)
        sizeStringNotLast = sizeStringLength-1
        sizeAppend = self.puzzleSize.append
        while counter < sizeStringLength:
            firstNumber = self.sizeString[counter]
            if not firstNumber.isdigit():
                pass
            else:
                if counter < sizeStringNotLast:
                    secondNumber = self.sizeString[counter+1]
                    if secondNumber.isdigit():
                        sizeAppend(int(firstNumber+secondNumber))
                        counter += 1
                    else:
                        sizeAppend(int(firstNumber))
                else:
                    sizeAppend(int(firstNumber))
            counter += 1

    def getLeftClues(self):
        self.leftClues = []
        counter = 0
        leftLineLength = len(self.leftLine)
        leftLineNotLast = leftLineLength-1
        column = 1
        clueAppend = self.leftClues.append
        while counter < leftLineLength:
            firstNumber = self.leftLine[counter]
            if firstNumber == ".":
                column = 1
            elif firstNumber == ",":
                column += 1
            else:
                if counter < leftLineNotLast:
                    secondNumber = self.leftLine[counter+1]
                    if secondNumber.isdigit():
                        clueAppend((int(firstNumber+secondNumber), column))
                        counter += 1
                    else:
                        clueAppend((int(firstNumber), column))
                else:
                    clueAppend((int(firstNumber), column))
            counter += 1

    def getTopClues(self):
        self.topClues = []
        counter = 0
        topLineLength = len(self.topLine)
        topLineNotLast = topLineLength-1
        row = 1
        clueAppend = self.topClues.append
        while counter < topLineLength:
            firstNumber = self.topLine[counter]
            if firstNumber == ".":
                row = 1
            elif firstNumber == ",":
                row += 1
            else:
                if counter < topLineNotLast:
                    secondNumber = self.topLine[counter+1]
                    if secondNumber.isdigit():
                        clueAppend((int(firstNumber+secondNumber), row))
                        counter += 1
                    else:
                        clueAppend((int(firstNumber), row))
                else:
                    clueAppend((int(firstNumber), row))
            counter += 1

    def getWinSquares(self):
        self.winSquares = []
        counter = 0
        winLineLength = len(self.winLine)
        winLineNotLast = winLineLength-1
        winLineNotSecondToLast = winLineLength-2
        winAppend = self.winSquares.append
        while counter < winLineLength:
            firstNumber = self.winLine[counter]
            if not firstNumber.isdigit():
                pass
            else:
                if counter < winLineNotLast:
                    secondNumber = self.winLine[counter+1]
                    if secondNumber.isdigit():
                        if counter < winLineNotSecondToLast:
                            thirdNumber = self.winLine[counter+2]
                            if thirdNumber.isdigit():
                                winAppend(int(firstNumber+secondNumber+
                                                                thirdNumber))
                                counter += 2
                            else:
                                winAppend(int(firstNumber+secondNumber))
                                counter += 1
                        else:
                            winAppend(int(firstNumber+secondNumber))
                            counter += 1
                    else:
                        winAppend(int(firstNumber))
                else:
                    winAppend(int(firstNumber))
            counter += 1

class SaveData:
    """Handles all data saving to a file."""
    def __init__(self):
        pass

    def saveSolvedPuzzles(self, solvedPuzzles):
        with open("save", "w") as saveFile:
            solvedPuzzles.sort()
            dump(solvedPuzzles, saveFile)

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    sleep(1.5)
    sysexit()
