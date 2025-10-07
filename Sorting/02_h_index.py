# Find H-Index

class Solution:
    def hIndex(self, citations):
        n = len(citations)
        freq = [0]*(n+1)
        s = 0
        
        for i in range(n):
            
            if (citations[i] >= n):
                freq[n] += 1
            
            else:    
                freq[citations[i]] += 1
            
        for i in range(n, -1, -1):
            
            s += freq[i]
            if (s >= i):
                return i
                
        return 0
