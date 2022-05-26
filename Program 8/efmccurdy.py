strLoopset = "y"

def Main():
    global strLoopset
    strInputsentence = input("Enter sentences to be modified: ")

    strSentencesplit = str

    strSentencesplit = strInputsentence.split(".")
    
    print(strSentencesplit)

    strFinishedsentence_l = [s.capitalize() for s in strSentencesplit]
    
    strFinishedsentence = ".".join(strFinishedsentence_l)

    print("Your modified sentence is: " +  strFinishedsentence)

    
    global strLoopset
    strLoopset = input("Enter 'y' to try again....")

while strLoopset == "y":
    Main()



exit
