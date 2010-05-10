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

# TODO: All file handling in one separate source file (filehandler.py)
# TODO: Redo this file!
from filehandler import *
from os import path, SEEK_SET
from sys import exit as sysexit
from pygame import Rect, mouse, font
from time import sleep

def Make_sqrect(size, coll=0):
    """Makes the rectangles for all squares that are created,
    mainly for collision checking"""
    sq = []
    a, i, x, y = 0, 0, 110, 132
    sqnum = size[0]*size[1]
    if coll==1:
        while i < sqnum:
            sqrect = Rect(x+1, y+1, 20, 20)
            sq.append(sqrect)
            x = x+22
            a += 1
            if a == size[0]:
                x = 110
                y += 22
                a = 0
            i += 1
        i = 0
    else:
        while i < sqnum:
            sqrect = Rect(x, y, 22, 22)
            sq.append(sqrect)
            x = x+22
            a += 1
            if a == size[0]:
                x = 110
                y += 22
                a = 0
            i += 1
        i = 0
    return sq

def PuzzleLoader(fname): #Filename
    """ Loads numbers to be hints, in the file: two first rows for numbers,
    first for ones on left side and second on numbers on top, and then rest of
    the file will be for PuzzleChecker """
    size = []
    join = path.join
    try:
        with open(join("data", "puzzles", fname), "r") as puzzle:
            strsize = []
            sizerow = len(puzzle.readline())
            r = 0
            append = strsize.append
            read = puzzle.read
            puzzle.seek(0, SEEK_SET)
            while r < sizerow:
                num = read(1) #Reads each byte from the first row
                append(num) #Appends the data to the list
                r += 1

        append = size.append
        if strsize[0].isdigit():
            if strsize[1].isdigit():
                temp = int(strsize[0]+strsize[1])
                append(temp)
                r = 2
            else:
                temp = int(strsize[0])
                append(temp)
                r = 1
        if r == 1:
            if strsize[2].isdigit():
                if strsize[3].isdigit():
                    temp = int(strsize[2]+strsize[3])
                    append(temp)
                else:
                    temp = int(strsize[2])
                    append(temp)
        if r == 2:
            if strsize[3].isdigit():
                if strsize[4].isdigit():
                    temp = int(strsize[3]+strsize[4])
                    append(temp)
                else:
                    temp = int(strsize[3])
                    append(temp)
    except IOError: #If there is no file at all
        print "Cannot load puzzle "+fname
        sleep(2.5)
        sysexit()
    return size, puzzle.name #Return Puzzle size and filename

def PuzzleChecker(filledlist, winlist, puznum, screen, bgc=(255, 255, 255)):
    """Checks whether all required squares are filled and
    no other square is filled"""
    ## Tests if the correct squares are filled ##
    if filledlist == winlist:
        l = load()
        blit = screen.blit
        join = path.join
        solution = l.data(join("solutions", "pz"+str(puznum)+".png"), "img")
        screenrect = screen.get_rect()
        text = l.data("EHSMB.TTF", "font", fontsize=35)
        soltext = text("Solved!", True, (50, 50, 50))
        soltextrect = soltext.get_rect()
        soltextrect = soltextrect.move(screenrect.centerx-soltext.get_width()/2, screenrect.centery-solution.get_height()/2-50)
        solutionrect = solution.get_rect()
        solutionrect.centerx = screenrect.centerx
        solutionrect.centery = screenrect.centery
        rtrntext = text("Returning to menu...", True, (50, 50, 50))
        rtrntextrect = rtrntext.get_rect()
        rtrntextrect = rtrntextrect.move(screenrect.centerx-rtrntext.get_width()/2, screenrect.centery+solution.get_height()/2+50)
        screen.fill(bgc)
        blit(soltext, soltextrect)
        blit(solution, solutionrect)
        blit(rtrntext, rtrntextrect)
        return 0 #Quit loop
    return 1 #Continue loop

def MouseClicks(collisionrects, screen, button, filled, bgc=(255, 255, 255), sq=0):
    """Handles mouse clicks"""
    i = 1
    mpos = mouse.get_pos()
    count = filled.count
    sort = filled.sort
    if button == 1: #If the left mouse button was pressed
        append = filled.append
        for sqrect in collisionrects: #Test each rectangle
            if sqrect.collidepoint(mpos): #If there is collision with the mouse pointer
                if count(i) == 0:
                    append(i)
                    sort()
                screen.fill((0, 0, 0), sqrect)
            i += 1
    else:
        remove = filled.remove
        for sqrect in collisionrects:
            if sqrect.collidepoint(mpos):
                if count(i):
                    remove(i)
                    sort()
                screen.fill(bgc, sqrect)
                screen.blit(sq, sqrect)
            i += 1
    return filled

def DrawClues(size, screen, cluepic, puzfile):
    """size: how many cluepics, screen: for blitting,
    cluepic: for background, puzfile: for checking the clues
    This function draws the clues and also creates winlist for PuzzleChecker() """
    i, x, y = 0, 110, 44 #Top
    blit = screen.blit
    while i < size[0]: #While i is less than width: The top clue pictures
        cluerect = Rect(x, y, 22, 88)
        blit(cluepic[0], cluerect)
        x += 22
        i += 1
    i, x, y = 0, 22, 132 #Reset for left side
    while i < size[1]: #While i is less than height: The left clue pictures
        cluerect = Rect(x, y, 88, 22)
        blit(cluepic[1], cluerect)
        y += 22
        i += 1
    # Create lists for clue numbers from puzfile #
    i = 0
    with open(puzfile, "r") as puzzle:
        readline = puzzle.readline
        read = puzzle.read
        seek = puzzle.seek
        sizerow = len(readline())+1
        leftlinelen = len(readline())+1
        toplinelen = len(readline())+1
        leftline = [] #Left clues
        topline = [] #Top clues
        winlinelen = len(readline())
        winline = [] #Needed filled squares for winning
        name = readline()
        col = 1 #Column where the puzzle number goes
        append = leftline.append
        while i < leftlinelen-2:
            seek(sizerow+i, SEEK_SET)
            clue = read(1)
            if clue == ".": #If dot then the next number will be in the next row
                col = 1
            elif clue == ",": #If point then the next number will be in the next column
                col += 1
            else:
                clue2 = read(1)
                if clue2.isdigit():
                    append((int(clue+clue2), col))
                    i += 1
                else:
                    append((int(clue), col))
            i += 1
        i = 0
        col = 1
        append = topline.append
        while i < toplinelen-2: #Look at first loop
            seek(sizerow+leftlinelen+i, SEEK_SET)
            clue = read(1)
            if clue == ".":
                col = 1
            elif clue == ",":
                col = 2
            else:
                clue2 = read(1)
                if clue2.isdigit():
                    append((int(clue+clue2), col))
                    i += 1
                else:
                    append((int(clue), col))
            i += 1
        i = 0
        append = winline.append
        ## Create winlist ##
        while i < winlinelen-1: #Mostly the same
            seek(sizerow+leftlinelen+toplinelen+i, SEEK_SET)
            winnum = read(1)
            if winnum == ".":
                pass
            else:
                winnum2 = read(1)
                if winnum2.isdigit(): #Check whether there are two numbers
                    winnum3 = read(1)
                    if winnum3.isdigit(): #Check whether there are three numbers(can't be higher than three because the biggest puzzle now is 31x30)
                        append(int(winnum+winnum2+winnum3))
                        i += 2
                    else:
                        append(int(winnum+winnum2))
                        i += 1
                else:
                    append(int(winnum))
            i += 1
    ########################
    ## PUZZLE FILE CLOSED ##
    ########################
    # Draw clue numbers from the lists #
    join = path.join
    i, x, y, leftlinelen, spacing, spacings = 0, 99, 135, len(leftline), 15, []
    text = font.Font(join("data", "font", "freesansbold.ttf"), 15)
    for numcol in leftline:
        numtext = text.render(str(numcol[0]), True, (50, 50, 50))
        numtextrect = numtext.get_rect()
        if i < leftlinelen-1:
            nextnum = leftline[i+1]
        if nextnum[1] > 1:
            if numcol[0] < 10:
                numtextrect = numtextrect.move(x, y)
            else:
                numtextrect = numtextrect.move(x-8, y)
            blit(numtext, numtextrect)
            if numcol[0] < 10:
                spacing = 15
            else:
                spacing = 22
            x -= spacing
            spacings.append(spacing)
        else:
            if numcol[0] < 10:
                numtextrect = numtextrect.move(x, y)
            elif numcol[0] == 11:
                numtextrect = numtextrect.move(x-7, y)
            else:
                numtextrect = numtextrect.move(x-9, y)
            blit(numtext, numtextrect)
            if numcol[1] != 1:
                for sp in spacings:
                    x += sp
                spacings = []
            y += 22
        i += 1
    # Reset and same thing for topline #
    i, x, y, toplinelen, spacing, spacings = 0, 117, 117, len(topline), 17, []
    for numcol in topline:
        numtext = text.render(str(numcol[0]), True, (50, 50, 50))
        numtextrect = numtext.get_rect()
        if i < toplinelen-1:
            nextnum = topline[i+1]
        if nextnum[1] > 1:
            if numcol[0] < 10:
                numtextrect = numtextrect.move(x, y)
            else:
                numtextrect = numtextrect.move(x-8, y)
            blit(numtext, numtextrect)
            y -= spacing
            spacings.append(spacing)
        else:
            if numcol[0] < 10:
                numtextrect = numtextrect.move(x, y)
            else:
                numtextrect = numtextrect.move(x-5, y)
            blit(numtext, numtextrect)
            if numcol[1] != 1:
                for sp in spacings:
                    y += sp
                spacings = []
            x += 22
        i += 1
    # Draw puzzle name on the screen #
    text = font.Font(join("data", "font", "EHSMB.TTF"), 27)
    nametext = text.render(name, True, (30, 30, 30))
    nametextrect = nametext.get_rect()
    nametextrect.centerx = 110+(size[0]*22/2)
    nametextrect.centery = 22
    blit(nametext, nametextrect)
    return winline

#####################
## Extra functions ##
def wait(time):
    sleep(time)

def quitprogram():
    #Might be some more things here
    sysexit()

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    wait(1.5)
    quitprogram()
