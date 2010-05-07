## Imports ##
from os import path, SEEK_SET
from sys import exit as sysexit
from pygame import Rect, mouse, Surface, font
from time import sleep

def Make_sqrect(size, coll=0): #Makes the rectangles for all squares that are created, mainly for collision checking
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
    ## Loads numbers to be hints, in the file: two first rows for numbers, first for ones on left side and second on numbers on top, and then rest of
    ## the file will be for PuzzleChecker ##
    size = [] #Empty list for x*y in the puzzle file e. g. 5*5 = [5, 5]
    join = path.join
    try:
        with open(join("data", "puzzles", fname), "r") as puzzle: #Open puzzle file
            strsize = [] #Empty list for raw data from the file
            sizerow = len(puzzle.readline())
            r = 0 #Counter
            append = strsize.append
            read = puzzle.read
            puzzle.seek(0, SEEK_SET)
            while r < sizerow: #Runs five times
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

def PuzzleChecker(filledlist, winlist, puznum, screen, bgc=(255, 255, 255)): #Checks whether all required squares are filled and no other square
    ## Tests if the correct squares are filled ##
    if filledlist == winlist:
        from resources import load_img
        blit = screen.blit
        join = path.join
        solution = load_img(join("solutions", "pz"+str(puznum)+".png"), 1)
        screenrect = screen.get_rect()
        text = font.Font(join("data", "font", "EHSMB.TTF"), 35) #Change to a font from file e. g. pygame.font.Font(Something)
        soltext = text.render("Solved!", True, (50, 50, 50)) #Change font to surface
        soltextrect = soltext.get_rect()
        soltextrect = soltextrect.move(screenrect.centerx-soltext.get_width()/2, screenrect.centery-solution.get_height()/2-50)
        solutionrect = solution.get_rect()
        solutionrect.centerx = screenrect.centerx
        solutionrect.centery = screenrect.centery
        rtrntext = text.render("Returning to menu...", True, (50, 50, 50)) #Change font to surface
        rtrntextrect = rtrntext.get_rect()
        rtrntextrect = rtrntextrect.move(screenrect.centerx-rtrntext.get_width()/2, screenrect.centery+solution.get_height()/2+50)
        screen.fill(bgc)
        blit(soltext, soltextrect)
        blit(solution, solutionrect)
        blit(rtrntext, rtrntextrect)
        return 0
    return 1

def MouseClicks(collisionrects, screen, button, filled, bgc=(255, 255, 255), sq=0):
    i = 1 #Counter
    mpos = mouse.get_pos() #Gets the mouse position
    count = filled.count
    sort = filled.sort
    if button == 1: # If the left mouse button was pressed
        append = filled.append
        for sqrect in collisionrects: #Test each rectangle
            if sqrect.collidepoint(mpos): #If there is collision with the mouse pointer
                if count(i) == 0:
                    append(i)
                    sort()
                screen.fill((0, 0, 0), sqrect)
            i += 1 #Add one to the counter
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
    return filled #Change to filledlist

def DrawClues(size, screen, cluepic, puzfile): #size: how many cluepics, screen: for blitting, cluepic: for background, puzfile: for checking the clues
    ## This function draws the clues and also creates the win list for PuzzleChecker() ##
    i, x, y = 0, 110, 44 #i is just an integer for checking if enough pictures have been drawn, x is the x-coordinate and y is y-coordinate
    blit = screen.blit
    while i < size[0]: #While i is less than width: The top clue pictures
        cluerect = Rect(x, y, 22, 88) #Create a rectangle where the picture is drawn
        blit(cluepic[0], cluerect) #Draw picture
        x += 22 #Change position
        i += 1
    i, x, y = 0, 22, 132 #Reset for left side
    while i < size[1]: #While i is less than height: The left clue pictures
        cluerect = Rect(x, y, 88, 22)
        blit(cluepic[1], cluerect)
        y += 22
        i += 1
    ## Create lists for clue numbers from puzfile ##
    i = 0
    with open(puzfile, "r") as puzzle: #Open the puzzle file and close it when everything is done
        readline = puzzle.readline
        read = puzzle.read
        seek = puzzle.seek
        sizerow = len(readline())+1 #Puzzle size, not useful here, linelength required though
        leftlinelen = len(readline())+1 #Linelength of the clues in left side
        toplinelen = len(readline())+1 #Linelength of the clues on top
        leftline = [] #Create an empty list for appending
        topline = [] #Create an empty list for appending
        winlinelen = len(readline()) #Linelength of winning rects list
        winline = [] #Create an empty list for appending
        name = readline() #Name of the puzzle
        col = 1 #Column where the puzzle number goes
        append = leftline.append
        while i < leftlinelen-2: #While we aren't in the end of the line in puzzle file
            seek(sizerow+i, SEEK_SET) #Sets the position in the file
            clue = read(1) #Reads the number, dot or point
            if clue == ".": #If dot then the next number will be in the next row
                col = 1
            elif clue == ",": #If point then the next number will be in the next column
                col += 1
            else:
                clue2 = read(1) #Checks whether the next byte is a number
                if clue2.isdigit(): #If it is then combine the first number and second number and append them and skip one byte
                    append((int(clue+clue2), col))
                    i += 1
                else: #If it isn't just append the first number
                    append((int(clue), col))
            i += 1 #Go one byte forward
        i = 0 #Reset
        col = 1 #Reset
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
        i = 0 #Reset
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
                        i += 2#Skip two next bytes
                    else:
                        append(int(winnum+winnum2))
                        i += 1
                else:
                    append(int(winnum))
            i += 1
    ########################
    ## PUZZLE FILE CLOSED ##
    ########################
    ## Draw clue numbers from the lists ##
    join = path.join
    i, x, y, leftlinelen, spacing, spacings = 0, 99, 135, len(leftline), 15, [] #Reset #Spacing of numbers: CHANGE
    text = font.Font(join("data", "font", "freesansbold.ttf"), 15) #Change to a font from file e. g. pygame.font.Font(Something)
    for numcol in leftline:
        numtext = text.render(str(numcol[0]), True, (50, 50, 50)) #Change font to surface
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
    #Reset and same thing for topline
    i, x, y, toplinelen, spacing, spacings = 0, 117, 117, len(topline), 17, [] #Reset
    for numcol in topline:
        numtext = text.render(str(numcol[0]), True, (50, 50, 50)) #Change font to surface
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
    ## Draw puzzle name on the screen ##
    text = font.Font(join("data", "font", "EHSMB.TTF"), 27) #Change to a font from file e. g. pygame.font.Font(Something)
    nametext = text.render(name, True, (30, 30, 30))
    nametextrect = nametext.get_rect()
    nametextrect.centerx = 110+(size[0]*22/2)
    nametextrect.centery = 22
    blit(nametext, nametextrect)
    return winline

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    sleep(1.5)
    sysexit()