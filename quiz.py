import pgzrun
WIDTH= 600
HEIGHT= 480
Message_box= Rect(10,0,600,100)
Question_box= Rect(10,120,470,100)
Timer_box= Rect(490,120,100,100)
Skip_box= Rect(490,240,100,220)
Answer_box_1= Rect(10,240,230,100)
Answer_box_2= Rect(250,240,230,100)
Answer_box= [Answer_box_1, Answer_box_2]
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(Message_box,"black")
    screen.draw.filled_rect(Question_box,"blue")
    screen.draw.filled_rect(Timer_box," dark Green")
    screen.draw.filled_rect(Skip_box,"red")
    for i in Answer_box:
        screen.draw.filled_rect(i,"yellow")
pgzrun.go()