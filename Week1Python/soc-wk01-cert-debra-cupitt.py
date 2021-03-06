# coding: utf-8
#
# ================ DAY 1 HOMEWORK - Calculator ================ #

hrs_year = 24*365
print('Hours in a yr: ' + str(hrs_year))

mins_dec = (hrs_year*60)*10
print('Minutes in a decade: ' + str(mins_dec))

secs_dec = mins_dec*60
my_age_secs = (secs_dec)*2.73
print("I am " + str(my_age_secs) + " seconds old.")

# Andreea Visanoiu​/s age is 48,618,000 seconds old (not counting leap years) at 11:30 am Jul 16, 2018. Convert to years

yrs_dec = 10
secs_dec = mins_dec*60

andreea_age_secs = 48618000
andreea_decs = float(andreea_age_secs)/float(secs_dec)
andreea_age_yrs = andreea_decs*yrs_dec

print("Andrea Visanoiu​ is " + str(andreea_age_yrs) + " years old.")


# ================ DAY 2 HOMEWORK - n/a =============================== #

# ================ DAY 3 HOMEWORK - Inputs and Responses ================ #

# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

first_name = ""
middle_name = ""
last_name = ""
first_name = input("What is your first name?  ")
middle_name = input("What is your middle name?  ")
last_name = input("What is your last name?  ")
print("It's lovely to meet you " + first_name + " " + middle_name + " " + last_name + "!")

# ----------------------------------------------------------------------------------------

# Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)

fav_number = input("What is your favourite number?  ")
def make_better_number (fav_number):
    better_number = int(fav_number) + 1
    return better_number

print("That's a great choice! However, perhaps " + str(make_better_number (fav_number)) + " is a bigger and better favourite number?")

# ----------------------------------------------------------------------------------------------

# Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
# WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!

def answer_boss():
    answer = str(input("What do you want? "))
    if answer == "I want a raise":
        print('WHADDAYA MEAN "I WANT A RAISE"?!? YOU\'RE FIRED!!')
    else:
        print('I SAID,')
        answer_boss()

answer_boss()

# ----------------------------------------------------------------------------------------------

# Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
# Table of Contents
# Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13

scrum_contents = [
["Chapter 1: The Way the World Works Is Broken", "p. 1"],
["Chapter 2 The Origins of Scrum", "p. 23"],
["Chapter 3 Teams", "p. 41"],
["Chapter 4 Time", "p. 71"],
["Chapter 5 Waste Is a Crime", "p. 85"],
["Chapter 6 Plan Reality, Not Fantasy", "p. 111"],
["Chapter 7 Happiness", "p. 145"],
["Chapter 8 Priorities", "p. 171"],
["Chapter 9 Change the World", "p. 203"],
["Acknowledgments", "p. 232"],
["Appendix: Implementing Scrum-How to Begin", "p. 234"],
["Notes", "p. 239"],
["Index", "p. 242"]
]

def print_contents(contents):
    print("Table of Contents")
    i = 0
    for c in contents:
        print(contents[i][0].ljust(60) + contents[i][1])
        i = i + 1

print_contents(scrum_contents)

# ================ DAY 4 HOMEWORK - Loops & Lists ================ #

# “99 Bottles of Beer on the Wall.”

for b in range (99,1,-1):
    print(str(b) + " bottles of beer on the wall, " + str(b) + " bottles of beer. Take one down and pass it around, " + str(b) + " bottles of beer on the wall.")

print(str(1) + " bottle of beer on the wall, " + str(1) + " bottle of beer. Take one down and pass it around, " + str(1) + " bottle of beer on the wall.")

print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")


# ----------------------------------------------------------------------------------------------

# Deaf grandma.

import random

def grandma_convo(num):
    year = str(random.randrange(1930, 1950))
    words_to_grandma = input("What would you like to say to Grandma?")
    count = num
    if words_to_grandma == "BYE" and count == 2:
        print("Grandma says: OK BYE DEAR!")
    elif words_to_grandma == "BYE":
        print("Grandma says: HOW\'S THE WEATHER?")
        count = count + 1
        grandma_convo(count)
    elif words_to_grandma.isupper():
        print("Grandma says: 'NO, NOT SINCE " + year + "!'")
        grandma_convo(0)
    else:
        print("Grandma says: 'HUH?! SPEAK UP, GIRL!'")
        grandma_convo(0)

grandma_convo(0)

# ----------------------------------------------------------------------------------------------

# Leap years.

def leap_year_calc(start_yr, end_yr):
    for y in range(int(start_yr), int(end_yr)):
        if y % 100 == 0 and y % 400 == 0:
            print(y)
        if y % 4 == 0 and y % 100 != 0:
            print(y)

starting_point = input("What year would you like to start counting from?  ")

ending_point = input("What year would you like to stop counting?  ")

print("The leap years between the years " + starting_point + " and " + ending_point + " include:")
leap_year_calc(starting_point, ending_point)


# ----------------------------------------------------------------------------------------------

# Find something today in your life, that is a calculation. Estimate your books by bookshelf

def books_bookshelf(bookshelves_num):
    books = int(bookshelves_num) * 200
    return books

bookshelves = input("How many bookshelves do you have?  ")

print("Based on this number, I predict you have approximately " + str(books_bookshelf(bookshelves)) + " books!")


# ----------------------------------------------------------------------------------------------

# Building and sorting an array.

def print_words(new_words_list):
    words_list = new_words_list
    word_input = input("Please enter one word to add to your list, or press Enter to finalise your list:  ")
    if word_input == "":
        print("Here is your sorted word list:  ")
        print(sorted(words_list))
    else:
        words_list.append(word_input)
        print_words(words_list)

print_words([])


# ----------------------------------------------------------------------------------------------

# Write a function that prints out "moo" n times.

def print_moo(n):
    for i in range(0, n):
        print("moo")

print_moo(3)


# ----------------------------------------------------------------------------------------------

# Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.
# I, II, III, IIII, V, VI, VII, VIII, VIIII, X, XI, XII, XIII, XIIII, XV ...
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

def old_roman_numeral_converter(num):
    number = num
    remaindar = 0
    old_roman_numeral = ""

    old_roman_numeral = old_roman_numeral + "M" * int((number / 1000))
    remaindar = number % 1000
    old_roman_numeral = old_roman_numeral + "D" * int((remaindar / 500))
    remaindar = number % 500
    old_roman_numeral = old_roman_numeral + "C" * int((remaindar / 100))
    remaindar = number % 100
    old_roman_numeral = old_roman_numeral + "L" * int((remaindar / 50))
    remaindar = number % 50
    old_roman_numeral = old_roman_numeral + "X" * int((remaindar / 10))
    remaindar = number % 10
    old_roman_numeral = old_roman_numeral + "V" * int((remaindar / 5))
    remaindar = number % 5
    old_roman_numeral = old_roman_numeral + "I" * int((remaindar / 1))

    print(old_roman_numeral)

old_roman_numeral_converter(3642)
# > MMMDCXXXXII

old_roman_numeral_converter(964)
# > DCCCCLXIIII

old_roman_numeral_converter(999)
# DCCCC LXXXX VIIII

old_roman_numeral_converter(444)
# CCCC XXXX IIII

# New-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.
# I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV ...

def new_roman_numeral_converter(num):
    number = num
    remaindar = 0
    new_roman_numeral = ""

    new_roman_numeral = new_roman_numeral + "M" * int((number / 1000))
    remaindar = number % 1000
    if remaindar >= 900:
        new_roman_numeral = new_roman_numeral + "CM"
        remaindar = number % 100
    else:
        new_roman_numeral = new_roman_numeral + "D" * int((remaindar / 500))
        remaindar = number % 500
    if remaindar >= 400:
        new_roman_numeral = new_roman_numeral + "CD"
        remaindar = number % 100
    else:
        new_roman_numeral = new_roman_numeral + "C" * int((remaindar / 100))
        remaindar = number % 100
    if remaindar >= 90:
        new_roman_numeral = new_roman_numeral + "XC"
        remaindar = number % 10
    else:
        new_roman_numeral = new_roman_numeral + "L" * int(remaindar / 50)
        remaindar = number % 50
    if remaindar >= 40:
        new_roman_numeral = new_roman_numeral + "XL"
        remaindar = number % 10
    else:
        new_roman_numeral = new_roman_numeral + "X" * int(remaindar / 10)
        remaindar = number % 10
    if remaindar == 9:
        new_roman_numeral = new_roman_numeral + "IX"
        remaindar = number % 1
    else:
        new_roman_numeral = new_roman_numeral + "V" * int(remaindar / 5)
        remaindar = number % 5
    if remaindar == 4:
        new_roman_numeral = new_roman_numeral + "IV"
    else:
        new_roman_numeral = new_roman_numeral + "I" * int(remaindar / 1)

    print(new_roman_numeral)

new_roman_numeral_converter(3642)
# > MMMDCXLII

new_roman_numeral_converter(964)
# > CM LX IV

new_roman_numeral_converter(999)
# CM XC IX

new_roman_numeral_converter(444)
# CD XL IV


#  ================ Week 1 Hackathon Challenge: Continent Counter ================================

import random
M = 'land'
o = 'water'

def create_wld(wld_sz):
    world = []
    for w in range(0,wld_sz):
        row = []
        i = 0
        while i < wld_sz:
            if random.randrange(2) == 0:
                tile = o
                row.append(tile)
                i = i + 1
            else:
                tile = M
                row.append(tile)
                i = i + 1
        world.append(row)
    print(world)
    return world

world_size_input = int(input('What size would you like your world to be? Please choose a number between 2 and 800.  '))

def check_sz(wld_sz_input):
    while wld_sz_input < 0 or wld_sz_input > 800:
        wld_sz_input = int(input('What size would you like your world to be? Please choose a number between 2 and 800. '))
    return wld_sz_input

wld_sz_fnl = check_sz(world_size_input)
world = create_wld(wld_sz_fnl)

x_coordinate = int(input('What "x" coordinate would you like to land on? You must choose a number between 0 and ' + str(wld_sz_fnl) + ":  "))

def check_x(wld_sz, x):
    while x < 0 or x > wld_sz:
        x = int(input('What "x" coordinate would you like to land on? You must choose a number between 0 and ' + str(wld_sz) + ":  "))
    return x

x_fnl = check_x(wld_sz_fnl, x_coordinate)

y_coordinate = int(input('What "y" coordinate would you like to land on? You must choose a number between 0 and ' + str(wld_sz_fnl) + ":  "))

def check_y(wld_sz, y):
    while y < 0 or y > wld_sz:
        y = int(input('What "y" coordinate would you like to land on? You must choose a number between 0 and ' + str(wld_sz) + ":  "))
    return y

y_fnl = check_y(wld_sz_fnl, y_coordinate)

def continent_counter(world, x, y):
    if x >= len(world) or x < 0 or y >= len(world) or y < 0:
        return 0
    if world[y][x] != 'land':
        return 0
    size = 1
    world[y][x] = 'counted land'

    # row above
    size = size + continent_counter(world, x-1, y-1)
    size = size + continent_counter(world, x  , y-1)
    size = size + continent_counter(world, x+1, y-1)

    # same row
    size = size + continent_counter(world, x-1, y  )
    size = size + continent_counter(world, x+1, y  )

    # row below
    size = size + continent_counter(world, x-1, y+1)
    size = size + continent_counter(world, x  , y+1)
    size = size + continent_counter(world, x+1, y+1)
    return size

your_continent = continent_counter(world, x_fnl, y_fnl)

print(your_continent)

print("The size of the continent you landed on at coordinates (" + str(x_fnl) + ", " + str(y_fnl) + ") is: " + str(your_continent) + " hectares")



# worldtest1 = [
#         [o,M,o],
#         [o,M,M]
#         ]
#
# worldtest2 = [
#          [o,o,o,o,o,o,o,o,o,o,o],
#          [o,o,o,o,M,M,o,o,o,o,o],
#          [o,o,o,o,o,o,o,o,M,M,M],
#          [o,o,o,M,o,o,o,o,o,M,o],
#          [o,o,o,M,o,M,M,o,o,o,o],
#          [o,o,o,o,M,M,M,M,o,o,o],
#          [o,o,o,M,M,M,M,M,M,M,o],
#          [o,o,o,M,M,o,M,M,M,o,o],
#          [o,o,o,o,o,o,M,M,o,o,o],
#          [o,M,o,o,o,M,o,o,o,o,o],
#          [o,o,o,o,o,o,o,o,o,o,o]
#         ]
# worldtest3 = [
#             [o,o,o,o,o,o,o,o,o,o,o],
#             [o,o,o,M,M,o,o,M,o,o,o],
#             [o,M,o,o,o,o,o,M,M,M,o],
#             [o,o,o,o,o,o,M,M,o,o,o],
#             [o,M,M,M,o,o,o,M,o,o,o],
#             [M,M,M,M,M,M,o,o,o,o,o],
#             [o,M,o,M,o,o,o,M,o,M,o],
#             [o,o,o,o,o,M,M,M,o,o,o],
#             [o,o,o,M,o,o,o,o,o,o,o],
#             [M,o,o,o,M,o,M,o,o,o,o],
#             [o,o,o,o,M,M,M,M,o,o,o]
#         ]

# print(continent_counter(worldtest1, 1, 0))  # 3
# print(continent_counter(worldtest2, 4, 1))  # 23
# print(continent_counter(worldtest3, 0, 6))  # 11
