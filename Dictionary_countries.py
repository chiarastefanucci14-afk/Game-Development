Countries_and_Capitals= {}
while True:
    print("1.Insert")
    print("2.Display all countries")
    print("3.Display all caapitals")
    print("4.Get capital")
    print("5.Delete")
    print("6.Exit")
    Choice= int(input("What is your choice?"))
    if Choice== 1:
        Country= input("What country do you want to add?")
        Capital= input("What is the capital of this country?")
        Countries_and_Capitals[Country]=Capital
    elif Choice== 2:
        print(Countries_and_Capitals.keys())
    elif Choice== 3:
        print(Countries_and_Capitals.values())
    elif Choice== 4:
        identify= input("What is the country that you want the capital of?")
        if identify in Countries_and_Capitals:
            print(Countries_and_Capitals[identify])
        else:
            print("The country you have entered does not exist in the dictionary. Please try again.")
    elif Choice== 5:
        delete= input("Which country do you want to delete?")
        del Countries_and_Capitals[delete]
    elif Choice== 6:
        print("You have existed the dictionary! Bye bye!")
        break
