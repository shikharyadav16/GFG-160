def maxSubArray(arr, n):
    maxSum = arr[0]
    res = arr[0]
    for i in range(1, n):
        maxSum = max(arr[i]+maxSum, arr[i])
        res = max(res, maxSum)
    return res

n = int(input("Enter the number of elements: "))
print("Enter the elements: ")

arr = []
for i in range(n):
    arr.append(int(input()))

print("Maximum sum of subarray is:", maxSubArray(arr, n))
