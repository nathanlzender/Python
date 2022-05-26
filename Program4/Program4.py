# Nathan Zender
# Program # 4
# COMS-170-XX
# 10/18/2020
#-----------------------------------------------------------------------
# Variable               Type              Purpose
#-----------------------------------------------------------------------
# fltRandomnumber       Float           Stores random number
# fltGuessnumber        Float           Stores the number the student guesses
# fltGuessamount        Float           Stores the amount of guesses the student has made
# fltLoopcontrol        Float           Controls the loop

import random

fltRandomnumber = random.randint(1,100)

fltGuessnumber = 0

fltGuessamount =  0

fltLoopcontrol = 0

while (fltLoopcontrol == 0):
    print("Guess a number from 1 to 100")
    fltGuessamount = fltGuessamount + 1
    fltGuessnumber = input()
    fltGuessnumber = float(fltGuessnumber)
    
    if fltGuessnumber == fltRandomnumber:
        print("You guessed correctly")
        print("You guessed " + str(fltGuessamount) + " times")
        print("Thanks for playing")
        fltLoopcontrol = 1

    elif fltGuessnumber < fltRandomnumber:
        print("You guessed too low")

    elif fltGuessnumber > fltRandomnumber:
        print("You guessed too high")

#Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#>>> 
#=== RESTART: C:\Users\nzpan\Desktop\Computer Programming\Program4\Program4.py ==
#Guess a number from 1 to 100
#50
#You guessed too high
#Guess a number from 1 to 100
#25
#You guessed too high
#Guess a number from 1 to 100
#12
#You guessed too low
#Guess a number from 1 to 100
#17
#You guessed too low
#Guess a number from 1 to 100
#21
#You guessed correctly
#You guessed 5 times
#Thanks for playing
#>>> 
