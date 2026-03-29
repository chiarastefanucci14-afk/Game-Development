import pgzrun
import random
#screen size
WIDTH= 600
HEIGHT= 600
def draw():
    screen.fill("black")
    w= 300
    h= 100
    for i in range (15):
        r1= Rect((0,0),(w,h))
        r1.center=(WIDTH/2, HEIGHT/2)
        r= random.randint(0, 255)
        g= random.randint(0,255)
        b= random.randint(0,255)
        screen.draw.rect(r1,(r,g,b))
        h+= 10
        w-= 10
        r-= 20
pgzrun.go()