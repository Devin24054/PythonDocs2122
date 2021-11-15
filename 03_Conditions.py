# Devin Cook
#practice using expressions and conditional statements
# an expression is a problem that must be solved
# 5+5 is a 'arithmetic' expression
x= 5+5
#functions,methods must be solved as expressions as well
answer=input("What is your name")

#comparison expressions resolve as true or false
print (7>7)

# a conditional statements runs if it's conditions is true/false
if answer== "Bob":
    print ("hello bob")
    print("this line also prints if your name is bob")
elif answer== "Vadim":
    print("Hey! You still owe me money, vadim")
else:
    print("Get Away,Weirdo")
# ^ if checks a condition
# ^ elif checks a condition if the previous conditions weren't true
# ^ else runs if no prior conditions were true
# ^ you can have as many elif's as you want only one else and one if




age= input("what is your age")

age= int(age)


if age >= 10:
     print("Here is your pokemon license")
elif age ==9:
    print("You're too young, you have one more year")
else:
    print("You are too young")



