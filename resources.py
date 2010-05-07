from pygame import image#, mixer
from os import path
from sys import exit as sysexit
from time import sleep

def load_img(name, alpha=0):
    join = path.join
    load = image.load
    try:
        imgname = join("data", "img", name)
        img = load(imgname)
        if alpha == 1:
            img.convert_alpha()
        else:
            img.convert()
    except:
        print "Can't load image: "+imgname
        sleep(1.5)
        sysexit()
    return img

##def load_snd(name):
##    join = path.join
##    sound = mixer.Sound
##    #try:
##    sndname = join("data", "snd", name)
##    print "Loading "+sndname
##    snd = sound(sndname)
##    #except:
##    #    print "Can't load sound: "+sndname
##    #    sleep(1.5)
##    #    sysexit()
##    return snd

if __name__ == "__main__":
    print "Start the game from Hanjie.py"
    sleep(1.5)
    sysexit()