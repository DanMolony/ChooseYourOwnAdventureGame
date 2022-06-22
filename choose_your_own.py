# This is the start of the Portfolio Project
# Fingers crossed.

from msilib.schema import Class


from final_project_pkg import choose_your_own_directions
from final_project_pkg.king_app import app
from final_project_pkg.bat_app import bat_app



import time


# Enemy variables
seaweed = "Seaweed Creature"
slime = "Slime Creature"
skeleton = "Skeleton"
giant_fish = "Giant Fish"

#death count after failed encounters
death_count = 0

# Dictionary of all enemy types, key is their names and value is their
enemies = {seaweed: "A terrifying monster from the sea made entirely of seaweed",
           slime: "A most foul creature made entirely of green goo ",
           skeleton: "A horrific shambling of clanking bones ",
           giant_fish: "A giant fish with horrible staring eyes"}
# Makes a list of all key value pairs
enemy_pairs = list(enemies.items())


# the following loop starts the game
while True:

    print("\nYou awaken underneath a tree in a forest, confused, hungry, and scared...\n ")
    time.sleep(3)
    to_start = input(
        "\nType STAND to rise up and start your adventure!, or... \nType SLEEP to call it a day and go back to sleep under the tree, \n")
    if to_start.upper() == "STAND":
        print("\nOnward!\n")
        time.sleep(3)
        break
    elif to_start.upper() == "SLEEP":
        print("Goodnight!")
        exit()

    elif to_start != "STAND" or "SLEEP":
        print("\nI don't know those words...\n")


# Short Introduction
print("\nNow that you're standing you feel a little better, but you quickly realize you forgot your name.\n")
time.sleep(3)
character_name = input(
    "\nOh wait, you remember your name! Your name is...\nPlease ENTER your name...\n")
print("\nYes that's right you are ", character_name.capitalize(), "!\n")
time.sleep(3)
print("\nWith your name all sorted out, you now wander over to an old looking sign,\nthe sign points in two diferent directions\n")
time.sleep(3)


# This chunk is the main game, 2 first options and then options in several battles,

while True:
    print("\nDo you want to follow the path LEFT towards a distant castle on an island, or...\nDo you want to follow the path RIGHT towards a dark cave.\n")
    story_choice = input("\nDo you want to go LEFT or RIGHT. \n")
    left = "LEFT"
    right = "RIGHT"

    
    
    
    # The left story is the path to the castle and begins here.
    
    if story_choice.upper() == left:
        print("\nYou decide to go left towards the castle on the island.\n")
        time.sleep(3)
        print("\nWhile walking on the beaches edge you see a boat in the distance, perfect to get to the island...\n")
        time.sleep(3)
        print("\nWhen suddenly you are attacked by a...\n")
        time.sleep(3)
        print(enemy_pairs[0])
        time.sleep(4)
        
      
        choose_your_own_directions.directions()   # Explains to the user what is going to happen
        print("\nThe " + seaweed + " rushes towards you\n")
        time.sleep(3)

        #first battlebelow
        battle_choice = input("\nDo you POKE the Seaweed Creature with a sharp stick you find on the ground or....\nDo you PUSH the Seaweed Creature back into it's watery home \n")
        

        if battle_choice.upper() == "POKE":
            print("\nYou POKE the", seaweed)
            time.sleep(3)
            print("\n...\n")
            time.sleep(3)
            print("\nThe", seaweed, "grabs the stick from your hands, and bops you on the head cracking your skull\n ")
            time.sleep(3)
            death_count = death_count + 1
            print("\nYou have died ", death_count, "times \n")
            # function below takes player to beginning of game, but i want it to take it to begining of battle.
            
            choose_your_own_directions.redo()
            

        elif battle_choice.upper() == "PUSH":
            print("\nYou PUSH the", seaweed)
            time.sleep(3)
            print("\n...\n")
            time.sleep(3)
            print("\nThe ", seaweed, "falls backwards and dissappers into the murky water\n")
            time.sleep(3)
            
            
           
           
           
           
            #post battle setting up next battle
            print("\nHoorah, ", character_name.capitalize(),"You defeated the", enemy_pairs[0])
            time.sleep(3)
            print("\nYou hop in the boat and set sail, almost to the castle when...\n")
            time.sleep(4)
            print("\nYou see a ", enemy_pairs[3], ", And it's coming right towards you!\n")
            time.sleep(5)
            battle_choice = input("\nDo you STAB the Giant Fish with a harpoon with a rope on it  or....\nDo you SLAP the Giant Fish so hard, its ancestors feel it\n")

            if battle_choice.upper() == "SLAP":
                print("\nYou SLAP the", giant_fish)
                time.sleep(3)
                print("\n...\n")
                time.sleep(3)
                print("\nThe", giant_fish,"Feels absolutley no pain and gobbles you up.\n")
                time.sleep(3)
                death_count = death_count + 1
                print("\nYou have died ", death_count, "times \n")
                choose_your_own_directions.redo()
            #Second Battle
            elif battle_choice.upper() == "STAB":
                print("\nYou STAB the", giant_fish)
                time.sleep(3)
                print("\n...\n")
                time.sleep(3)
                print("\nThe ", giant_fish," howls, you stabbed it!, And it starts to pull the boat towards the island!\n")
                time.sleep(3)
                print("\nYou've made it to Castle de Island ", character_name.capitalize(), ", But who's castle is this anyway?\n")
                time.sleep(3)
                print("\nYou hear footsteps clomping in the castle's great hall.\n")
                time.sleep(3)
                print("\nNo...\n")
                time.sleep(3)
                print("\nit can't be!\n")
                time.sleep(3)
                print("\nIt's none other than the dreaded King Banking App! and He's forcing you to register yourself in his Banking App and Donate Money to him!\n")
                time.sleep(4)
                choose_your_own_directions.king_directions()
                app()
                print("You died ", death_count, "times")
                #This ends the game and is the end of the LEFT portion of the story
                choose_your_own_directions.game_end()
            else: 
                print("\nPLESE PICK ONE OF THE TWO OPTIONS :)\n")
        else:
            print("\nPLEASE PICK ONE OF THE TWO OPTIONS :)\n")
    #Below begins the RIGHT section of the game
    elif story_choice.upper() == right:
        print("\nYou decide to follow the path RIGHT towards the dark cave\n")
        time.sleep(3)
        print("\nThankfully you brought a torch that lights the darkness\n")
        time.sleep(3)
        print("\nAll is quiet until suddenly, you are attacked by a...\n")
        time.sleep(3)
        print(enemy_pairs[2])
        time.sleep(4)

    # Explains to the user what is going to happen
        choose_your_own_directions.directions()

        print("\nThe " + skeleton + " rushes towards you\n")
        time.sleep(3)
        battle_choice = input("\nDo you BONK the Skeleton with a big rock or....\nDo you HUG the skeleton, to show him you care. \n")
        #Beginning of the second battle
        if battle_choice.upper() == "BONK":
            print("\nYou BONK the", skeleton)
            time.sleep(3)
            print("\n...\n")
            time.sleep(3)
            print("\nThe", skeleton, " Becomes furious and bonks you back with a bigger rock\n ")
            time.sleep(3)
            death_count = death_count + 1
            print("\nYou have died ", death_count, "times \n")
            

            choose_your_own_directions.redo()
        elif battle_choice.upper() == "HUG":
            print("\nYou HUG the ", skeleton)
            time.sleep(3)
            print("\n...\n")
            time.sleep(3)
            print("\nThe ", skeleton, " hesitates, but then hugs you back \n")
            time.sleep(3)


        #post battle
            print("\nHoorah, ", character_name.capitalize(),"You defeated the", enemy_pairs[2])
            time.sleep(4)
            print("\nYou continue down the dark cave towards a minecart and hop in.")
            time.sleep(4)
            print("\nNot too long in the walls begin to turn green with slime")
            time.sleep(4)
            print("\nWhen suddenly you see a ", enemy_pairs[1], "ooze from the ceiling and fall in the minecart behind you\n")
            time.sleep(4)
            battle_choice = input("\nDo you DETACH the minecart from the one with the Goo man in it  or....\nDo you THROW a stick of dynamite you found on the floor.\n")
            
            if battle_choice.upper() == "THROW": #battle 2
                print("\nYou Throw the dynamite at the", slime)
                time.sleep(3)
                print("\n...\n")
                time.sleep(3)
                print("\nThe", slime," absorbs the dynamite and then jumps and ABSORBS YOU!,\n", character_name.upper())
                time.sleep(4)
                death_count = death_count + 1
                print("\nYou have died ", death_count, "times \n")
                choose_your_own_directions.redo()

            elif battle_choice.upper() == "DETACH":
                print("\nYou DETACH the minecart with the ", slime, "in it.")
                time.sleep(3)
                print("\n...\n")
                time.sleep(3)
                print("\nThe minecart is released! and the ", slime," begins to fall behind back into the darkness.\n")
                time.sleep(4)
                print("\nYou've made it to the end of the dark cave ", character_name.capitalize(), "although its a dead end.\n")
                time.sleep(4)
                print("\nThe narrow cave has expanded to a larger room, almost like a boss lives here.\n")
                time.sleep(3)
                print("\nRocks begin to fall from the ceiling\n")
                time.sleep(3)
                print("\nOH NO! it can't be!\n")
                time.sleep(3)
                print("\nWhy it's Giant Donation Fruit Bat! and it wants you to donate fruits to satisfy it's immense hunger.\n")
                time.sleep(5)
                choose_your_own_directions.bat_directions()
                bat_app()
                
                choose_your_own_directions.game_end()
                
        

                
                


            else:
                print("\nPLESE PICK ONE OF THE TWO OPTIONS :)\n")
        else:
             print("\nPLEASE PICK ONE OF THE TWO OPTIONS :)\n")

            