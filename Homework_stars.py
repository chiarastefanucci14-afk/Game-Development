import random
import time
import pgzrun
WIDTH= 750
HEIGHT= 480
stars= []
lines=[]
next_star= 0
start_time= 0
end_time= 0
total_time= 0
total_stars= 8
def create():
    global start_time
    for i in range(total_stars):
        star= Actor("star")
        star.pos= random.randint(90,660), random.randint(90,390)
        stars.append(star)
    start_time= time.time()
def draw():
    global total_time
    screen.blit("space",(0,0))
    number= 1
    for i in stars:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20)) 
        number+=1
    for i in lines:
        screen.draw.line(i[0],i[1],"white")
    if next_star < total_stars:
        total_time= time.time()- start_time
        screen.draw.text(str(round(total_time, 1)),(10,10),fontsize= 80)
    else:
        screen.draw.text(str(round(total_time, 1)),(10,10),fontsize= 80)
def update():
    pass
def on_mouse_down(pos):
    global next_star, lines
    if next_star< total_stars:
        if stars[next_star].collidepoint(pos):
            if next_star:
                lines.append((stars[next_star-1].pos,stars[next_star].pos))
            next_star+=1
        else:
            lines=[]
            next_star= 0
create()
pgzrun.go()