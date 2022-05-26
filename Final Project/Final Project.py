# Nathan Zender
# Final Project
# COMS-170-XX
# 12/08/2020
#-----------------------------------------------------------------------
# Variable               Type              Purpose
#-----------------------------------------------------------------------
#setloop                integer             controls while loop
#fltfinalcharge         float               holds value for final cost
#intdaysrented          integer             holds value for the amount of days rented
#intmilesdriven         integer             holds value for the amount of miles rented
#intweeksrented         integer             holds value for the amount of weeks rented
#strclassification      string              holds the truck classification letter
#strtimerented          string              holds amount of time rented
#whileloopcontrol       integer             controls while loop
#loopset2               integer             controls while loop
#loopset3               integer             controls while loop
#truckrentallist        list                list that holds the startup menu sentences


setloop = 1

def totalcharge(strclassification,strtimerented,intdaysrented,intmilesdriven,intweeksrented):
    fltfinalcharge = 0
    fltfinalcharge = float(fltfinalcharge)
    intdaysrented = float(intdaysrented)
    intmilesdriven = float(intmilesdriven)
    intweeksrented = float(intweeksrented)

    if strclassification == "A":
        if strtimerented == "Daily":
            fltfinalcharge = (17.95 * intdaysrented) + (0.49 * intmilesdriven)
            print("your total is: ", str(round(fltfinalcharge,2)))

        if strtimerented == "Weekly":
            x = (intmilesdriven - 200)
            
            if x < 0:
                x = 0
                fltfinalcharge = (107.79*intweeksrented) + (x*0.49)
                print("your total is: ", str(round(fltfinalcharge,2)))
        
            else:
                
                fltfinalcharge = (107.79*intweeksrented) + (x*0.49)
                print("your total is: ", str(round(fltfinalcharge,2)))


    elif strclassification =="B":
        if strtimerented == "Daily":
            fltfinalcharge = (27.95 * intdaysrented) + (0.69 * intmilesdriven)
            print("your total is: ", str(round(fltfinalcharge,2)))

        if strtimerented == "Weekly":
            x = (intmilesdriven - 200)
            
            if x < 0:
                x = 0
                fltfinalcharge = (166.59*intweeksrented) + (x*0.69)
                print("your total is: ", str(round(fltfinalcharge,2)))
        
            else:
                
                fltfinalcharge = (166.59*intweeksrented) + (x*0.69)
                print("your total is: ", str(round(fltfinalcharge,2)))
        

    elif strclassification=="C":
        if strtimerented == "Daily":
            fltfinalcharge = (37.95 * intdaysrented) + (0.79 * intmilesdriven)
            print("your total is: ", str(round(fltfinalcharge,2)))

        if strtimerented == "Weekly":
            x = (intmilesdriven - 200)
            
            if x < 0:
                x = 0
                fltfinalcharge = (237.99*intweeksrented) + (x*0.79)
                print("your total is: ", str(round(fltfinalcharge,2)))
        
            else:
                
                fltfinalcharge = (237.99*intweeksrented) + (x*0.79)
                print("your total is: ", str(round(fltfinalcharge,2)))
    

def main():
    intdaysrented = 0
    intmilesdriven = 0
    intdaysrented = 0
    intweeksrented = 0
    strclassification = "D"
    strtimerented = "N/A"
    whileloopcontrol = 1

#---------------------------------------------------------------------------------------------------------------------------------------
    truckrentallist =("-------------------------------------------------------------------","Truck Rental","-------------------------------------------------------------------")
    for i in truckrentallist:
        print(i)
    
    print("What classification of truck are you going to be renting?")
    print("Class A")
    print("Class B")
    print("Class C")
    while whileloopcontrol != 0:
        strclassification = input("Please choose A,B,or C: ")
        strclassification = strclassification.upper()
        
        if strclassification == "A" or strclassification == "B" or strclassification == "C" :
            whileloopcontrol = 0
        else:
            print("You entered an invalid class, try entering the class again")
    
#---------------------------------------------------------------------------------------------------------------------------------------    
    print("How long are you going to be renting?")
    print("Daily or Weekly")
    while strtimerented != "Daily" and strtimerented != "Weekly":
        strtimerented = input("Please enter Daily or Weekly: ")
        strtimerented = strtimerented.capitalize()
        loopset2 = 0
        loopset3 = 0

        if strtimerented == "Daily":
            while loopset2 == 0:
                intdaysrented = input("How many days are you going to be renting? ")
                if intdaysrented.isdigit():
                    loopset2 = 1
                    
                else:
                    print("You entered an invalid number/ character ")
                    
            while loopset3 == 0:
                        
                intmilesdriven = input("How many miles are you going to drive? ")
                if intmilesdriven.isdigit():
                    loopset3 = 1
                    totalcharge(strclassification,strtimerented,intdaysrented,intmilesdriven,intweeksrented)
                            
                else:
                    print("You entered an invalid number/ character ")
            

        
        elif strtimerented == "Weekly":
            while loopset2 == 0:
                intweeksrented = input("How many weeks are you going to be renting? ")
                if intweeksrented.isdigit():
                    loopset2 = 1
                    
                else:
                    print("You entered an invalid number/ character ")
                    
            while loopset3 == 0:
                        
                intmilesdriven = input("How many miles are you going to drive? ")
                if intmilesdriven.isdigit():
                    loopset3 = 1
                    totalcharge(strclassification,strtimerented,intdaysrented,intmilesdriven,intweeksrented)
                            
                else:
                    print("You entered an invalid number/ character ")
                    
            
            
        else:
            print("You entered an invalid selection, try entering the selection again")
    
#---------------------------------------------------------------------------------------------------------------------------------------    
while setloop != 0:
    main()

#-------------------------------------------------------------------
#Truck Rental
#-------------------------------------------------------------------
#What classification of truck are you going to be renting?
#Class A
#Class B
#Class C
#Please choose A,B,or C: b
#How long are you going to be renting?
#Daily or Weekly
#Please enter Daily or Weekly: daily
#How many days are you going to be renting? 2
#How many miles are you going to drive? 130
#your total is:  145.6
#-------------------------------------------------------------------
#Truck Rental
#-------------------------------------------------------------------
#What classification of truck are you going to be renting?
#Class A
#Class B
#Class C
#Please choose A,B,or C: c
#How long are you going to be renting?
#Daily or Weekly
#Please enter Daily or Weekly: weekly
#How many weeks are you going to be renting? 1
#How many miles are you going to drive? 210
#your total is:  245.89

