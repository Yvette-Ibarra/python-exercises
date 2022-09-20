# 1 function returns true if entry is an int 2 or str 2 other entries return false
def is_two(e):
    if str(e) == '2':
        return True
    else:
        return False

# 2 Takes in one arguemnt and returns True if argument is a vowel, False if argument is not vowel
def is_vowel(entry):
    if entry in ('aeiouAEIOU'):
        return True
    else:
        return False

# 3 Takes in an entry and returns True if entry is a consanant
def is_consonant(entry):
    if is_vowel(entry):
        return False
    else:
        return True

# 4 If argument is a word that starts with a consonant then capitalize the word
def capitalize_word(entry):
    first_char = entry[0]
    if is_consonant(first_char):
        return entry.capitalize()
    else:
        return entry

# 5 calculate tip. enter tip percentage (between 0 and 1) and bill total to calculate tip
def calculate_tip(tip_percentage,total):
    tip_percentage = float(tip_percentage)
    amount_to_tip = (tip_percentage)*(total)
    print(amount_to_tip)
    
# 6 function takes in original price and discount percentage in arguments and returns price after discount
def apply_discount(original_price, discount_percentage):
    new_price = (original_price)*(1 - discount_percentage)
    return new_price

# 7 Function argument is a digit string with commas and returns an integer without commas
def handle_commas(entry):
    new_entry = entry.split(',')
    new_entry =''.join(new_entry)
    new_entry = int(new_entry)
    return new_entry

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
    for i in vowels:
        new_entry = entry.replace(i,"")
        return(new_entry)

# 10 normalize the name of python take in string and removes capital letter, replaces spaces between words with underscore
def normalize_name(entry):
    new_entry = entry.lower()
    new_entry.replace('' '','_')
    new_entry.replace(''%'','')
    return new_entry