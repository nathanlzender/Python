# Nathan Zender
# Program # 7
# COMS-170-XX
# 11/23/2020
#-----------------------------------------------------------------------
# Variable               Type              Purpose
#-----------------------------------------------------------------------
#intloop                integer             Controls when loop stops
#listTestscores         list                Stores students scores in a list
#intcurrentgrade        integer             Stores students scores temporarily
#intlistnumber          integer             Counter for final score display

intloop = 0
listTestscores = list()

def main():
    intcurrentgrade = 0
    intcurrentgrade = input("Enter test score or -1 to calculate totals: ")
    intcurrentgrade = int(intcurrentgrade)
    if intcurrentgrade == -1:
        global intloop
        intloop = 1
        print("Highest Score:" , max(listTestscores))
        print("Lowest Score:" , min(listTestscores))
        print("Average Score:" , int(sum(listTestscores)/len(listTestscores)))
        print("Test Scores")
        intlistnumber = 0
        for i in listTestscores:
            intlistnumber = intlistnumber + 1
            print(str(intlistnumber) + ": " + str(i))

    else:
        listTestscores.append(intcurrentgrade)
        
while intloop == 0:
    main()

"""
== RESTART: C:/Users/nzpan/Desktop/Computer Programming/Program 7/Program 7.py =
Enter test score or -1 to calculate totals: 94
Enter test score or -1 to calculate totals: 87
Enter test score or -1 to calculate totals: 95
Enter test score or -1 to calculate totals: 62
Enter test score or -1 to calculate totals: 90
Enter test score or -1 to calculate totals: 84
Enter test score or -1 to calculate totals: -1
Highest Score: 95
Lowest Score: 62
Average Score: 85
Test Scores
1: 94
2: 87
3: 95
4: 62
5: 90
6: 84
>>> 
== RESTART: C:/Users/nzpan/Desktop/Computer Programming/Program 7/Program 7.py =
Enter test score or -1 to calculate totals: 72
Enter test score or -1 to calculate totals: 90
Enter test score or -1 to calculate totals: 83
Enter test score or -1 to calculate totals: 91
Enter test score or -1 to calculate totals: -1
Highest Score: 91
Lowest Score: 72
Average Score: 84
Test Scores
1: 72
2: 90
3: 83
4: 91
>>> 
== RESTART: C:/Users/nzpan/Desktop/Computer Programming/Program 7/Program 7.py =
Enter test score or -1 to calculate totals: 55
Enter test score or -1 to calculate totals: 72
Enter test score or -1 to calculate totals: 100
Enter test score or -1 to calculate totals: 81
Enter test score or -1 to calculate totals: 70
Enter test score or -1 to calculate totals: 89
Enter test score or -1 to calculate totals: -1
Highest Score: 100
Lowest Score: 55
Average Score: 77
Test Scores
1: 55
2: 72
3: 100
4: 81
5: 70
6: 89
"""
