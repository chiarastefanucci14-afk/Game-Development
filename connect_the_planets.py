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
    number= 1
    for i in planets:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20)) 
        number+=1
    for i in lines:
        screen.draw.line(i[0],i[1],"white")
    if next_planet < total_planets:
        total_time= time.time()- start_time
        screen.draw.text(str(round(total_time, 1)),(10,10),fontsize= 80)
    else:
        screen.draw.text(str(round(total_time, 1)),(10,10),fontsize= 80)
def update():
    pass
def on_mouse_down(pos):
    global next_planet, lines
    if next_planet< total_planets:
        if planets[next_planet].collidepoint(pos):
            if next_planet:
                lines.append((planets[next_planet-1].pos,planets[next_planet].pos))
            next_planet+=1
        else:
            lines=[]
            next_planet= 0
create()
pgzrun.go()