students_details = {
  'name':'Jane Doe',
  'age':23,
  'address': 'West Street house number -2 Ireland',
  'phone number':'+21-56348790'
  }
print(students_details)
#acessing the values
print(students_details['age'])
#add a key
students_details['Driving licence No']='SG234T5'
print(students_details)

#update the value
students_details['Driving licence No']='SH234T5'
print(students_details)

#for loop
for items in students_details:
  print("{}: {}".format(items,students_details[items]))

del students_details['address']
print(students_details)