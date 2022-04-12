'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in range(len(strs)):
            k=sorted(strs[i])
            k1=''.join(k)
            if k1 in dict:
                dict[k1].append(i)
            else:
                dict[k1]=[i]
        l1=[]
        for k,v in dict.items():
            l=[]
            for i in v:
                l.append(strs[i])
            l1.append(l)
        return l1