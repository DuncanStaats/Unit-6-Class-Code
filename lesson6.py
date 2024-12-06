"""
Name: Duncan Staats
Date: 12/5/2024
description: Strings
"""

#upper case
name = "starla"
print(name.upper())
print(name)

name = name.upper()
print(name)

#lower case
name = "FRANKLIN"
print(name.lower())

#title case
sentence = "FRANKLIN LEAVE MILLIE ALONE"
print(sentence.title())

#swap case
word = "ViOlIn"
print(word.swapcase())

#strip
school = "         Oregon State       University       "
print(school.strip())

#find: return index of first occurence 
print("Oregon State University".find("go"))

##########################################

# Boolean checks
print("b".isupper())
print("b".islower())
print("b".isalpha())
print("b".isalnum())
print("b".isdigit())