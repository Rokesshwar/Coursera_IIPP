# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code
range = 100
secret_num = 0
guesses_left = 0


# helper function to start and restart the game
def new_game():  
    global range
    global secret_num
    global guesses_left
    
    secret_num = random.randrange(0, range)
    
    if range == 100 : 	
        guesses_left = 7
    elif range == 1000 :
        guesses_left = 10
      

    print "New game. The range is from 0 to", range, ". Good luck!"
    print "Number of remaining guesses is ", guesses_left, "\n"
    pass


# define event handlers for control panel
def range100():
    global range
    range = 100 # button that changes range to range [0,100) and restarts
    new_game() 
    pass

def range1000():
    global range
    range = 1000 # button that changes range to range [0,1000) and restarts
    new_game()
    pass

    
def input_guess(guess):    
    # main game logic goes here	
    global guesses_left
    global secret_num 
    
    won = False
    
    print "You guessed: ",guess
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is ", guesses_left
    
    if int(guess) == secret_num:       
        won = True
    elif int(guess) > secret_num:
        result = "It's High Need lower!"
    else:
        result = "It's low Need higher!"                
        
        
    if won:
        print "Winner Winner Chicken Dinner"
        new_game()
        return
    elif guesses_left == 0:
        print " Game Ended,Sorry You Lose. You didn't guess the number in time!"   
        new_game()
        return
    else:
        print result
        pass
            
    
# create frame
frame = simplegui.create_frame("Game: Guess the number!", 250, 250)
frame.set_canvas_background('Blue')

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 100)
frame.add_button("Range is [0, 1000)", range1000, 100)	
frame.add_input("Enter your guess", input_guess, 100)

# call new_game and start frame
new_game()
frame.start()
