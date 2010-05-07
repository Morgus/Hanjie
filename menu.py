from MenuBase import *
from os import path
from resources import load_img
from sys import exit as sysexit
from pygame import Surface, display, event, font
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from time import sleep
from cPickle import load
##from random import randint #Random not needed when menu is fully created

def menu(screen):
    r = 1
    init = 1
    join = path.join
    blit = screen.blit
    #######################
    ## Loading resources ##
    text = font.Font(join("data", "font", "EHSMB.TTF"), 60)
    menubg = load_img("menubg.png")
    ## Menu loop ##
    ## Testing, might be part of the real menu ##
    allpuzzles = []
    append = allpuzzles.append
    with open(join("data", "puzzles", "_pzcount")) as pzcount:
        num = int(pzcount.readline())
        i = 1
        while i <= num:
            append(i)
            i += 1
    with open("save", "r") as save:
        try:
            solved = load(save)
        except EOFError:
            solved = []
    puzzlenum = 0
    menuType = "main"
    ## End ##
    while r:
        if init == 1:
            blit(menubg, screen.get_rect())
            menubuttons = create_menu(screen, text, ["Play random puzzle", "Puzzle select", "Exit"]) #There may be some more return values for this sometime
            init = 0
        for ev in event.get():
            if ev.type == QUIT: sysexit()
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    if menuType == "main": # Testing #
                        ##menuButtonClicked = 0
                        menuButtonClicked = MouseClicks(menubuttons)
                        if menuButtonClicked == 1:
                            init = randompuzzle(solved, allpuzzles, menubg, screen, text, num)
                        elif menuButtonClicked == 2:
                            print "Function not yet implemented" #CHANGE
                            menuType = "select" #CHANGE
                        elif menuButtonClicked == 3:
                            r = 0
                        elif menuButtonClicked == 0:
                            print "Didn't click anything!" #REMOVE
                    elif menuType == "select": # Testing #
                        ##menuButtonClicked = 0 # Testing #
                        print "I'm in another loop!" # Testing #
                        menuType = "main" # Testing #


if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    sleep(1.5)
    sysexit()