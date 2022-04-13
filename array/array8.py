'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        post=[]
        for i in range(len(nums)):
            if i==0:
                pre.append(1)
            else:
                pre.append(pre[i-1]*nums[i-1])
        k=0
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                post.append(1)
            else:
                post.append(post[k-1]*nums[i+1])
            k+=1
            
    
        l=[]
        k=len(pre)-1
        for i in range(len(pre)):
            l.append(pre[i]*post[k])
            k-=1
        return l