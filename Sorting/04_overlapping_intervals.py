# Overlapping Intervals

class Solution:
	def mergeOverlap(self, arr):
		n = len(arr)
		res = []
		
		arr.sort()
		
		res.append(arr[0])
		for i in range(1, n):
		    
		    left = arr[i][0]
		    right = arr[i][1]
		    
		    if (left <= res[-1][1]):
		        res[-1][1] = max(res[-1][1], right)
		        
		    else:
		        res.append([left, right])
		    
		return res
