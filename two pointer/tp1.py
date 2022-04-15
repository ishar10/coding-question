'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while(i<j):
            if (s[i].isalpha() and s[j].isalpha()):
                if s[i].lower()!=s[j].lower():
                    return False
                i+=1
                j-=1
            elif (s[i].isdigit() and s[j].isdigit()):
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            elif (s[i].isdigit() and s[j].isalpha()) or (s[i].isalpha() and s[j].isdigit()):
                return False
            elif s[i].isalpha()==False and s[i].isdigit()==False:
                i+=1
            elif s[j].isalpha()==False and s[j].isdigit()==False:
                j-=1
                    
        return True
                
        