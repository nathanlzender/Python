# Nathan Zender
# Program #8
# COMS-170-XX
# 11/28/2020
#-----------------------------------------------------------------------
# Variable               Type              Purpose
#-----------------------------------------------------------------------
#strLoopset             string          Controls Loop
#strInputsentence       string          First Variable for user input
#words                  list            Stores split input sentence
#uncapitalizedStrings   list            Stores split sentence
#tempString             string          Stores capital words
#finalString            string          Output variable
#charTempString         string          Stores character for capitilization

strLoopset = "y"

def Main():
    global strLoopset
    strInputsentence = input("Enter sentences to be modified: ")
    
    words = strInputsentence.split('.')

    uncapitalizedStrings = words[:-1]
                            
    tempString = str
    tempString = words[0]
    
    finalString = tempString[0].capitalize()
    tempString = tempString[1:]
    finalString = finalString + tempString
    finalString = finalString + ". "

    uncapitalizedStrings = uncapitalizedStrings[1:]
    
    charTempString = str
    
    for string in uncapitalizedStrings:
        
        string = string[1:]
        charTempString = string[0].capitalize()
        finalString = finalString + str(string[0].capitalize())
        string = string[1:]
        finalString = finalString + string
        finalString = finalString + ". "


    print("Your modified sentence is: " +  finalString)

    
    global strLoopset
    strLoopset = input("Enter 'y' to try again....")

while strLoopset == "y":
    Main()

exit

#== RESTART: C:\Users\nzpan\Desktop\Computer Programming\Program 8\Program 8.py =
#Enter sentences to be modified: my name is Samantha. i go to Mott Community College.
#Your modified sentence is: My name is Samantha. I go to Mott Community College. 
#Enter 'y' to try again....y
#Enter sentences to be modified: my favorite character is Charlie Brown. he is a great sport.
#Your modified sentence is: My favorite character is Charlie Brown. He is a great sport. 
#Enter 'y' to try again....y
#Enter sentences to be modified: programming in Python is super FUN. i can't wait to learn more.
#Your modified sentence is: Programming in Python is super FUN. I can't wait to learn more. 
#Enter 'y' to try again....x
#>>>
