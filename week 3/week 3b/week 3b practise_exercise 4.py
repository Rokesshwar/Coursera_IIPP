# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

width = 200
height= 200
radius = 1


# Timer handler
def tick():
    global radius
    radius+=1
    
# Draw handler
def draw(canvas):
    canvas.draw_circle([width/2,height/2],radius,1,"white","red")
    
        
# Create frame and timer
frame=simplegui.create_frame("Circle",200,200)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,tick)
# Start timer
frame.start()
timer.start()
