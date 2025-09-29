# Check Anagram

def checkAnagram(s1, s2):
    temp = {}


    for i in range(len(s1)):
        temp[s1[i]] = temp.get(s1[i], 0) + 1

    for i in range(len(s2)):
        temp[s2[i]] = temp.get(s2[i], 0) - 1

    for val in temp.values():
        if (val != 0):
            return False
    return True

s1 = input("Enter string 1:")
s2 = input("Enter string 2:")

if (checkAnagram(s1, s2)):
    print("It is Anagram")
else:
    print("It is not Anagram")
    
