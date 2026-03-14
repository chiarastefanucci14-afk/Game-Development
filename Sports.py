badminton_list= ["Person 1", "Person 2", "Person 3", "Person 4"]
soccer_list= ["Person 2","Person 4", "Person 6", "Person 7"]
badminton= set(badminton_list)
soccer= set(soccer_list)
#students who play both sports-> intersection
print(badminton&soccer)
#students who only play one sport-> symetric difference
print(badminton^soccer)
#Students that only play badminton
print(badminton-soccer)