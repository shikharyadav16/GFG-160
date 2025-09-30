# Sort 0s, 1s and 2s

class Solution:
    def sort012(self, arr):
        
        c1 = c2 = 0
        c3 = len(arr) - 1
        
        while (c2 != c3+1):
            
            if (arr[c2] == 0):
                arr[c1], arr[c2] = arr[c2], arr[c1]
                c1 += 1
                c2 += 1
                
            elif (arr[c2] == 1):
                c2 += 1
            
            else:
                arr[c3], arr[c2] = arr[c2], arr[c3]
                c3 -= 1

        return arr
        
        
