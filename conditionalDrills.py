'''
For this assignment you should read the task, then below the task do what it asks you to do.
'''

'''
#1) Create a Variable called grade and set it to an integer. Make an if statement that checks if the grade is a passing grade. grade must be above 65 to pass. print out "student is passing"
'''
grade = 78
if grade > 65:
    print ("student is passing")
'''
#2) Now make an if, else statement that checks if the student is passing but also print "student is failing", if the grade is less than 65
'''
grade = 45 
if grade < 65:
    print ("student is failing")  
else grade > 65:
    print ("student is passing")  
'''
#3)Create a variable called age. Make and if, else statement that checks if the age entered is old enough to vote. Remember the voting age is 18
'''
age = 7
if age < 18:
    print ("cannot vote")
else age == 18:
    print ("can vote")
'''
#4)Create a variable called weight. Make an if statement that checks the unit of the weight. If the weight is in kilograms, convert it to pounds 
'''
weight = 100
if weight == int:
    print (weight*0.45359)
'''
#5)Now modify the previous program to also convert from pounds to kilograms
'''
weight = 100
if weight == int:
    print (weight*2.20462)
'''
#6)create a list (seat1 = 1, seat2 = 1, seat3 = 0, seat4 = 1), Now make an if elseif, else statement that checks if a seat is open. if the seat = 1 its closed and print that it's closed. If the seat = 0, it's open and print that it's open. If no seats are open print "There are no available seats"
'''
seat1 = 1 
seat2 = 1
seat3 = 0
seat4 = 1
listSeats = [seat1,seat2,seat3,seat4]
if seat1 == 1:
    print ("seat 1 is closed")  
else seat1 == 0:
    print ("seat 1 is open")
if seat2 == 1:
    print ("seat 2 is closed")
else seat2 == 0:
    print ("seat 2 is opened")
if seat3 == 1:
    print ("seat 3 is closed")
else seat3 == 0:
    print ("seat 3 is opened")
if seat4 == 1:
    print ("seat 4 is closed")
else seat4 == 0:
    print ("seat 4 is opened")
