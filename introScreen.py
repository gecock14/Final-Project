#!/usr/bin/env python

import getpass, fileinput, os
from sys import stdin, stdout, stderr, exit



def intro_screen(picked):
    valid = 0
    os.system('clear')
    stdout.write( "Welcome to Escape!\n" )
    stdout.write( "To read the instructions, press 'i'.\n")
    stdout.write( "To pick a scenario, press 'c'.\n")
    if picked:
	stdout.write("To begin the game press, 's'.\n")
    while (not valid):
	selectedOption = raw_input('==> ')
    	if selectedOption == 'i':
		return selectedOption
		valid = 1
    	elif selectedOption == 'c':
		return selectedOption
		valid = 1
	elif selectedOption == 's' and picked:
		return selectedOption
		valid = 1


def instruction_screen():
    os.system('clear')
    try:
	open("instructions")
	stdin = file("instructions")
    except:
	stderr.write("instructions does not exist\n")
	exit(1)
    for line in stdin:
	stdout.write(line)
    stdout.write( "Press 'b'  to return to the opening screen.\n")
    if raw_input('==> ') == 'b':
        selectedOption = 'b'
    else:
        selectedOption = 'i'
    return selectedOption
    
def start_game():
    os.system('clear')
    stdout.write( "Type 'QUIT' to end the game.\n")
    if raw_input('==> ') == 'QUIT':
        exit(0)
    else:
        return 's'

def choose_story():
    picked = 0;
    os.system('clear')
    stdout.write("Please enter the scenario you would like to play:\n")
    stdout.write("Car, Room\n")
    while(not picked):
	choice = raw_input('==> ')
        if (choice == 'Car' or choice == "Room"):
            try:
    		open(choice)
            	stdin = file(choice)
		picked = 1
    	    except:
                stderr.write(choice + " does not exist.\n")
                exit(1)
	else:
	    stdout.write("That scenario is not available at this time.\n")
	    stdout.write("Please choose another one from the list.\n")
    return picked    


if __name__=='__main__':
    state = 'b'
    picked = 0	    
    stdout.write("Hello, " + getpass.getuser() + "\n")
    while(1):
        if state == 'b':
            state = intro_screen(picked)
        if state == 'i':
            state = instruction_screen()
        if state == 's':
	    if picked:
            	state = start_game()
        if state == 'c':
	    #stdout.write(places[0])
	    picked = choose_story()
	    state = 'b'
    
    exit(0)
