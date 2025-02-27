# not done...
class Solution(object):
    def generate(self, numRows):
        x = 1
        array = []
        nestedArray=[]

        while x <= numRows:
            nestedArray.append(x)
            array.append(nestedArray)
            # array.append(x+x)
            x += 1
            print(array)
        print(array)
        return array


solution = Solution()
result = solution.generate(6)
print(result)

