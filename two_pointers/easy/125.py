"""
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i <= j:
            
            if not str.isalnum(s[i]):
                i += 1
                continue
            if not str.isalnum(s[j]):
                j -= 1
                continue
                        
            if str.lower(s[i]) != str.lower(s[j]):
                return False
            
            i += 1
            j -= 1
            
        return True

if __name__ == "__main__":

    tests = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " "
    ]

    for test in tests:
        print(Solution().isPalindrome(test))