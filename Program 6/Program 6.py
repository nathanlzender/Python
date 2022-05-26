# Nathan Zender
# Program # 6
# COMS-170-XX
# 11/16/2020
#-----------------------------------------------------------------------
# Variable               Type              Purpose
#-----------------------------------------------------------------------
# menunumber            String              Determines when to re-run menu loop
# intcount              Integer             Stores the amount of file lines 
# inttotal              Integer             Stores the amount of the sum of the values in the file lines

def main():

    menunumber= "1"
    while menunumber != "x":
        Main_Menu()
        menunumber = input("Select option c,d, or x ")
        if menunumber =="c":
            DisplaySales()
        elif menunumber == "d":
            CalcTotal()
        elif menunumber == "x":
            print("You have closed the application")
            quit
        
def Main_Menu():
    print("*************************************************************************")
    print("POPCORN SALES")
    print("*************************************************************************")
    print("c: Display Sales")
    print("d: Calculate Totals")
    print("x: Exit application")

def DisplaySales():
    print("*************************************************************************")
    print("Popcorn Sales")
    print("*************************************************************************")
    fsalesdata = open('saledata.txt')
    intcount = 1
    for line in fsalesdata:
        line = line.rstrip()
        print(intcount,':', line)
        intcount = intcount + 1

def CalcTotal():
    print("*************************************************************************")
    print("Popcorn Totals")
    print("*************************************************************************")
    
    fsalesdata = open('saledata.txt')
    intcount = 0
    inttotal = 0
    for line in fsalesdata:
        intcount = intcount + 1
        inttotal = float(inttotal) + float(line)
    print("Total Popcorn Sales: ", str(round(inttotal,2)))
    print("Average Popcorn Sales: " , str(round(inttotal / intcount,2)))
   
main()

#*************************************************************************
#POPCORN SALES
#*************************************************************************
#c: Display Sales
#d: Calculate Totals
#x: Exit application
#Select option c,d, or x c
#*************************************************************************
#Popcorn Sales
#*************************************************************************
#1 : 50
#2 : 17.32
#3 : 32.99
#4 : 51.02
#5 : 15.61
#6 : 23.94
#7 : 5.99
#8 : 12.1
#9 : 62.74
#10 : 105.59
#11 : 16.50
#12 : 32.99
#13 : 23.71
#14 : 54.90
#15 : 19
#16 : 17.52
#17 : 48.6
#18 : 102
#19 : 99.99
#20 : 73.05
#21 : 50
#22 : 17.32
#23 : 32.99
#24 : 51.02
#25 : 15.61
#26 : 23.94
#27 : 5.99
#28 : 12.1
#29 : 62.74
#30 : 105.59
#31 : 16.50
#32 : 32.99
#33 : 23.71
#34 : 54.90
#35 : 19
#36 : 17.52
#37 : 48.6
#*************************************************************************
#POPCORN SALES
#*************************************************************************
#c: Display Sales
#d: Calculate Totals
#x: Exit application
#Select option c,d, or x d
#*************************************************************************
#Popcorn Totals
#*************************************************************************
#Total Popcorn Sales:  1456.08
#Average Popcorn Sales:  39.35
#*************************************************************************
#POPCORN SALES
#*************************************************************************
#c: Display Sales
#d: Calculate Totals
#x: Exit application
#Select option c,d, or x x
#You have closed the application
