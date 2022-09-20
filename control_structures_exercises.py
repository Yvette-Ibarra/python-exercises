# Control Structures Exercises

#Do your work for this exercise in a file named control_structures_exercises.py.


# 1 Conditional Basics
# A prompt the user for a day of the week, print out whether the day is Monday or not '''

day = input('what day is today? ')
day= day.lower
if day == 'monday':
    print ('Today is Monday!')
else:
    print('Today is not Monday!')

# B prompt the user for a day of the week, print out whether the day is a weekday or a weekend  '''

day = input('Type in a day of the week? ')
weekend = ['saturday','sunday']
day= day.lower
if day in weekend:
    print ('This day falls on the weekend!')
else:
    print('This day is a weekday')

# C create variables and make up values for
            #the number of hours worked in one week 
number_of_hrs = 20
            #the hourly rate
pay_per_hour = 13.55
            #how much the week's paycheck will be
total_paycheck = number_of_hrs * pay_per_hour
total_paycheck


# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
total_week_hrs = 45
pay_rate = 20

if total_week_hrs <= 40:
    total_weeks_pay = total_week_hrs * pay_rate
else:
    overtime = total_week_hrs - 40
    overtime_pay = overtime * (pay_rate*1.5)
    
    total_weeks_pay = overtime_pay + 40*(pay_rate)
    
total_weeks_pay 


#    2 Loop Basics
'''
        While
           Create an integer variable i with a value of 5.

            Create a while loop that runs so long as i is less than or equal to 15
            Each loop iteration, output the current value of i, then increment i by one.
 '''
i = 5
while i <= 15:
    print(i)
    i = i + 1





# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 100000000:
    print(i)
    i **= 2

# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5



# b For Loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

for x in range(1,11):
    print(f'{user_num} X {x} = {int(user_num) * x }') 


    # Using While Loop
 number =  int(input('Enter a positive number that is 10 or less '))
i = 0
if number <= 10:
    while i <= 10:
        multiply = number * i
        print(f'{number} X {i} = {multiply}')
        i +=1       

#  Create a for loop that uses print to create the output shown below.

for i in range(1, 10):
    print(i * str(i))


# Using While Loop
i = 1
while i <=9:
    x=str(i)
    print (x*i)
    i += 1

# c break and continue
# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
positive_integer = int(input("Enter a positive integer "))
                       
while True:
    print(positive_integer)
    positive_integer -= 1
    if positive_integer < 1:
        break

# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
'''
number =int(input("Enter a positive number "))
i = 0
if number > 0:
    while i <= number:
        print (i)
        i += 1
        if i > number:
            break
'''
# Update to check for digits in user input

while True:
    user_num = input( 'Please enter a positive number: ')
                                                # could have used     if user_num.isdigit():
    if user_num.isdigit() == True:              # check digit first because if we run int(user_num) on a non digit error will occur
        print('This is a digit')                #print to check what part of loop is actually working
        if int(user_num) > 0:
            print("This number is positve!")
            break

user_num = int(user_num)
for i in range(user_num, 0, -1):
    print(i)


# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

while True:
    num = input('Enter an odd number between 1 and 50: ' )
    if num.isdigit() == True:
        num = int(num)
        if num%2 == 1 and num > 0 and num < 51:
            for i in range(1, 50, 2):
                if i == num:
                    print(f'Yikes! Skipping number: {i}')
                    continue
                print(f'Here is an odd number: {i}') 


# 3 Fizzbuzz
    '''One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
        Write a program that prints the numbers from 1 to 100.
        For multiples of three print "Fizz" instead of the number
        For the multiples of five print "Buzz".
        For numbers which are multiples of both three and five print "FizzBuzz".  '''  
i = 0
while i <= 100:
    print(i)
    i +=1
    if i%3 == 0 and i%5 ==0:
        print ( 'FizzBuzz')
        i +=1
        continue
    elif i%3 == 0:
        print ('Fizz')
        i +=1
        continue
    elif i%5 == 0:
        print('Buzz')
        i +=1
    

''' 4 Display a table of powers.
        Prompt the user to enter an integer.
        Display a table of squares and cubes from 1 to the value entered.
        Ask if the user wants to continue.
        Assume that the user will enter valid data.
    Only continue if the user agrees to. '''

number = int(input("What number would you like to go up to?  "))
ask = 'yes'
while ask == 'yes':
    print ("{:<8}| {:<10}| {:<10}".format('number','squared','cubed'))
    i = 1
    while i <= number:
        print ("{:<8}| {:<10}| {:<10}".format(i, i**2, i**3))
        i +=1
        continue
    ask = input ('Do you want to continue? ')
    ask = ask.lower()
    if ask == 'yes':
        number = int(input("What number would you like to go up to?  "))

Bonus: Research python's format string specifiers to align the table
5. Convert given number grades into letter grades.
        Prompt the user for a numerical grade from 0 to 100.
        Display the corresponding letter grade.
        Prompt the user to continue.
        Assume that the user will enter valid integers for the grades.
        The application should only continue if the user agrees to.
Grade Ranges:
A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0

'''

'''
Bonus
Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
'''