'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        dict1={}
        for i in dict:
            if dict[i] in dict1:
                dict1[dict[i]].append(i)
            else:
                dict1[dict[i]]=[i]
        l=[]
        # print(dict1)
        for key,v in sorted(dict1.items(),reverse=True):
            for i in range(len(v)):
                if k>0:
                    l.append(v[i])
                    k-=1
                    if k==0:
                        return l
                else:
                    return l