class Solution(object):
    def generate(self, numRows):
        x = 1
        array = []

        while x <= numRows:
            innerArray =[]
            nestedArray = [x,x/2,x/3]
            innerArray.append(nestedArray)
            array.append(innerArray)
            print(innerArray)
            x += 1

    
# test
# test from my computer


solution = Solution()
result = solution.generate(6)
print(result)