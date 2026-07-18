"""
U:
    input: list of integers representing heights of 
    output: maximum area of rectangle formed by bars of different heights (interger)

    - There will be atleast two bars in the input array
    - The height of a rectangle can be 0
M:
    - Two pointers
    - Math
P:
    - Set a left pointer to beginning of the list
    - Set a right pointer to the end of the list
    - Set a variable for the area and set it to - infinity
    - While the left pointer is less than the right pointer
        - Calculate the area: 
            area = (distance between left and right) * minimum(L_height, R_height)
        - Replace the area if a new hight is found
        - If the height at R is smaller: decrement right pointer
        - Else the height at L is smaller: increment left pointer
    - Return the max height
I: 

R:   0 1 2 3 4 5   6   7  8 9 10 11 12 13
    [1,7,2,5,12,3,500,500,7,8, 4, 7, 3,6]
                  l    r
     area = 13,72,72,72,72       
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = - float("inf")
        while l < r: 
            max_area = max(max_area,((r - l) * (min(heights[l], heights[r]))))
            
            if heights[r] < heights[l]: 
                r -= 1
            else: 
                l += 1
        return max_area
