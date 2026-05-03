import random
import time
import pgzrun
WIDTH= 750
HEIGHT= 480
planets= []
lines=[]
next_planet= 0
start_time= 0
end_time= 0
total_time= 0
total_planets= 8
def create():
    global start_time
    for i in range(total_planets):
        planet= Actor("planet")
        planet.pos= random.randint(90,660), random.randint(90,390)
        planets.append(planet)
    start_time= time.time()
def draw():
    global total_time
    screen.blit("space",(0,0))
    for i in planets:
        i.draw()
create()
pgzrun.go()