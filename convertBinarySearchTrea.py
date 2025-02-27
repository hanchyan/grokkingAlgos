import json
class Solution(object):
    def sortedArrayToBST(self, nums):
        x = len(nums)
        med = x/2
        little =[]
        big = []
        bst= []
        for i in range(len(nums)):
            if i< med:
                little.append(nums[i])
        for i in range(len(nums)):
            if i > med:
                big.append(nums[i])
        littleLen = len(little)
        bigLen = len(big)
        if bigLen > littleLen:
            refNum = bigLen
        else:
            refNum = littleLen
        bst.append(nums[med])
        for i in range(refNum):
            if little:
                bst.append(little.pop())
            if not little:
                bst.append(None)
            if big:
                bst.append(big.pop())
        json_output = json.dumps(bst)  # Converts None to "null" in JSON

        print(json_output)
solution = Solution()
result = solution.sortedArrayToBST([-10,-3,0,5,9])
print(result)



