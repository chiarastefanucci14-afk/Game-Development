import random
import pgzrun
#screen
HEIGHT= 600
WIDTH= 600
rabbit=Actor("rabbit")
rabbit.pos= 100,100
carrot=Actor("carrot")
carrot.pos= 200,400
score= 0
game_over= False
def timer():
    global game_over
    game_over= True
def draw():
    screen.blit("forest",(0,0))
    rabbit.draw()
    carrot.draw()
    screen.draw.text("score:"+str(score),(180,50),fontsize= 60)
    if game_over:
        screen.fill("lavender")
        screen.draw.text("Time is up! Your score is:"+str(score),(40,50),fontsize= 60,color="black")
def move():
    carrot.x= random.randint(90,510)
    carrot.y= random.randint(90,510)
def update():
    global score
    if keyboard.left:
        rabbit.x-= 5
    if keyboard.right:
        rabbit.x+= 5
    if keyboard.up:
        rabbit.y-= 5
    if keyboard.down:
        rabbit.y+= 5
    flower_collected= rabbit.colliderect(carrot)
    if flower_collected:
        move()
        score+=1
clock.schedule(timer, 60.0)
pgzrun.go()