#!/usr/bin/env python

"""
    Metronome for the Digitech Whammy
"""

import sys
import os
import pygame
import pygame.midi
from pygame.locals import *
from whammy import *
from time import *

def start(beats, noteval, bpm):
    pygame.init()
    pygame.midi.init()

    port = pygame.midi.get_default_output_id()

    whammy = WhammyTime(port, beats, noteval, bpm)
    
    for bar in range(0, 20):
        whammy.metronome(bar, float(1) / noteval)

    sleep(10)

    whammy.abort()
    whammy.close()
    pygame.midi.quit()

def stop():
    WhammyFilter.setMute(whammy, pygame.midi.time() + 1000)       

if __name__ == '__main__':
    start(4,4,100)

