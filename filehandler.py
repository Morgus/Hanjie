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

class Load:
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
    # Loads a puzzle and returns its size, cluestrings for left and top,
    # name and list of squares needed to fill.
    # ########################
    def puzzle(self, pznum):
        filename = self.join("data", "puzzles", "pz"+str(pznum)+".txt")
        with open(filename, "r") as puzzle:
            readline = puzzle.readline
            # Puzzle size #
            raw_size = readline()
            size_len = len(raw_size)-1
            size_len_not_last = size_len-1
            size = []
            # Clue numbers #
            leftline = readline()
            left_len = len(leftline)-1
            left_len_not_last = left_len-1
            left_list = []
            topline = readline()
            top_len = len(topline)-1
            top_len_not_last = top_len-1
            top_list = []
            # Win list #
            winline = readline()
            win_len = len(winline)-1
            win_len_not_last = win_len-1
            win_len_not_sec_last = win_len-2
            win_list = []
            # Name #
            name = readline()
        # Puzzle size #
        r = 0
        append = size.append
        while r < size_len:
            num = raw_size[r]
            if not num.isdigit():
                pass
            else:
                if r < size_len_not_last:
                    sec_num = raw_size[r+1]
                    if sec_num.isdigit():
                        append(int(num+sec_num))
                        r += 1
                    else:
                        append(int(num))
                else:
                    append(int(num))
            r += 1
        # Clue numbers: Left #
        r = 0
        col = 1
        append = left_list.append
        while r < left_len:
            clue = leftline[r]
            if clue == ".": #If dot then the next number will be in the next row
                col = 1
            elif clue == ",": #If point then the next number will be in the next column
                col += 1
            else:
                if r < left_len_not_last:
                    clue2 = leftline[r+1]
                    if clue2.isdigit():
                        append((int(clue+clue2), col))
                        r += 1
                    else:
                        append((int(clue), col))
                else:
                    append((int(clue), col))
            r += 1
        # Clue numbers: Top #
        r = 0
        col = 1
        append = top_list.append
        while r < top_len:
            clue = topline[r]
            if clue == ".": #If dot then the next number will be in the next row
                col = 1
            elif clue == ",": #If point then the next number will be in the next column
                col += 1
            else:
                if r < top_len_not_last:
                    clue2 = topline[r+1]
                    if clue2.isdigit():
                        append((int(clue+clue2), col))
                        r += 1
                    else:
                        append((int(clue), col))
                else:
                    append((int(clue), col))
            r += 1
        # Win list #
        r = 0
        col = 1
        append = win_list.append
        while r < win_len:
            winnum = winline[r]
            if winnum == ".":
                pass
            else:
                if r < win_len_not_last:
                    winnum2 = winline[r+1]
                    if winnum2.isdigit(): #Check whether there are two numbers
                        if r < win_len_not_sec_last:
                            winnum3 = winline[r+2]
                            if winnum3.isdigit(): #Check whether there are three numbers(can't be higher than three because the biggest puzzle now is 31x30)
                                append(int(winnum+winnum2+winnum3))
                                r += 2
                            else:
                                append(int(winnum+winnum2))
                                r += 1
                        else:
                            append(int(winnum+winnum2))
                            r += 1
                    else:
                        append(int(winnum))
                else:
                    append(int(winnum))
            r += 1
        return size, left_list, top_list, win_list, name
    # ########################
    # Handles all image, sound, music and font loading. Also handles the
    # check for the number of puzzles.
    # ########################
    def data(self, name="", ftype="", alpha=0, fontsize=0):
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
    def saved_data(self):
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

class Save:
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
