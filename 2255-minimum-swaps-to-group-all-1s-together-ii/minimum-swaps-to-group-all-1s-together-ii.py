class Solution:
    def minSwaps(self, nums):
        total_ones = sum(nums)
        if total_ones <= 1:
            return 0
        
        n = len(nums)
        max_ones = 0
        curr_ones = 0
        
        left = 0
        
        # Sliding window over circular array
        for right in range(n * 2):
            curr_ones += nums[right % n]
            
            # Maintain window size = total_ones
            if right - left + 1 > total_ones:
                curr_ones -= nums[left % n]
                left += 1
            
            max_ones = max(max_ones, curr_ones)
        
        return total_ones - max_ones
        