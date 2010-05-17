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

from sys import exit as sysexit
from os import environ
import pygame, menu

def main():
    environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    if not pygame.font:
        print "Warning, fonts disabled, game not playable"
        pygame.time.delay(1500)
        sysexit()
    if not pygame.mixer:
        print "Warning, sound disabled"
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Hanjie")
    pygame.display.update()
    menu.menu(screen)

if __name__ == "__main__":
    main()
    sysexit()
