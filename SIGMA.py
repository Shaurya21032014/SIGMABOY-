# progrm to find if a number is rmstrong 
number = int(input("input ur number "))
# cslculate number of the digits 
digits =len(str(number))


# intilazing result varialble
resultNumber= 0

# find the sum of the a^digits of the each

temp = number
while temp > 0:
    digits = temp% 10
    resultNumber += digits **  digits
    temp //= 10

# display the result 
if number == resultNumber:
    print(number, "is a armstrong number ")

else:
    print(number, " is not armstrong number ")