# Nathan Zender
# Program # 5
# COMS-170-XX
# 10/02/2020
#-----------------------------------------------------------------------
# Variable               Type              Purpose
#-----------------------------------------------------------------------
# menunumber            String              Determines when to re-run menu loop
# fltjumpers            Float               Stores the inputted amount of jumpers
# fltjumphours          Float               Stores the inputted amount of jump hours
# flttotalcost          Float               Stores total cost of jump
# fltservicefee         Float               Stores Service Fee
# fltsubtotal           Float               Stores subtotal cost

def main():

    menunumber= "1"
    while menunumber != "x":
        Main_Menu()
        menunumber = input("Select option c,d, or x ")
        if menunumber =="c":
            CalculateAdmission()
        elif menunumber == "d":
            DisplayFees()
        elif menunumber == "x":
            print("Thank you for coming to Jumpers Adventure Zone")
            quit
        
def Main_Menu():
    print("*************************************************************************")
    print("Jumpers Adventure Zone")
    print("*************************************************************************")
    print("c: Calculate admission cost")
    print("d: Display admission options")
    print("x: Exit application")

def DisplayFees():
    print("*************************************************************************")
    print("Admission Options")
    print("*************************************************************************")
    print("1.0 Hours         $14.00")
    print("1.5 Hours         $17.00")
    print("2.0 Hours         $20.00")

def CalculateAdmission():
    subtotal = 0
    flttotalcost = 0
    print("*************************************************************************")
    print("Jumpers Cost")
    print("*************************************************************************")
    fltjumpers = input("How many are jumping today? ")
    fltjumphours = input("How many hours would you like to jump? ")
    fltjumphours = float(fltjumphours)
    
    if fltjumphours == 1:
        fltjumpers = float(fltjumpers)
        flttotalcost = fltjumpers*14
        flttotalcost = float(flttotalcost)
        CalcServiceFee(flttotalcost)

    elif fltjumphours == 1.5:
        fltjumpers = float(fltjumpers)
        flttotalcost = fltjumpers*17
        flttotalcost = float(flttotalcost)
        CalcServiceFee(flttotalcost)

    elif fltjumphours == 2.0:
        fltjumpers = float(fltjumpers)
        flttotalcost = fltjumpers*20
        flttotalcost = float(flttotalcost)
        CalcServiceFee(flttotalcost)

def CalcServiceFee(flttotalcost):
    fltservicefee = 0
    fltservicefee = float(fltservicefee)
    fltservicefee = flttotalcost * .08
    flttotalcost = fltservicefee + flttotalcost
    print("The cost of admission would be " + str(round(flttotalcost,2)) + "$")
      
main()

#*************************************************************************
#Jumpers Adventure Zone
#*************************************************************************
#c: Calculate admission cost
#d: Display admission options
#x: Exit application
#Select option c,d, or x d
#*************************************************************************
#Admission Options
#*************************************************************************
#1.0 Hours         $14.00
#1.5 Hours         $17.00
#2.0 Hours         $20.00
#*************************************************************************
#Jumpers Adventure Zone
#*************************************************************************
#c: Calculate admission cost
#d: Display admission options
#x: Exit application
#Select option c,d, or x c
#*************************************************************************
#Jumpers Cost
#*************************************************************************
#How many are jumping today? 3
#How many hours would you like to jump? 1.5
#The cost of admission would be 55.08$
#*************************************************************************
#Jumpers Adventure Zone
#*************************************************************************
#c: Calculate admission cost
#d: Display admission options
#x: Exit application
#Select option c,d, or x c
#*************************************************************************
#Jumpers Cost
#*************************************************************************
#How many are jumping today? 1
#How many hours would you like to jump? 1
#The cost of admission would be 15.12$
#*************************************************************************
#Jumpers Adventure Zone
#*************************************************************************
#c: Calculate admission cost
#d: Display admission options
#x: Exit application
#Select option c,d, or x c
#*************************************************************************
#Jumpers Cost
#*************************************************************************
#How many are jumping today? 12
#How many hours would you like to jump? 2
#The cost of admission would be 259.2$
#*************************************************************************
#Jumpers Adventure Zone
#*************************************************************************
#c: Calculate admission cost
#d: Display admission options
#x: Exit application
#Select option c,d, or x x
#Thank you for coming to Jumpers Adventure Zone

