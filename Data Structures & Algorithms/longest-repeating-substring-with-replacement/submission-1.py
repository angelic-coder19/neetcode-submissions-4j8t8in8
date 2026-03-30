class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = { c: 0 for c in s }
        
        l, max_sub = 0, 0
        for r in range(len(s)):
            counts[s[r]] += 1
            win_len = r - l + 1
            most_freq = counts[self.most_freq(counts)] 

            if win_len - most_freq <= k:
                max_sub = max(win_len, max_sub)
            
            else:
                counts[s[l]] -= 1
                l += 1 

        
        return max_sub
    
    
    def most_freq(self, counts):
        return sorted(counts.items(), key=lambda l: l[1], reverse=True)[0][0]
            