import menu, pygame
from sys import exit as sysexit
from os import environ

def main():
    #########################
    ### Setting up pygame ###
    environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    fonts = 1
    sound = 1
    if not pygame.font:
        print "Warning, fonts disabled, game not playable"
        fonts = 0
    if not pygame.mixer:
        print "Warning, sound disabled"
        sound = 0
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Hanjie")
    pygame.display.update()
    menu.menu(screen)

if __name__ == "__main__":
    main()
    sysexit()