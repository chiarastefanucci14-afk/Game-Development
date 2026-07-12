import pgzrun
WIDTH= 556
HEIGHT= 390
Red= Rect(30,30,150,150)
Dark_green= Rect(200,30,150,150) 
Blue= Rect(372,30,150,150)
Yellow= Rect(30,210,150,150)
Purple= Rect(200,210,150,150)
Pink= Rect(372,210,150,150)
chosen= ""
def draw():
    screen.clear()
    screen.fill("black") 
    if chosen == "":   
        screen.draw.filled_rect(Purple,"purple")
        screen.draw.filled_rect(Blue,"blue")
        screen.draw.filled_rect(Dark_green,"dark Green")
        screen.draw.filled_rect(Red,"red")
        screen.draw.filled_rect(Yellow,"yellow")
        screen.draw.filled_rect(Pink,"pink")
    else:
        screen.draw.text("Your favorite color is "+  chosen + "!!!",(40,170), fontsize= 50, color= chosen)

def on_mouse_down(pos):
    global chosen
    if Red.collidepoint(pos):
        chosen= "red"
    if Dark_green.collidepoint(pos):
        chosen= "green"
    if Blue.collidepoint(pos):
        chosen= "blue"
    if Yellow.collidepoint(pos):
        chosen= "yellow"
    if Purple.collidepoint(pos):
        chosen= "purple"
    if Pink.collidepoint(pos):
        chosen= "pink"
pgzrun.go()
    
