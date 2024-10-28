"""
Text Analyzer, first project for Engeto Online Python Academy
Author: Helena Tresohlava
Email: h.tresohlava@gmail.com
Discord: Helena T. (3nul)
"""

# Defining users and their passwords
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# User login
username = input("Enter a username: ")
password = input("Enter a password: ")

separator = "-" * 50

# Username and password authentication
if username in users and users[username] == password:
    print(separator)
    print(f"Welcome to the app, {username}!")
    print(f"We have 3 texts to be analyzed.")
    print("-" * 50)
    
    # Continue to parse text if login is successful
    TEXTS = ['''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley. ''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
    ]

    # Getting a selection from the user
    user_input = input("Enter a number btw.  1 and 3 to select: ")

    # Verification of entry
    if not user_input.isdigit():
        print("You have entered an invalid entry, you must enter a number.")
    else:
        text_number = int(user_input)
        if text_number < 1 or text_number > 3:
            print("The specified text number does not exist.")
        else:
            # Text selection
            text = TEXTS[text_number - 1]
            print(f"Analyzing text number {text_number}...")
            print("-" * 50)

            # Division of text into words
            words = text.split()
            
            # Word count
            total_words = len(words)
            
            # Amount of words starting with a capital letter
            capitalized_words = sum(1 for word in words if word[0].isupper())
            
            # Amount of capitalized words   
            uppercase_words = sum(1 for word in words if word.isupper() and word.isalpha())
            
            # Amount of words in lowercase
            lowercase_words = sum(1 for word in words if word.islower())
            
            # Amount of numbers and their sum
            numbers = [int(word) for word in words if word.isdigit()]
            total_numbers = len(numbers)
            sum_numbers = sum(numbers)

            # The results
            print(f"There are {total_words} words in the selected text.")
            print(f"There are {capitalized_words} titlecase words.")
            print(f"There are {uppercase_words} uppercase words.")
            print(f"There are {lowercase_words} lowercase words.")
            print(f"There are  {total_numbers} numeric strings.")
            print(f"The sum of all numbers {sum_numbers}.")

            # Dictionary for storing word length frequencies
            lengths = {}

            # Counting word lengths
            for word in words:
                # Removing punctuation from the end of a word
                word = word.strip(",.?!")
                length = len(word)
                if length in lengths:
                    lengths[length] += 1
                else:
                    lengths[length] = 1

            # Bar chart display in terminal with header
            print("-" * 50)
            print(f"{'LEN':<5}|  {'OCCURRENCES':<12}  |NR.")
            print("-" * 50)
            for length, count in sorted(lengths.items()):
                print(f"{length:<5}|  {'*' * count:<12}  |{count}")
else:
    print("Unregistered user, terminating the program.")
