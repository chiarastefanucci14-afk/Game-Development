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
    for i in items:
        i.draw()
def update():
    global items
    if len(items)==0:
        items= make_items(current_level)
def make_items(extra_items):
    items_to_create= option_to_create(extra_items)
    new_items= create_items(items_to_create)
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
pgzrun.go()