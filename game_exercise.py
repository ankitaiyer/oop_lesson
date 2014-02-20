


# ############################## CommentedCode###############

#     for rock in rocks:
#         print rock

# #step 9 Instance Methods
#     print (PLAYER.x, PLAYER.y)
#     print PLAYER.next_pos("up")
#     print (PLAYER.x, PLAYER.y)


#     #step 7 - Keyboard Interaction
#     def keyboard_handler():
#         if KEYBOARD[key.UP]:
#             GAME_BOARD.draw_msg("you pressed UP")
#             next_y = PLAYER.y - 1 #step8
#             GAME_BOARD.del_el(PLAYER.x, PLAYER.y) #step8
#             GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER) #step8
#         elif KEYBOARD[key.DOWN]:
#             GAME_BOARD.draw_msg("You pressed DOWN")
#             next_y = PLAYER.y + 1
#             GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
#             GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
#         elif KEYBOARD[key.LEFT]:
#             GAME_BOARD.draw_msg("You pressed LEFT")
#             next_x = PLAYER.x - 1
#             GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
#             GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
#         elif KEYBOARD[key.RIGHT]:
#             GAME_BOARD.draw_msg("You pressed RIGHT")
#             next_x = PLAYER.x + 1
#             GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
#             GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
#    #Intialise and register Rock1 - step2 
#     rock1 = Rock()
#     GAME_BOARD.register(rock1) #step1
#     GAME_BOARD.set_el(1,1,rock1) #step1

#     #Intialise and register Rock2 - step2
#     rock2 = Rock()
#     GAME_BOARD.register(rock2)
#     GAME_BOARD.set_el(2,2,rock2)

#     print "The first rock is at", (rock1.x, rock1.y)
#     print "The second rock is at", (rock2.x, rock2.y)
#     print "Rock 1 image", rock1.IMAGE
#     print "Rock 2 image", rock2.IMAGE


# ####################

# class BlueGem(GameElement):
#     IMAGE = "BlueGem"
#     SOLID = False
    

#     def interact(self,player):
#         player.inventory.append(self)
#         gem_counter =  1
#         GAME_BOARD.draw_msg("You have just acquired a gem! You now have %d items."%(len(player.inventory)))
#         #if GEM in player.inventory:
#         for index in range(len(player.inventory)):
#             if type(player.inventory[index]) == OrangeGem or type(player.inventory[index])== GreenGem:
#                 gem_counter = gem_counter + 1
#                 if gem_counter == 3:
#                      # when all 3 gems are found a girl turns into a princess
#                     player.IMAGE = "Princess"
#                     GAME_BOARD.register(player)
#                     GAME_BOARD.set_el(player.x,player.y,player)
#                     GAME_BOARD.draw_msg("Wow! I am a princess now!")
                         

# class GreenGem(GameElement):
#     IMAGE = "GreenGem"
#     SOLID = False

#     def interact(self,player):
#         player.inventory.append(self)
#         gem_counter = 1
#         GAME_BOARD.draw_msg("You have just acquired a gem! You now have %d items."%(len(player.inventory)))
#         for index in range(len(player.inventory)):
#             if type(player.inventory[index]) == OrangeGem or type(player.inventory[index]) == BlueGem:
#                 gem_counter = gem_counter + 1
#                 if gem_counter == 3:
#                     # when all 3 gems are found a girl turns into a princess
#                     player.IMAGE = "Princess"
#                     GAME_BOARD.register(player)
#                     GAME_BOARD.set_el(player.x,player.y,player)
#                     GAME_BOARD.draw_msg("Wow! I am a princess now!")

# class OrangeGem(GameElement):
#     IMAGE = "OrangeGem"
#     SOLID = False

#     def interact(self,player):
#         player.inventory.append(self)
#         gem_counter = 1
#         GAME_BOARD.draw_msg("You have just acquired a gem! You now have %d items."%(len(player.inventory)))
#         for index in range(len(player.inventory)):
#             if type(player.inventory[index]) == GreenGem or type(player.inventory[index]) == BlueGem:
#                 gem_counter = gem_counter + 1
#                 if gem_counter == 3:
#                     # when all 3 gems are found a girl turns into a princess
#                     player.IMAGE = "Princess"
#                     GAME_BOARD.register(player)
#                     GAME_BOARD.set_el(player.x,player.y,player)
#                     GAME_BOARD.draw_msg("Wow! I am a princess now!")
                    
# #########################################

#     pass

