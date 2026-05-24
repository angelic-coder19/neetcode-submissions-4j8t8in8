"""
U: 
    Input: string of words 
    Output: True - if it is valid palindrome
            False - if the string is not a vilid palindrome
    - Must be case insensitive
    - Must not consider non-alphanumeric characters
    - can be a single word
M: 
    Two pointers

P:
    - Create an array of characters, convert to lower case, remove the spaces
    - Set a left pointer to the start of array and right pointer to the end
    - While the left and the right pointer are not equal
        - Check if the character at the r is not equal to char at l
            return False
        - Move r index back, left index forward
    - Return True 
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip().replace(" ", "")
        string = []
        for c in s:
            if c.isalnum():
                string.append(c.lower())

        l, r = 0, len(string) - 1
        while l <= r: 
            if string[l] != string [r]:
                return False
            
            l += 1
            r -= 1
            
        return True
        