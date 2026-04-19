import pgzrun
import random
HEIGHT= 600
WIDTH= 600
message= ""
saturn= Actor("planet")
def draw():
    screen.fill("blue")
    saturn.draw()
    screen.draw.text(message,(180,50),fontsize=70)
def update():
    if keyboard.left:
        saturn.x-= 10
    if keyboard.right:
        saturn.x+= 10
    if keyboard.up:
        saturn.y-= 10
    if keyboard.down:
        saturn.y+= 10
def random_moves():
    saturn.x= random.randint(90, 510)
    saturn.y= random.randint(90,510)
def on_mouse_down(pos):
    global message
    if saturn.collidepoint(pos):
        random_moves()
        message= "Good shot!"
    else:
        message= "You missed!"
pgzrun.go()
