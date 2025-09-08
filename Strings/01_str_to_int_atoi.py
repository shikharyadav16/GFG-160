# String to integer (your own atoi)

def myAtoi(self, s):
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    index = 0
    while (index < len(s) and s[index] == " "):
        index += 1
        
    sign = 1
    if (index < len(s) and (s[index] == "+" or s[index] == "-")):
        if (s[index] == "-"):
            sign = -1
        index += 1
        
    res = 0
    while (index < len(s) and "0" <= s[index] <= "9"):
        res = 10*res + (ord(s[index]) - ord("0"))
        if (res > MAX_INT and sign == -1):
            return MIN_INT
        elif (res > MAX_INT and sign == 1):
            return MAX_INT
        index += 1
            
    return res*sign

s = input("Enter the string: ")
print("Number is:", myAtoi(s))
