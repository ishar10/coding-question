'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsset=set()
        nums=sorted(nums)
        for i in range(len(nums)-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            target=-(nums[i])
            one=i+1
            two=len(nums)-1
            while(one<two):
                sum=nums[one]+nums[two]
                if sum==target:
                    numsset.add((nums[i],nums[one],nums[two]))
                    one+=1
                elif sum>target:
                    two-=1
                else:
                    one+=1
        return list(numsset)