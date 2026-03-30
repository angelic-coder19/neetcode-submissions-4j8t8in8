class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for S in s: 
            if S not in chars:
                chars[S] = 1
                continue
            chars[S] += 1
        
        for T in t:
            if T not in chars: 
                return False
            chars[T] -= 1
        for key in chars:
            if chars[key] != 0:
                return False
        
        return True