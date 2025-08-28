def maxProfit(arr, n):
    profit = 0
    
    for i in range(1, n):
        if (arr[i] > arr[i-1]):
            profit += arr[i] - arr[i-1]
    return profit

n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))
    
print("Total profit:", maxProfit(arr, n))
    
