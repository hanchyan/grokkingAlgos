# accepted by leet
class Solution(object):
    def twoSum(self, nums, target):
        x = 0

        while x < len(nums):
            for i in range(len(nums)):  # i is now an index (0, 1, 2...)
                if i == x:
                    continue
                check = nums[i] + nums[x]  # Now nums[i] is valid
                if check == target:
                    return(x, i)
            x += 1  

        print(target)

solution = Solution()
result = solution.twoSum([1, 3, 4, 5, 6], 9)
print(result)
