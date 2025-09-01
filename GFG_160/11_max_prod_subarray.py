# Maximum Product of subarray

def maxProdSubArray(arr, n):
    maxProd = float("-inf")
    ltor = 1
    rtol = 1
    
    for i in range(n):
        if (ltor == 0):
            ltor = 1
        if (rtol == 0):
            rtol = 1
            
        ltor *= arr[i]
        rtol *= arr[n-i-1]
        
        maxProd = max(maxProd, ltor, rtol)
    return maxProd

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input()))
    
print("Maximum product is:", maxProdSubArray(arr, n))
