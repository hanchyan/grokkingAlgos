# passed leet... with very bad score... 
class Solution(object):
    def plusOne(self, digits):
        pythonInt = int("".join(map(str, digits)))
        pythonInt +=1
        pythonArray = list(map(int, str(pythonInt)))
        return(pythonArray)
solution = Solution()
result = solution.plusOne([1,2,3,4,5,6,7,9])
print(result)