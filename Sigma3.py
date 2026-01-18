def romanToInt(romanInput):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # rsult 
    resultInteger = 0

    # go from 0 to len-1 if inteager equivalent is greater than next elemant then add it else subtract it




    for i in range(0,len(romanInput) -1):
        if roman[romanInput[i]] <= roman[romanInput[i + 1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]
        return resultInteger + roman[romanInput[-1]]
    








# take roman input from the user
roman = input("input roman numeral ")

print("The integer value is ", romanToInt(roman))