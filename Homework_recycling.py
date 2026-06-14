import pgzrun
import random
WIDTH= 600
HEIGHT= 600
levels= 10
start_speed= 10
non_recycle=['banana_peel','shirt','phone','pot']
game_over= False
game_complete= False
current_level= 1
items=[]
animations= []
def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit('recycleimg',(0,0))
    if game_over:
        screen.draw.text("Game Over!",(150, HEIGHT/2), fontsize= 80, color= "midnight blue")
    elif game_complete:
        screen.draw.text("You finished the game!",(150, HEIGHT/2), fontsize= 50, color= "midnight blue")
    else:
        for i in items:
            i.draw()
def update():
    global items
    if len(items)==0:
        items= make_items(current_level)
def make_items(extra_items):
    items_to_create= option_to_create(extra_items)
    new_items= create_items(items_to_create)
    lay_out_items(new_items)
    animate_items(new_items)
    return new_items
def option_to_create(extra_items):
    items_to_create= ['paper']
    for i in range(extra_items):
        random_option= random.choice(non_recycle)
        items_to_create.append(random_option)
    return items_to_create
def create_items(items_to_create):
    new_items= []
    for i in items_to_create:
        item= Actor(i+'img')
        new_items.append(item)
    return new_items
def lay_out_items(items_to_layout):
    gaps= len(items_to_layout)+1
    gaps_size= WIDTH/gaps
    random.shuffle(items_to_layout)
    for i,j in enumerate(items_to_layout):
        new_x= (i+1)*gaps_size 
        j.x= new_x
def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        duration= start_speed- current_level
        i.anchor= ("center","bottom")
        animation= animate(i,duration=duration,on_finished= handle_game_over,y=HEIGHT)
        animations.append(animation)
def handle_game_over():
    global game_over
    game_over= True
def on_mouse_down(pos):
    global items,current_level
    for i in items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handle_game_complete()
            else:
                handle_game_over()
def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    if current_level== levels:
        game_complete= True
    else:
        current_level+= 1
        items= []
        animations= []
def stop_animations(animations_to_stop):
    for i in animations_to_stop:
        if i.running:
            i.stop()
pgzrun.go()