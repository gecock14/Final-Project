#!/usr/bin/env python

import getpass, fileinput, os
from sys import stdin, stdout, stderr, exit

global stars
stars = 0
global defeated
defeated = 0
global defeated_Bear
defeated_Bear = 0

def intro_screen():
    valid = 0
    os.system('clear')
    print "Hello, " + getpass.getuser()
    print "Welcome to Super Mario Text Adventure!"
    print "To read the instructions, press 'i'."
    print "To begin the game press, 's'."
    while (not valid):
	selectedOption = raw_input('==> ').lower()
    	if selectedOption == 'i':
		return selectedOption
		valid = 1
    	elif selectedOption == 's':
		return selectedOption
		valid = 1
	elif selectedOption == 'quit':
		exit(0)

def instruction_screen():
    os.system('clear')
    try:
	open("instructionsMario")
	stdin = file("instructionsMario")
    except:
	stderr.write("Error opening instructionsMario\n")
	exit(1)
    for line in stdin:
	stdout.write(line)
    print "Press 'b'  to return to the opening screen."
    if raw_input('==> ').lower() == 'b':
        selectedOption = 'b'
    else:
        selectedOption = 'i'
    return selectedOption
    


def start_game():
    os.system('clear')
    print '''It's a me! Mario!
    The evil Bowser has kidnapped Princess Peach and is holding her
    in a locked room in the upper tier of the castle.
    You must find all 2 Stars in order to open the door and 
    save Princess Peach.
    \nTo enter Princess Peach's Castle press 'e'.'''
    print
    while(1):
	choice = raw_input('==> ').lower()
    	if choice == 'quit':
            exit(0)
    	elif choice == 'e':
	    enter_castle()
    	else:
             print "That's not an option, try 'e' to enter the castle or 'quit' to end the game.\n"


def enter_castle():
    global stars
    os.system('clear')
    print "You are standing in the great hall of Princess Peach's Castle."
    if(stars != 2):
	print "There are two doors in front of you. Which do you choose, '1' or '2'?"
    else:
	print "***You've unlocked Bowser's Lair!***"
	print "Which room do you choose? 1,2 or Lair"
    print "Stars: ",stars
    while(1):
	choice = raw_input('==> ').lower()
	if (choice == 'quit'):
	    exit(0)
	elif (choice == '1'):
	    winter_room()
	elif (choice == '2'):
	    bear_room()
	elif(choice == 'lair' and stars is 2):
	    bowsers_lair()
	    

def winter_room():
    global stars
    global defeated
    if( not defeated):
    	print ''' You enter the room and discover a giant Snowman!
    	There are two power ups on the table, Super Mushroom and Fire Flower.
    	Which do you choose?"'''
    	while(1):
	    choice = raw_input('==> ').lower()
	    if( choice == 'super mushroom'):
	        kicked("Snowman: Size wont help you against me! I can become as big as I want!")
	    	return_main()
	    elif( choice == 'fire flower'):
		defeated = 1
		print "Snowman: I'm Melting!!!!"
		print "You've earned a star!"
		stars = stars + 1
		winter_room()
		
    else:
	print "Snowman wont be hiding out in here anymore."
	return_main()


def bear_room():
    global stars
    global defeated_Bear
    if( not defeated_Bear):
        print ''' You enter the room and discover a bear!
        There are two power ups on the table, Starman and Super Mushroom
        Which do you choose?"'''
        while(1):
            choice = raw_input('==> ').lower()
            if( choice == 'starman'):
                kicked("When your star power wore off the bear killed you.")
                return_main()
            elif( choice == 'super mushroom'):
                defeated_Bear = 1
                print "Your immense size scared off the bear."
                print "You've earned a star!"
                stars = stars + 1
                bear_room()

    else:
        print "The bear wont be hiding out in here anymore."
        return_main()


def bowsers_lair():
    print "Bowser: Mwahaha! It looks like you've made it past my gaurds!"
    print "Bowser: No matter, you will not get past me!"
    print "**Bowser starts charging at you**"
    print "Dodge, Jump, or Punch"
    dodged = 0
    grabbed = 0
    swing = 0
    while(1):
	action = raw_input('==> ').lower()
	if(action == 'dodge' and dodged == 0):
	    print "Great Job! Bowser is now not looking! Grab, Punch or Kick!"
	    dodged = 1
	elif(action == 'jump'):
	    kicked("Bowser: Mwahaha! You can't jump over me!")
	elif(action == 'punch'):
	    kicked("Bowser: Mwahaha! Do you really think you can hurt me?!")
	elif(action == 'grab' and dodged == 1 and grabbed == 0):
	    print "You've got Bowser by the tail! Punch, Kick, or Swing!"
	    grabbed = 1
	elif(action == 'kick'):
	    kicked( "Bowser: Mwahaha! Do you really thing you can hurt me?!")
	elif(action == 'swing' and grabbed == 1):
	    print "Bowser is swinging fast and faster! Throw, Drop, or Kick"
	elif(action == 'drop' and swing == 0):
	    kicked("Bowser: Mwahaha! You are a fool for dropping me!")
	elif(action == 'throw' and swing == 0):
	    print "***You throw Bowser into a bomb and it explodes***"
	    end_game()


def return_main():
    print "Press 'b' to return to the main hall."
    while(1):
        if(raw_input('==> ').lower() == 'b'):
            enter_castle()


def kicked(reason):
    print reason
    return_main()
    
    
def start():
    state = 'b'
    while(1):
        if state == 'b':
            state = intro_screen()
        elif state == 'i':
            state = instruction_screen()
    	elif state == 's':
	    state = start_game()

def end_game():
    print "You Win!"
    while(1):
	print "Press 'm' to go to the main menu"
	if(raw_input('==> ').lower() == 'm'):
	    start()    	    
start()
