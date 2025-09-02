# Maximum sum subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = nums[0]
        maxSum = nums[0]
        minSum = nums[0]
        currMax = nums[0]
        currMin = nums[0]
        
        for i in range(1, len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            maxSum = max(maxSum, currMax)

            currMin = min(currMin + nums[i], nums[i])
            minSum = min(minSum, currMin)

            totalSum += nums[i]

        if (totalSum == minSum):
            return maxSum
        return max(maxSum, (totalSum - minSum))
