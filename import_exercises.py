import function_exercises as fe
calculateion = fe.calculate_tip(50, .1)
print(calculateion)

# 2
# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
    # 9 different ways
import itertools as it
len(list(it.product('abc','123')))

#How many different combinations are there of 2 letters from "abcd"?
    # 6 combinations
combinations_letter = list(it.combinations('abcd',2))
print(combinations_letter)
length = len(list(it.combinations('abcd',2)))
print(length)

#How many different permutations are there of 2 letters from "abcd"?
    # 12 different permutations
combinations_letter = list(it.permutations('abcd',2))
print(combinations_letter)
length = len(list(it.permutations('abcd',2)))
print(length)

#3
import json
profiles = json.load(open('profiles.json')) 

# Total number of users
    # 19 users
len(profiles)

# Number of active users
    # 9 active users 
counter = 0
for item in profiles:
    if item['isActive']== True:
        counter = counter +1
print(counter)
   
# Number of inactive users
    # 10 inactive users
counter = 0
for item in profiles:
    if item['isActive']== False:
        counter = counter +1
print(counter)

# Grand total of balances for all users
    #grand_total is 52667.02

grand_total = 0
for item in profiles:
    number = item['balance']
    number = number.replace(',','').replace('$','')
    
    grand_total +=float(number)
print(grand_total)

#Average balance per user
    #The average balance is 2771.9484210526316
grand_total = 0
for item in profiles:
    number = item['balance']
    number = number.replace(',','').replace('$','')
    
    grand_total +=float(number)
average_balance = grand_total / (len(profiles))
print(average_balance)

#User with the lowest balance
    # lowest balance  is $1,214.10
lowest_balance = profiles[0]['balance']

for file in profiles:
    
    if file['balance'] < lowest_balance:
        
        lowest_balance = file['balance']

print(lowest_balance)

# User with the highest balance
    # the highest balance is $3,919.64

highest_balance = profiles[0]['balance']

for file in profiles:
    
    if file['balance'] > highest_balance:
        
        highest_balance = file['balance']

print(highest_balance)

# Most common favorite fruit
    #strawberry
list_of_fruit = []
for i in profiles:
    list_of_fruit.append(i['favoriteFruit'])  
print(max(set(list_of_fruit), key = list_of_fruit.count))

# Least most common favorite fruit
    #apple
list_of_fruit = []
for i in profiles:
    list_of_fruit.append(i['favoriteFruit'])  
print(min(set(list_of_fruit), key = list_of_fruit.count))

# Total number of unread messages for all users
    # total unread messages is 210
import re
list_of_greetings= []
for i in profiles:
    list_of_greetings.append(i['greeting'])
numbers_list = [int(i) for i in str(list_of_greetings).split() if i.isdigit()]
print (sum(numbers_list))

