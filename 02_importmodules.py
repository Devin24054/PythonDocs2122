#import the basics module to use its code
import basics


# make a new application object from the bascis module
app = basics.newProgram()

#use a method that belongs to our new application object
app.print("yo momma")

#print a property of our new application object
app.print( app.debugging )

#this line won't print if app.debugging = false
app.debug('Hello')

# we'l enable debugging for the application
app.debugging=True

app.debug('now it works')

#import a default python module
import random

#use a method from the random module
randomNumber = random.randint(1,10)

app.print(randomNumber)

