# accepted by leet
class Solution(object):
    def searchInsert(self, nums, target):
        myList = []
        for i in range(len(nums)):
            if nums[i] == target:
                myList.append(nums[i])
                return(nums.index(nums[i]))
            else:
                i += 1 
        if not myList:
            for i in range(len(nums)):
                if len(nums) == 1 and target> nums[i]:
                    return(1)
                elif (nums[i] < target and nums[i+1] > target):
                    return(i+1)
                elif nums[i] > target:
                    return(i)
                elif nums[len(nums)-1] < target:
                    return len(nums)
                    # return(10)
                elif len(nums)== 1 and target< nums[0]:
                    return(0)
                elif len(nums)== 1 and target> nums[0]:
                    return(1)

        print(len(nums))        
        return(len(nums))   

solution = Solution()
result = solution.searchInsert([-3,-1,3,90], 0)
print(result)
        