# CONDITIONAL STATEMENTS:-
# A conditional statement in Python is used to make decisions in a program.
# It allows the program to execute different blocks of code depending on whether a condition is True or False.

# IF STATEMENT:-
# The if statement executes a block of code only when the condition is true.

# age=20
# if age>=18:
#     print("You are an Adult")

# marks=90
# if marks>=75:
#     print("You are in Grade A")

# num=10
# if num>=0:
#     print("num is positive")

# num=10
# if num%2==0:
#      print("num is even")

# temp=100
# if temp>=100:
#     print("Water starts to boil")

# num=3
# if num%2!=0:
#     print("num is odd")


# IF ELSE STATEMENT:-
# if-else statement is used when we want to make a decision between two possibilities.
# If the condition is True, execute the if block. Otherwise, execute the else block.

# marks=30
# if marks>=75:
#     print("You are a grade A student")
# else:
#     print("You are an average student")


# age=20
# if age>=18:
#     print("You are an Adult")
# else:
#     print("You are a minor")


# temp=40
# if temp>=30:
#     print("It's a Summer season")
# else:
#     print("It's a Winter season")

# num=10
# if num%2==0:
#     print("Even number")
# else:
#     print("Odd number")

# num=15
# if num%2!=0:
#     print("Odd number")
# else:
#     print("Even number")


# IF-ELIF-ELSE STATEMENT:-
# The if-elif-else statement is used when we have multiple conditions and want Python to choose one block of code based on those conditions.
# marks=95
# if marks>=90:
#     print("You are a Grade A student")
# elif marks>=75:
#     print("You are a Grade B student")
# elif marks>=60:
#     print("You are a Grade C student")
# else:
#     print("You are a Garde D student")

# age=65
# if age>=60:
#     print("You are a senior citizen")
# elif age>=35:
#     print("You are a Mature citizen")
# elif age>=18:
#     print("you are an adult")
# else:
#     print("You are a teenager")

# num=-1
# if num>0:
#     print("number is positive")
# elif num<0:
#     print("number is negative")
# else:
#     print("number is zero")

# temp=18
# if temp>=30:
#     print("It's a hot day")
# elif temp>=20:
#     print("It's a pleasant day")
# else:
#     print("It's a cold day")

# day="monday"
# if day=="monday":
#      print("start of the week")
# elif day=="Wednesday":
#     print("Weekdays")
# else:
#     print("Weekend")

# unit=600
# if unit<=100:
#     print("Low Usage")
# elif unit<=300:
#     print("Medium Usage")
# else:
#       unit>300
#       print("Excessive Usage")

# NESTED STATEMENT:-
# A nested statement means putting one statement inside another statement.
# When one control statement is written inside another control statement, it is called nesting.
# For example, an if statement inside another if statement is called a nested if statement.

# 1.NESTED-IF STATEMENT:-
# if statement inside another if statement is called a nested if statement.
# age=20
# citizen =True

# if age>=18:
#      print("You are an adult") -outer condition is true so inner condition will also give an output.
    
#      if citizen:
#           print("You are eligible to vote")

# num=10
# if num>0:
#     print("number is positive")
#     if num<0:
#         print("number is negative")


# marks=65
# if marks>=60:
#     print("You are in Grade B")
#     if marks>=65:
#         print("You are also an average student")

# temp=45
# if temp>=30:
#     print("It's a hot Day")
#     if temp>=40:
#         print("You are facing peak summer days")


# 2.NESTED IF-ELSE STATEMENT:-
# Nested if-else statement means an if-else statement is placed inside another if-else statement.
# age=20
# if age>=18:
#     print("You are an Adult")
#     if age>=18:
#         print("You can drive")
#     else:
#         print("You can't drive")
# else:
#     print("You are minor")


# username="Adarsh"
# password=1234
# if username=="Adarsh":
#     print("You have access ")
#     if password==1234:
#         print("You can login Successfully")
#     else:
#         print("You can't have access")
# else:
#     print("You can't login")

# temp=20
# season="Winter"
# if temp>=20:
#     print("It's a cold day")
#     if season=="Winter":
#         print("You have to wear a Jacket")
#     else:
#         print("You don't have to wear Jacket") 
# else:
#      print("It's not a cold day")  

# 3.NESTED IF-ELIF-ELSE STATEMENT:-
# A nested if-elif-else statement means putting one complete if-elif-else statement inside another if, elif, or else block.

# marks=85
# if marks>=40:
#     print("Student has passed")
#     if marks>=80:
#         print("Grade A")
#     elif marks>=60:
#         print("Grade B") 
#     else:
#         print("Grade C")  
# else:
#     print("Student has Failed")


# age=65
# if age>=60:
#     print("Senior citizen")
#     if age>=30:
#         print("Aware citizen")
#     elif age>=18:
#         print("Adult citizen")
#     else:
#         print("Minor")
# else:
#     print("Samll Boy")
