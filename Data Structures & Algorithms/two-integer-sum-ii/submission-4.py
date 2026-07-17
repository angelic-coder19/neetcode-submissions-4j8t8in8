"""
U:
    Input: array of integers (sorted in non-decreasing order), integer target
    Output: array of 1 indexed integers representing the numbers that add up to target

    Edge cases:
    - There are only two numbers in the array

    Constraints: 
    - There will only be one solution
    - Use of constant space (no extra memory)

M:
    Two Pointers
P:
    - Declare left pointer to point to beginning of the list
    - Declare right pointer to pont to the end of the list
    - Repeat until left is greater or equal to right: 
        - Calculate the sum the number at left and at right
        - if the sum is equal to target
            - return [left + 1, right + 1]
        
        - If the sum is larger than the target:
            - lower the right pointer
        - increment the left pointer
    - Since there is always a solution, do nothing here
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r: 
            s = numbers[l] + numbers[r]

            if s == target: 
                return [l + 1, r + 1]
            
            elif s > target:
                r -= 1
            else: 
                l += 1
        





