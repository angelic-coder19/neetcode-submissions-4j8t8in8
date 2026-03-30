class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(s.split()).lower()
        l, r = 0, len(new_str) - 1
        print(new_str)
        while l <= r:
            if not(new_str[l].isalpha()) and not(new_str[l].isdigit()):
                l += 1
                continue
            if not(new_str[r].isalpha()) and not(new_str[r].isdigit()):
                r -= 1
                continue
            
            
            if new_str[l] != new_str[r]:
                return False
            l += 1
            r -= 1
        return True