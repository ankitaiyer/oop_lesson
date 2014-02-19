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
#increase the GRID size - step3, step4
GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True
class Character(GameElement): # step5
    IMAGE = "Girl"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    #step 9 adding instance method
    def next_pos(self, direction):
        if direction == 'up':
            return(self.x, self.y-1)
        elif direction == 'down':
            return (self.x, self.y+1)
        elif direction == 'left':
            return(self.x-1, self.y)
        elif direction == 'right':
            return (self.x+1, self.y)

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self,player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("you just acquired a gem! you have %d items!"%(len(player.inventory)))

    
####   End class definitions    ####

def initialize():
    #"""Put game initialization code here"""
 
    rock_positions = [(2,1),(1,2),(3,2),(2,3)]
    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0],pos[1],rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    # for rock in rocks:
    #     print rock

    #Added character - GIRL for step5    
    global PLAYER
    PLAYER = Character()
    print PLAYER.inventory
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2,2,PLAYER)
    #print PLAYER

    GAME_BOARD.draw_msg("This game is wicket awesome") # step6

    # Added GEM - step12
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3,1,gem)

    #step 9
def keyboard_handler():
    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
        GAME_BOARD.draw_msg("Moving up!")
    if KEYBOARD[key.DOWN]:
        direction = "down"  
        GAME_BOARD.draw_msg("Moving Down!")  
    if KEYBOARD[key.LEFT]:
        direction = "left"
        GAME_BOARD.draw_msg("Moving Left!")
    if KEYBOARD[key.RIGHT]:
        direction = "right"
        GAME_BOARD.draw_msg("Moving Right!")

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        if (0 <= next_x <= GAME_WIDTH) and (0 <= next_y <= GAME_HEIGHT): 
            existing_el = GAME_BOARD.get_el(next_x, next_y)
            if existing_el:
                existing_el.interact(PLAYER)

            if existing_el is None or not existing_el.SOLID:
                GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
                GAME_BOARD.set_el(next_x,next_y,PLAYER)
            else:
                new_message = "can't move " + direction
                GAME_BOARD.draw_msg(new_message)
        else:
            GAME_BOARD.draw_msg("Reached boundries")










############################### CommentedCode###############
# #step 9 Instance Methods
#     print (PLAYER.x, PLAYER.y)
#     print PLAYER.next_pos("up")
#     print (PLAYER.x, PLAYER.y)


    # #step 7 - Keyboard Interaction
    # def keyboard_handler():
    #     if KEYBOARD[key.UP]:
    #         GAME_BOARD.draw_msg("you pressed UP")
    #         next_y = PLAYER.y - 1 #step8
    #         GAME_BOARD.del_el(PLAYER.x, PLAYER.y) #step8
    #         GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER) #step8
    #     elif KEYBOARD[key.DOWN]:
    #         GAME_BOARD.draw_msg("You pressed DOWN")
    #         next_y = PLAYER.y + 1
    #         GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #         GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
    #     elif KEYBOARD[key.LEFT]:
    #         GAME_BOARD.draw_msg("You pressed LEFT")
    #         next_x = PLAYER.x - 1
    #         GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #         GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
    #     elif KEYBOARD[key.RIGHT]:
    #         GAME_BOARD.draw_msg("You pressed RIGHT")
    #         next_x = PLAYER.x + 1
    #         GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    #         GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
   # #Intialise and register Rock1 - step2 
   #  rock1 = Rock()
   #  GAME_BOARD.register(rock1) #step1
   #  GAME_BOARD.set_el(1,1,rock1) #step1

   #  #Intialise and register Rock2 - step2
   #  rock2 = Rock()
   #  GAME_BOARD.register(rock2)
   #  GAME_BOARD.set_el(2,2,rock2)

   #  print "The first rock is at", (rock1.x, rock1.y)
   #  print "The second rock is at", (rock2.x, rock2.y)
   #  print "Rock 1 image", rock1.IMAGE
   #  print "Rock 2 image", rock2.IMAGE



    #pass

