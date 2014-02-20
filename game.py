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
GAME_WIDTH = 7
GAME_HEIGHT = 7

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement): # step5
    IMAGE = "Girl"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []
        self.gem_counter = 0

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
    SOLID = False
       

    def __init__(self, IMAGE, gem_type1, gem_type2):
        self.IMAGE = IMAGE
        self.gem_type1 = gem_type1
        self.gem_type2 = gem_type2
        

    def interact(self,player):
        player.inventory.append(self)
        player.gem_counter+=1
        print player.gem_counter
        GAME_BOARD.draw_msg("You have just acquired a gem! You now have %d items."%(len(player.inventory)))
        if player.gem_counter == 3:
            # when all 3 gems are found a girl turns into a princess
            player.IMAGE = "Princess"
            GAME_BOARD.register(player)
            GAME_BOARD.set_el(player.x,player.y,player)
            GAME_BOARD.draw_msg("Wow! I am a princess now!")


class DoorClosed(GameElement):
    IMAGE = "DoorClosed"
    SOLID = True

    def interact(self,player):
        #if Key in player.inventory:
        for index in range(len(player.inventory)):
            if type(player.inventory[index]) == Key:
                self.SOLID = False
                del player.inventory[index]
                player.inventory.append(self)
                GAME_BOARD.draw_msg("You have used your key to acquire a door! You now have %d items." %(len(player.inventory)))
                break
    
class Key(GameElement):
    IMAGE = "Key"
    SOLID = False

    def interact(self,player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You have just acquired a key! You now have %d items." %(len(player.inventory)))


class Wall(GameElement):
    IMAGE = "Wall"
    SOLID = True

class ShortTree(GameElement):
    IMAGE = "ShortTree"
    SOLID = True   

    def interact(self,player):
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)

class Chest(GameElement):
    IMAGE = "Chest"
    SOLID = True
    chest_collection = []

    def interact(self,player):
        if  player.inventory == []:
            GAME_BOARD.draw_msg("There is nothing to store")
        else:
            self.SOLID = False
            self.chest_collection = player.inventory
            print "Chest Inventory is " , self.chest_collection
            player.inventory = []
            GAME_BOARD.draw_msg("Transfered everything from Player's inventory to Chest. Chest is in secret place now")

class WaterBlock(GameElement)               :
    IMAGE = "WaterBlock"
    SOLID = True


####   End class definitions    ####
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
       

        if (0 <= next_x < GAME_WIDTH) and (0 <= next_y < GAME_HEIGHT): 
            existing_el = GAME_BOARD.get_el(next_x, next_y)
            
            if existing_el:
                existing_el.interact(PLAYER)
            
            if existing_el is None or not existing_el.SOLID:
                GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
                GAME_BOARD.set_el(next_x,next_y,PLAYER)
            elif type(existing_el) == DoorClosed:
                GAME_BOARD.draw_msg("You just hit a closed door. You need a key to open and acquire this door.")    
            elif type(existing_el) == ShortTree:
                GAME_BOARD.draw_msg("You hit the Tree of Invisibility! Back away to reappear!") 
            elif type(existing_el) == Chest and PLAYER.inventory == []:
                GAME_BOARD.draw_msg("There is nothing to store")            
            else:
                new_message = "I can't move " + direction + " I see something SOLID"
                GAME_BOARD.draw_msg(new_message)
        else:
            GAME_BOARD.draw_msg("Reached boundries")

def initialize():
    #"""Put game initialization code here"""

    rock_positions = [(2,1),(1,2),(2,2)]
    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0],pos[1],rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    #Added character - GIRL for step5    
    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(1,5,PLAYER)

    GAME_BOARD.draw_msg("Collect all 3 gems and see the magic!") # step6

    # Adding GEMS
    bluegem = Gem("BlueGem", "OrangeGem", "GreenGem")
    GAME_BOARD.register(bluegem)
    GAME_BOARD.set_el(1,0,bluegem)
    
    greengem = Gem("GreenGem", "OrangeGem", "BlueGem")
    GAME_BOARD.register(greengem)
    GAME_BOARD.set_el(3,0,greengem)

    orangegem = Gem("OrangeGem", "GreenGem", "BlueGem")
    GAME_BOARD.register(orangegem)
    GAME_BOARD.set_el(5,0,orangegem)

    doorclosed = DoorClosed()
    GAME_BOARD.register(doorclosed)
    GAME_BOARD.set_el(3,3,doorclosed)

    key1 = Key()
    GAME_BOARD.register(key1)
    GAME_BOARD.set_el(6,6,key1)

    wall_positions = [(0,3),(1,3),(2,3),(4,3),(5,3),(6,3),]
    walls = []
    for pos in wall_positions:
        wall = Wall()
        GAME_BOARD.register(wall)
        GAME_BOARD.set_el(pos[0],pos[1],wall)
        walls.append(wall)

    shorttree = ShortTree()
    GAME_BOARD.register(shorttree)
    GAME_BOARD.set_el(3,5,shorttree)

    chest = Chest()
    GAME_BOARD.register(chest)
    GAME_BOARD.set_el(0,5,chest)
