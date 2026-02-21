matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
#find the number of rows
print(len(matrix))
#find the number of columns
print(len(matrix[1]))
#Access an element in a 2D list
print(matrix[1][2])
#Take an input and print the elements
rows= int(input("How many rows would you like to have?:"))
columns= int(input("How many columns would you like to have?:"))
matrix=[]
for i in range(rows):
    sublist= []
    for j in range(columns):
        element= int(input("Which element would you like to add?:"))
        sublist.append(element)
    matrix.append(sublist)
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end=" ")
    print()
#Add matrices
matrix1= [[3,8],[4,1]]
matrix2= [[2,6],[10,9]]
addition=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        addition[i][j]= matrix1[i][j]+matrix2[i][j]
print(addition)
#HOMEWORK- SUBTRACT 2 MATRICES
matrix3= [[8,6],[7,9]]
matrix4= [[2,4],[1,3]]
subtraction= [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        subtraction[i][j]= matrix3[i][j]-matrix4[i][j]
print(subtraction)