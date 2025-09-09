# Addition of two string binary number not leading zero
def trimExtraZeros(s):
    firstOne = s.find("1")
    return s[firstOne:] if (firstOne != -1) else "0"

def addBinary(s1, s2):
    s1 = trimExtraZeros(s1)
    s2 = trimExtraZeros(s2)

    n = len(s1)
    m = len(s2)
    if (n < m):
        s1, s2 = s2, s1
        n, m = m, n

    j = m-1
    carry = 0
    res = []
    for i in range(n-1, -1, -1):
        bit1 = int(s1[i])
        bitSum = bit1 + carry

        if (j != -1):
            bit2 = int(s2[j])
            bitSum += bit2
            j -= 1

        bit = str(bitSum % 2)
        carry = bitSum // 2

        res.append(bit)

    if (carry == 1):
        res.append("1")
    return "".join(res[::-1])

s1 = input("Enter the string 1: ")
s2 = input("Enter the string 2: ")

print(addBinary(s1, s2))
