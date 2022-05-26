# Nathan Zender
# Program # 3
# COMS-170-WWW02
# 09/28/2020
#-----------------------------------------------------------------------
# Variable               Type              Purpose
#-----------------------------------------------------------------------
#intAge                 Integer               Stores input age

print("         Genesee County Parks Fun Finder")

print(" ")

print("Enter your age for a fun experience recommendation:")

intAge = input()

intAge = int(intAge)

if (intAge <= 0) :
    print("Hey there partner, there might be an error.")
    
elif (intAge > 0 and intAge < 4) :
      print("Grab a seat on Thomas the Train at Huckleberry Railroad.")
      
elif (intAge >= 4 and intAge < 9) :
      print("The splash pad at Bluebell Beach is splashtastic!")
      
elif (intAge >= 9 and intAge < 16) :
      print("Toboggan Hill is packed full of winter fun!")
      
elif (intAge >= 16) :
      print("Crossroads Village is fun for adults and children.")

#Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#>>> 
#== RESTART: C:/Users/nzpan/Desktop/Computer Programming/Program 3/Program3.py ==
#         Genesee County Parks Fun Finder
 
#Enter your age for a fun experience recommendation:
#6
#The splash pad at Bluebell Beach is splashtastic!
#>>> 
#== RESTART: C:/Users/nzpan/Desktop/Computer Programming/Program 3/Program3.py ==
#         Genesee County Parks Fun Finder
 
#Enter your age for a fun experience recommendation:
#56
#Crossroads Village is fun for adults and children.
#>>> 
#== RESTART: C:/Users/nzpan/Desktop/Computer Programming/Program 3/Program3.py ==
#         Genesee County Parks Fun Finder
 
#Enter your age for a fun experience recommendation:
#1
#Grab a seat on Thomas the Train at Huckleberry Railroad.
#>>> 
