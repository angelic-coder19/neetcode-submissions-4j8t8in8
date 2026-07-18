"""
U:
    Input: array of integers
    Output: array of arrays(triplets) where all the triplets add up to 0

    Edge cases:
    - There can be no triplets that add up to 0
    - There must be no duplicate triplets
    - There will be a minimum of 3 numbers
M: 
    - Two Pointers
    - Sorting
P: 
    - Sort the input array to have lower numbers at the front
    - Declare empty array for triplets found
    - Start iteration at first () element up to the 2nd from last
        - If the index is not 0 and the element before it is the same as this one, 
            skip this iteration because all the triplets must have been found
        - set left pointer to the current index + 1
        - set right pointer to the length of the array + 1
        - Iterate until left pointer is equal or greater than right
            - Calculate sum by adding the numbers at each index
            - if the sum is equal to 0:
                - Create triplet array and add to the triplets list
                - Add to triplets array
                - 
                
            - if the sum is too high, lower right pointer
            - if the sum is too low, increment left pointer
    - Return list of triplets
R:  
    [-1,0,1,2,-1,-4] --> [-4,-1,-1,0,1,2]
                              c    l r
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for c in range(len(nums) - 2):
            if c != 0 and nums[c] == nums[c - 1]:
                continue

            l, r = c + 1, len(nums) - 1
            while l < r:
                target = nums[c] + nums[l] + nums[r]

                if target == 0:
                    triplet = [nums[c], nums[l], nums[r]]
                    triplets.append(triplet)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
                elif target > 0: 
                    r -= 1
                else:
                    l += 1
            
        return triplets

