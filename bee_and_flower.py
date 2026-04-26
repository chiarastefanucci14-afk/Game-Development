import random
import pgzrun
#screen
HEIGHT= 600
WIDTH= 600
bee=Actor("bee")
bee.pos= 100,100
flower=Actor("flower")
flower.pos= 200,400
def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
def move():
    flower.x= random.randint(90,510)
    flower.y= random.randint(90,510)
def update():
    if keyboard.left:
        bee.x-= 5
    if keyboard.right:
        bee.x+= 5
    if keyboard.up:
        bee.y-= 5
    if keyboard.down:
        bee.y+= 5
    flower_collected= bee.colliderect(flower)
    if flower_collected:
        move()

pgzrun.go()