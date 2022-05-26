# Nathan Zender
# Program # 1
# COMS-170-XX
# 09/21/2020
#-----------------------------------------------------------------------
# Variable               Type              Purpose
#-----------------------------------------------------------------------
#fltRetailprice         Float           Stores retail price
#fltSaleprice           Float           Stores sales price
#fltTax                 Float           Stores tax price
#fltFinalprice          Float           Stores final price

#Asks for user input
print("Please enter retail price")

#Sets retail price value to input price
fltRetailprice = input()

#Converts input price of retail price to float value
fltRetailprice = float(fltRetailprice)

#Calcultes saleprice and stores it as sale price variable
fltSaleprice = fltRetailprice - (fltRetailprice * .20)

#Calculates tax and stores it in variable
fltTax = fltSaleprice * .06

#Calculates final price and stores it in variable
fltFinalprice = fltTax + fltSaleprice

#Converts retail price variable to string
fltRetailprice = str(fltRetailprice)

#Converts sale price variable to string
fltSaleprice= str(fltSaleprice)

#Converts Tax price variable to string
fltTax= str(fltTax)

#Converts Final price variable to string
fltFinalprice = str(fltFinalprice)

#Displays retail price to screen
print("Retail Price = " + fltRetailprice + "$")

#Displays sale price to screen
print("Sale Price = " + fltSaleprice + "$")

#Displays tax price to screen
print("Tax price = " + fltTax + "$")

#Displays final price to screen
print("Final price = " + fltFinalprice + "$")
