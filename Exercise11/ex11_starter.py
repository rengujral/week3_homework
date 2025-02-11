#!/usr/bin/python

# pre-existing string taken from example provided with details about Belgium
# print variable
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)

# character_count variable established to find character count using len() function
# print character count
character_count = len(Belgium)
print(character_count)

# print hyphens to match the character length of the previous variable by multiplying them by 81
print("-" * 81)

# alt method:
# print(Belgium.replace(",",":"))
# Belgium_list = ['Belgium', '10445852','Brussels','737966','Europe','1830','Euro','Catholicism','Dutch','French','German']

# using string method .split turn the substrings within string Belgium into a list
# print list
Belgium_list = Belgium.split(",")
print(Belgium_list)

# method .join concatenates list of substrings back into a single string, separated by ":" instead of ","
# calls on the string ":" to insert itself between each substring
print(":".join(Belgium_list))

# finding the total population of Belgium and its capital
# population of Belgium is the second substring, thus [1] (python counts up from 0)
# population of Brussels is the fourth substring, thus [3]
# int function converts values from strings into integers before finding total
# print final value of total_popu variable
total_popu = int(Belgium_list[1]) + int(Belgium_list[3])
print(total_popu)