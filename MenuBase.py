import game
from sys import exit as sysexit
from pygame import font, Surface, display, mouse, Rect
from time import sleep
from random import randint

def create_menu(screen, text, menustrings): #Screen for blitting, text for the font and menustrings for the strings that are going to be written
    menubuttons = []
    append = menubuttons.append
    blit = screen.blit
    sr = screen.get_rect()
    c = -70
    for strs in menustrings:
        t = text.render(strs, True, (50, 50, 50))
        tr = t.get_rect()
        tr = tr.move(sr.centerx-t.get_width()/2, sr.centery-t.get_height()/2+c)
        blit(t, tr)
        append(tr)
        c += 70
    display.update()
    return menubuttons

def puzzleselect():
    pass

def randompuzzle(solved, allpuz, menubg, screen, text, end): # Remove allpuz, menubg, text, end ## MAY CHANGE ##
    blit = screen.blit
    screct = screen.get_rect()
    ## REMOVE THIS ##
    if solved == allpuz:
        blit(menubg, screct)
        testtext = text.render("All puzzles solved.", True, (50, 50, 50))
        testtrect = testtext.get_rect()
        testtrect.centerx, testtrect.centery = screct.centerx, screct.centery
        blit(testtext, testtrect)
        display.update()
        sleep(1.5)
    ## END ##
    else:
        puzzlenum = randint(1, end)
        count = solved.count
        while count(puzzlenum) == 1:
            puzzlenum = randint(1, end)
        puzzlenum, solved = game.game(puzzlenum, screen, solved)
        ## REMOVE THIS ##
        if solved == allpuz:
            blit(menubg, screct)
            testtext = text.render("All puzzles solved.", True, (50, 50, 50))
            testtrect = testtext.get_rect()
            testtrect.centerx, testtrect.centery = screct.centerx, screct.centery
            blit(testtext, testtrect)
            display.update()
            sleep(1.5)
        ## END ##
    return 1

def MouseClicks(buttons): #Handles mouse clicks
    mpos = mouse.get_pos()
    i = 1
    for rect in buttons:
        if rect.collidepoint(mpos):
            a = i
        i += 1
    try:
        return a
    except UnboundLocalError:
        return 0

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    sleep(1.5)
    sysexit()