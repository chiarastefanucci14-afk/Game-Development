import random
import pgzrun
#screen
HEIGHT= 600
WIDTH= 600
bee=Actor("bee")
bee.pos= 100,100
flower=Actor("flower")
flower.pos= 200,400
score= 0
game_over= False
def timer():
    global game_over
    game_over= True
def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+str(score),(180,50),fontsize= 60)
    if game_over:
        screen.fill("lavender")
        screen.draw.text("Time is up! Your score is:"+str(score),(40,50),fontsize= 60,color="black")
def move():
    flower.x= random.randint(90,510)
    flower.y= random.randint(90,510)
def update():
    global score
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
        score+=1
clock.schedule(timer, 10.0)
pgzrun.go()