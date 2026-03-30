class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        seen = set()
        l, r, longest = 0, 0, 0
        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            seen.add(s[r])
            longest = max(longest, r - l + 1 )
            r += 1
            
        
        return longest 