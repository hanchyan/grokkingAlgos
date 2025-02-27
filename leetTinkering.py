class Solution(object):
    def merge(nums1, nums2):

       for x in nums2:
           nums1.insert(0,x)
       nums1.sort()     
       print(nums1) 

    merge([1,4,5,6,4,2,], [3,5,6,3])

    