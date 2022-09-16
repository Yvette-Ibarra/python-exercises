# Exercises Identify the data type of the following values:

#float
99.9

#String
"False"

#boolean
False

#string
'0'

#int
0

#boolean
True

#String
'True'

#LIST
[{}]

#Dictionary
{'a': []}


# What data type would best represent:
"""
 A term or phrase typed into a search box?
    string 

If a user is logged in?
    string

A discount amount to apply to a user's shopping cart?
    float

Whether or not a coupon code is valid?
    boolean

An email address typed into a registration form?
    String

The price of a product?
    float

A Matrix?
    dictionary

The email addresses collected from a registration form?
    Nonetype

Information about applicants to Codeup's data science program?  
    NoneType
"""

#For each of the following code blocks, read the expression and predict what the result of evaluating it would be, 
# then execute the expression in your Python REPL.

# Prediction 12 ...returned TypeError
'1' + 2

# Prediction 2 ...returned 2
6 % 4

# Prediction INT ...returned int
type(6 % 4)

# Prediction  type ...
type(type(6 % 4))

# Prediction  TypeError
'3 + 4 is ' + 3 + 4

# Prediction False ..returened False
0 < 0

# Prediction TypeError ...returned False
'False' == False

# Prediction False ...returened False
True == 'True'

# Prediction True ...returned True
5 >= -5

# Prediction TypeError ...True
True or "42"

# Prediction 1 ...returned 1
6 % 5

# Prediction False ...returned False
5 < 4 and 1 == 1

# Prediction 'codeup', 'codeup','codeup','codeup' ... returned False
'codeup' == 'codeup' and 'codeup' == 'Codeup'

# Prediction True ...returned SyntaxError
4 >= 0 and 1 !== '1'

# Prediction True ...returned True
6 % 3 == 0

# Prediction True ...returned True
5 % 2 != 0

# Prediction SyntaxError ...returned TypeError
[1] + 2

# Prediction [3] ...returned [ 1, 2]
[1] + [2]

# Prediction [1,1] ... returned  [1,1] 
[1] * 2

# Prediction [1],[1] ...returned TypeError
[1] * [2]

# Prediction True ...returned True
[] + [] == []

# Prediction {} ...returned TypeError
{} + {}

'''You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it),
 and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, 
 how much will you have to pay? '''

price_for_movie_per_day = 3
days = 3 + 5 + 1
total_cost = price_for_movie_per_day* days
print(total_cost)

'''Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per 
hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? 
You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.'''

google_payrate = 400
amazon_payrate = 380
facebook_payrate = 350

google_hrs_worked = 6
amazon_hrs_worked = 4
facebook_hrs_worked = 10

total_payment = (google_payrate * google_hrs_worked  ) + (amazon_payrate * amazon_hrs_worked ) + (facebook_payrate * facebook_hrs_worked )
print(total_payment) 

'''A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her 
current schedule.'''

class_not_full = True

no_schedule_conflict = True

can_be_enrolled = class_not_full and no_schedule_conflict

print(can_be_enrolled)


'''A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do 
not need to buy a specific amount of products. '''

items_purchased =0
offer_not_expired =False
premium_member= False
if (items_purchased > 2 and offer_not_expired == True)  or premium_member == True:
    product_offer = True
    Else False
print(product_offer)


''' Use the following code to follow the instructions below:


username = 'codeup'
password = 'notastrongpassword'
Create a variable that holds a boolean value for each of the following conditions: '''

#the password must be at least 5 characters
len(password) >= 5
#the username must be no more than 20 characters
len(username) <= 20
#the password must not be the same as the username
username != password
#bonus neither the username or password can start or end with whitespace
 username != ' %s' and password != ' s%'