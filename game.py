import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 3
GAME_HEIGHT = 3

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    #pass
####   End class definitions    ####

def initialize():
    #"""Put game initialization code here"""
   
   #increase the GRID size - step3, step4
    GAME_WIDTH = 4
    GAME_HEIGHT = 4

   #Intialise and register Rock1 - step2 
    rock1 = Rock()
    GAME_BOARD.register(rock1) #step1
    GAME_BOARD.set_el(1,1,rock1) #step1

    #Intialise and register Rock2 - step2
    rock2 = Rock()
    GAME_BOARD.register(rock2)
    GAME_BOARD.set_el(2,2,rock2)

    print "The first rock is at", (rock1.x, rock1.y)
    print "The second rock is at", (rock2.x, rock2.y)
    print "Rock 1 image", rock1.IMAGE
    print "Rock 2 image", rock2.IMAGE



    #pass

