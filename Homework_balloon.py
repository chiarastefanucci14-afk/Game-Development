import pgzrun
import random
HEIGHT= 600
WIDTH= 600
message= ""
balloon= Actor("balloon")
def draw():
    screen.fill("midnight blue")
    balloon.draw()
    screen.draw.text(message,(180,50),fontsize=70)
def update():
    if keyboard.left:
        balloon.x-= 10
    if keyboard.right:
        balloon.x+= 10
    if keyboard.up:
        balloon.y-= 10
    if keyboard.down:
        balloon.y+= 10
def random_moves():
    balloon.x= random.randint(90, 510)
    balloon.y= random.randint(90,510)
def on_mouse_down(pos):
    global message
    if balloon.collidepoint(pos):
        random_moves()
        message= "Good shot!"
    else:
        message= "You missed!"
pgzrun.go()
