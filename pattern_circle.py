import pgzrun
import random
#screen
WIDTH= 600
HEIGHT= 600
def draw():
    screen.fill("black")
    radius= 100
    for i in range (15):
        r= random.randint(0, 255)
        g= random.randint(0,255)
        b= random.randint(0,255)
        #screen.draw.circle((WIDTH/2,HEIGHT/2),radius,(r,g,b))
        screen.draw.filled_circle((WIDTH/2,HEIGHT/2),radius,(r,g,b))  #see only filled cicles 
        screen.draw.text("Circle pattern!",(200,430),color="blue",fontsize=40)
        radius-= 10
        b+= 20
pgzrun.go()