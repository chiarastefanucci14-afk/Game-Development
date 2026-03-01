List=[]
for i in range (5):
    groupname=input("What is the group name?")
    sizeofgroup=input("How many people are on your team?")
    dateofcompetition=input("When is this tournament?")
    venue=input("Where is it going to be?")
    typeofmedal=input("What is the prize if you win?")
    information= groupname,sizeofgroup,dateofcompetition,venue,typeofmedal
    List.append(information)
print(List)
