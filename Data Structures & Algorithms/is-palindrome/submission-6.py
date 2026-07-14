"""
U:
    input: string of characters (spaces, numbers, letters, punctuation)
    output: True if the sting is a palindrome, False if not palindrome

    - Punctuation marks must be skipped
    - Numeric characters must be skipped
    - must be case insensitive
    - below one thousand characters per string
M:
    - Two pointers
    - String manipulation
P:
    - Strip for whitespace 
    - Convert string to lowercase
    - Convert entire string into array
    - set left point to beggining of array and the right pointer to end
    - Iterate until left pointer is equal or greater than right
        - if char on left is punct or numeric, increment counter
        - compare left char and right char: if not same return False
        - increment left pointer
        - decrement right pointer
    - Return True because we never exited

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower().replace(" ", "")
        string = [] 
        for c in s:
            if c.isalnum():
                string.append(c)
    

        l, r = 0, len(string) - 1
        while l < r: 
            if string[l] != string[r]:
                return False 
            
            l += 1
            r -= 1
        
        return True





