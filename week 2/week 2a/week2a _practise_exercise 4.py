# Open a frame
import simplegui
###################################################
# Open frame
# Student should add code where relevant to the following.


message = "My first frame!"
message = "Hi Im Roki"
# Handler for mouse click
def click():
    print message

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)


