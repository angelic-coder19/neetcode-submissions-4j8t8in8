"""
Understanding:
    Input: Array of integers 
    Output: Integer representing the longest consecutive sequence

    - The integers can be in any order
    - The algorithm must be in linear time O(n) where n is the length of the array
    - Duplicate numbers must be only counted once
    - There could be no elements in the array and must return 0
Match:
    - Set
Planning:
    [2, 20, 4, 10, 3, 4, 5] set = {2,4,10,20,3,5}
    {2: 3, 20: 21, 4: 5, 10: 11, 3: 4, 5: 6}
    - First pass to make a set of distinct numbers
    - Second pass through the array 
        -  if num - 1 does not exist in the set then a new sequence has began
            - Set counter for how long sequence is initially 1
            - While num + 1 exists in set
                - Increment the counter
                - Increment num by 1
            - Replace the longest sequence if necessary
    - Return counter        
            
    
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in unique:
                counter = 1
                while num + 1 in unique:
                    counter += 1
                    num += 1
                longest = max(longest, counter)
                
        
        return longest