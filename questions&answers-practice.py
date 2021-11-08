#Question1....'Hello there, how old are you?-what index will return how old?
love = "Hello there, how old are you?"
love[13:20]
print(love[13:20])

""" 
You can actually reduce redundancy by printing directly 
Example: 
love = "Hello there, how old are you?"
print(love[13:20])

With this you have lesser lines of codes 
that does the same thing
"""


#Question2..."Python is awesome"..What is story[2:4] + story[-1]
story = "Python is awesome"
story[2:4]
story[-1]
print (story[2:4])
print (story[-1]) #kindly expalin more on this sir

"""
What this question wants to achieve is to solidify your
Knowledge in string concatenation.
So this solution will be:
print(story[2:4])
>>> 'th'
print(story[-1])
>>> 'e'
print(story[2:4] + story[-1])
# 'th' + 'e'
>>> 'the'

"""

#Question3...'mystring' = "Python rocks" - what is len(mystring)
mystring = 'Python rocks'
len(mystring)
print(len(mystring)) #12 is the answer

""" GOOD 👍 """

#Question4....flower = "Rose" what is flower [0]="P"; print (flower)? Will it return Pose?
flower = "Rose"
flower[0]
print(flower[0]) #QUESTION NOT CLEAR PLS

"""
IT EXPLAINS THE FACT THAT STRINGS ARE IMMUTABLE 
MEANING THAT YOU CAN CHANGE A VALUE OF ANY POSITIONAL
INDEX FROM ITS CONTENTS 

"""

#Question5....'Word = Python is so cool. What is word[-4:] * 3')
word = "Python is so cool"
word[-4:] * 3
print(word[-4:] * 3) #coolcoolcool is the answer

""" GOOD 👍 """

#Question6...Write a code that return "pepsi" as "PEPSI"
drink = "pepsi"
drink.upper()
print(drink.upper())

""" GOOD 👍 """

#Question7...Write a code that return 'macdonald' as 'MacDonald'
name = "mac donald"
name.title()
print(name.title()) #Please how can one achieve MacDonald without putting space in btwn?

"""
To achieve this you have to use the power of concatenation 
Let's split mac and donald and the one of Strings built-in method

.capitalize()
name = macdonald
first_name = name[:3]
print(first_name.capitalize())
>>> Mac
last_name = name[3:]
print(last_name.capitalize())
>>> Donald
full_name = first_name + last_name
>>> MacDonald


"""


#Question8....Write a code that return "MUSHRAH" as "mushrah"
name = "MUSHRAH"
name.lower()
print(name.lower())

""" GOOD 👍 """

#Question9....Using the built-in method, how will you "Hello Word" as a list?
x = ("Hello" "World")
len(x)
print(len(x))

""" GOOD 👍 """

#Question10....How do I add a "-" in between every character in a string "Python is cool"
sentence = "Python is cool"
my_sentence = '-'.join(sentence)
print(my_sentence)

""" GOOD 👍 """

my_sentence = '+'.join(sentence)
print(my_sentence)

my_sentence = '*'.join(sentence)
print(my_sentence)

my_sentence = '_'.join(sentence)
print(my_sentence)

""" GOOD 👍 """

#Question11 ...How do I remove "Hello" from "Hello World"
x = "Hello World"
x[0:5]
print (x[0:5])

""" GOOD 👍 """

#Question12....What is the index of the first character in a string?
answer = 0
print(f"The first index of the first character in a string is {answer}")

""" GOOD 👍 """

