# First non repeating character

def nonRepeatingChar(s):
    temp = [-1]*26

    for i in range(len(s)):
        index = ord(s[i]) - ord("a")

        if (temp[index] == -1):
            temp[index] = i
        else:
            temp[index] = -2

    l = [x for x in temp if x >= 0]

    return -1 if len(l) == 0 else s[min(l)]
            

s = input("Enter the string: ")
print("First non repeating character is:", nonRepeatingChar(s))
