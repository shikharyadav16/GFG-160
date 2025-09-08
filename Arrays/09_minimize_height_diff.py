# Minimize height difference 2

def getDifference(arr, n, k):
    arr.sort()
    res = arr[n-1] - arr[0]
    
    for i in range(1, n):
        if (arr[i]-k < 0):
            continue
        minH = min(arr[0]+k, arr[i]-k)
        maxH = max(arr[n-1]-k, arr[i-1]+k)
        
        res = min(res, maxH-minH)
        
    return res

n = int(input("Enter the number of elements: "))
k = int(input("Enter the number to do operation: "))
arr = []
for i in range(n):
    arr.append(int(input()))
    
print("Minimum difference is", getDifference(arr, n, k))
