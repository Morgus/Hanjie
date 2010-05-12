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
from time import sleep
from cPickle import load as pickleload
from cPickle import dump
from pygame import image, mixer, font

class LoadData:
    """Handles all data loading from a file."""
    def __init__(self):
        # For puzzle loading #
        # Nothing yet...
        # For data loading #
        self.join = path.join
        self.imgload = image.load
        self.sndload = mixer.Sound
        self.music = mixer.music
    # ########################
    # Handles all image, sound, music and font loading. Also handles the
    # check for the number of puzzles.
    # ########################
    def load(self, name="", ftype="", alpha=0, fontsize=0):
        # Image loading
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
        # Sound loading
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
        # Music loading
        elif ftype == "mus":
            try:
                pass
            except:
                pass
        # Font loading
        elif ftype == "font":
            text = font.Font(self.join("data", "font", name), fontsize)
            return text.render
        # Checks how many puzzles there are from _pzcount file
        elif ftype == "pzcount":
            with open(self.join("data", "puzzles", "_pzcount")) as pzcount:
                num = int(pzcount.readline())
            i = 1
            temp = []
            append = temp.append
            while i <= num:
                append(i)
                i += 1
            return temp, num
    # ########################
    # Loads the save file from root directory which contains puzzle numbers
    # of solved puzzles.
    # ########################
    def load_saved_data(self):
        try:
            with open("save", "r") as savefile:
                savelist = pickleload(savefile)
        except EOFError:
            savelist = []
        except IOError:
            savelist = []
            f = open("save", "w")
            f.close()
            del f
        return savelist

class LoadPuzzle:
    """Loads a puzzle file. You only need to initialize to get all values."""
    def __init__(self, puzzleNumber):
        self.puzzleFileName = path.join("data", "puzzles",
                                                "pz"+str(puzzleNumber)+".txt")
        self.loadFile()
        self.getSize()
        self.getLeftClues()
        self.getTopClues()
        self.getWinSquares()

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
        sizeAppend = self.size.append
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
    # ########################
    # Saves the mubers of the solved puzzles to a file.
    # ########################
    def solvedpuzzles(self, savelist):
        with open("save", "w") as savefile:
            savelist.sort()
            dump(savelist, savefile)

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    sleep(1.5)
    #sysexit()
