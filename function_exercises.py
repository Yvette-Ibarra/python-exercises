# 1 function returns true if entry is an int 2 or str 2 other entries return false
def is_two(e):
    if str(e) == '2':
        return True
    else:
        return False

# Alternative code
def is_two(n):
    return n == 2 or n == '2'



# 2 Takes in one arguemnt and returns True if argument is a vowel, False if argument is not vowel
def is_vowel(entry):
    if entry in ('aeiouAEIOU'):
        return True
    else:
        return False

# Alternative Code using list and checking type and length or argument
def is_vowel(somestring):
    if type(somestring) == str:
        if len(somestring) == 1:
            return somestring.lower() in list('aeiou')
        else:
            return False
    else:
        return False



# 3 Takes in an entry and returns True if entry is a consanant
def is_consonant(entry):
    if is_vowel(entry):
        return False
    else:
        return True

# ALternative Code checks to see if it is 
#.isalpha is a string method that checks if argument is alphabetical
            
def is_consonant(somestring):
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha(): 
            return (not is_vowel(somestring))
        else:
            return False
    else:
        return False   



# 4 If argument is a word that starts with a consonant then capitalize the word
def capitalize_word(entry):
    first_char = entry[0]
    if is_consonant(first_char):
        return entry.capitalize()
    else:
        return entry

# Alternative Code that checks if type of arguments is a string
def capitalize_starting_consonant(somestring):
    if type(somestring) == str:
        if is_consonant(somestring[0]):
            return somestring.capitalize()
        else:
            return somestring
    else:
        return somestring


# 5 calculate tip. enter tip percentage (between 0 and 1) and bill total to calculate tip
def calculate_tip(tip_percentage,total):
    tip_percentage = float(tip_percentage)
    amount_to_tip = (tip_percentage)*(total)
    print(amount_to_tip)

  # Alternative code using default tip_percent value
def calculate_tip(bill, tip_percent = 0.2):
    return bill * tip_percent

# 6 function takes in original price and discount percentage in arguments and returns price after discount
def apply_discount(original_price, discount_percentage):
    new_price = (original_price)*(1 - discount_percentage)
    return new_price

# Alternative code wid default tip_percent value
def apply_discount(orig_price, discount = 0.0):
    return orig_price - orig_price * discount




# 7 Function argument is a digit string with commas and returns an integer without commas
def handle_commas(entry):
    new_entry = entry.split(',')
    new_entry =''.join(new_entry)
    new_entry = int(new_entry)
    return new_entry

# Alternative code checks that argument is a string
def handle_commas(fakenum):
    if type(fakenum) == str:
        return int (fakenum.replace(',',''))
    else:
        return fakenum



# 8 Function argument is a number and returns its equivalent letter grade
def get_letter_grade (number):
    if number >= 90:
        return ('A')
    elif number >= 80:
        return('B')
    elif number >= 67:
        return('C')
    else:
        return('F')

# 9 Function accepts a string and returns string with vowels removed
def remove_vowels (entry):
    vowels = ('a','e','i','o','u','A','E','I', 'O', 'U')
    for i in entry:
        if i in vowels:
            entry = entry.replace(i,"")
    return entry

    # Alternative Code using an empty string
def remove_vowels(vowel_word):
    new_word = ''
    for letter in vowel_word:
        if not is_vowel(letter):
            new_word += letter
    return new_word

# 10 normalize the name of python take in string and removes capital letter, replaces spaces between words with underscore
def normalize_name(entry):
  
    entry = entry.lower()
    entry = entry.strip()
    
    for letter in entry:
        if letter == ' ':
            entry = entry.replace(letter, '_')
        elif not letter.isalpha() and not letter.isdigit():
            entry = entry.replace(letter, '')
    return entry

# Alternative code using .isidentifier method
def normalize_name(somestring):
    newstring = ''
    for letter in somestring:
        if letter.isidentifier() or letter == ' ':
            newstring += letter
    return newstring.strip().lower().replace(' ', '_') 

# 11 function arguments is a list and returns the cumative sum the number in the list
def cumulative_sum (list_of_numbers = []):
    new_list = []
    y= list_of_numbers[0]
    i=0
    
    while i < len(list_of_numbers)-1:
        new_list.append(y)
        y=list_of_numbers[i+1]+y
        i +=1
    new_list.append(y)
    print (new_list)

# Alternative code using sum function
def cumulative_sum(oldlist):
    newlist = []
    for i in range(1,len(oldlist)+1):
        cumusum = sum(oldlist[ :i])
        newlist.append(cumusum)
    return newlist