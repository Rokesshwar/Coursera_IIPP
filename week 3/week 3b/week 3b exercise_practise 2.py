# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
def start():
    timer.start()
    
def stop():
    timer.stop()
    
def reset():
    global counter 
    counter=0
    
# Event handlers for buttons
frame = simplegui.create_frame("Counter with buttons", 200, 200)

frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)

        
# Create frame and timer

timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
frame.start()