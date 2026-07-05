import pgzrun
WIDTH= 600
HEIGHT= 480
Message_box= Rect(10,0,600,100)
Question_box= Rect(10,120,470,100)
Timer_box= Rect(490,120,100,100)
Skip_box= Rect(490,240,100,220)
Answer_box_1= Rect(10,240,230,100)
Answer_box_2= Rect(250,240,230,100)
Answer_box_3= Rect(250,350,230,100)
Answer_box_4= Rect(10,350,230,100)
Answer_box= [Answer_box_1, Answer_box_2, Answer_box_3, Answer_box_4,]
Message= ""
Score= 0
Time_left= 10
Is_game_over= False
Count= 0
Index= 0
Questions= []
File= "questions.txt"
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(Message_box,"black")
    screen.draw.filled_rect(Question_box,"blue")
    screen.draw.filled_rect(Timer_box," dark Green")
    screen.draw.filled_rect(Skip_box,"red")
    for i in Answer_box:
        screen.draw.filled_rect(i,"yellow")
    Message= f"Welcome to quiz master! Q: {Index} of {Count}"
    screen.draw.textbox(Message, Message_box, color= "white")
    screen.draw.textbox(str(Time_left), Timer_box, color= "white")
    screen.draw.textbox("Skip", Skip_box, color= "white")
    screen.draw.textbox(question[0].strip(),Question_box, color= "white")
    j= 1
    for i in Answer_box:
        screen.draw.textbox(question[j].strip(),i, color= "blue")
        j+=1
def update():
    move_message()
def move_message():
    Message_box.x-= 2
    if Message_box.right<0:
        Message_box.left=WIDTH
def update_time():
    global Time_left
    if Time_left:
        Time_left-=1
    else:
        game_over()
def game_over():
    global question, Time_left, Is_game_over
    m= f"Game over\n you got {Score} questions correct"
    question= [m,"-","-",""]
def read_question():
    global Count, Questions
    file= open(File, "r")
    for i in file:
        Questions.append(i)
        Count+=1
    file.close()
def read_next_question():
    global Index
    Index+=1
    return Questions.pop(0).split(",")
read_question()
question= read_next_question()
pgzrun.go()