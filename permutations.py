class Solution(object):
    def permute(self, nums):
        x = len(nums)
        while x>0:
            y=x*(x-1)
            print(y)
            x = x-1



# list = [nums[len(nums)-1], nums[len(nums)-2], nums[len(nums)-3]]
# list2 = [nums[len(nums)-3], nums[len(nums)-2], nums[len(nums)-1]]
# print([list]+[list2])


            
solution = Solution()
result = solution.permute([1, 3, 4,3])
print(result)
        