class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare middle with the rightmost element
            if nums[mid] < nums[right]:
                right = mid  # Minimum is in the left part
            elif nums[mid] > nums[right]:
                left = mid + 1  # Minimum is in the right part
            else:
                # nums[mid] == nums[right], reduce right to skip duplicates
                right -= 1
        
        return nums[left]
