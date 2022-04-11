

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        else:
            return False

'''Runtime: 48 ms, faster than 89.54% of Python3 online submissions for Valid Anagram.
Memory Usage: 15.1 MB, less than 12.72% of Python3 online submissions for Valid Anagram.'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in t:
            if i in dict2:
                dict2[i]+=1
            else:
                dict2[i]=1
        if dict1==dict2:
            return True
        else:
            return False

'''Runtime: 65 ms, faster than 58.73% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 69.94% of Python3 online submissions for Valid Anagram.'''