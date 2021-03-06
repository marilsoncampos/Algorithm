'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a,b,c = 0,0,len(nums)-1
        mid = 1
        while b<=c:
            if nums[b]<mid:
                nums[a],nums[b] = nums[b],nums[a]
                a+=1
                b+=1
            elif nums[b]>mid:
                nums[b],nums[c] = nums[c],nums[b]
                c-=1
            else:
                b+=1
        #return nums
