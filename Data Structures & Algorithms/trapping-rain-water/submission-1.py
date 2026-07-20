"""
 0 1 2 3 4 5 6 7 8 9
[0,2,0,3,1,0,1,3,2,1]
   length = 10
   i = 0, 
max_s = 3, suff = [1,2,3,3,3,3,3,3] 

U: 
    Input: array of integer heights
    Output: the maximum water that can be stored between the heights

M: 
    - Two pointers
    - Stack (Monotomic stack)
P: 
    - Declare two arrays for the prefix max and suffix maximum
    - Iterate from 0 through heights to find the highest number at each index
    - Do the same from len(heights) - 1 to find the highest val at each index

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = [], [None for h in height]
        max_h = height[0]
        for h in height:
            max_h = max(max_h, h)
            prefix.append(max_h)
        
        max_s = height[-1]
        i = len(height) - 1
        while i >= 0:
            max_s = max(max_s, height[i])
            suffix[i] = max_s
            i -= 1     

        water = 0
        for i in range(len(height) - 1): 
            water += min(prefix[i], suffix[i]) - height[i]
            
        return water
        