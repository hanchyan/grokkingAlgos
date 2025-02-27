# accepted by leet
class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 1:  # Ensure i+1 is always valid
            if nums[i] == nums[i + 1]:  
                nums.pop(i)  # Remove duplicate
            else:
                i += 1  # Move forward only when no removal happens
        return len(nums)

solution = Solution()
result = solution.removeDuplicates([1, 1, 2, 2, 3, 3, 4])
print(result)  # Should print the new length of the list
