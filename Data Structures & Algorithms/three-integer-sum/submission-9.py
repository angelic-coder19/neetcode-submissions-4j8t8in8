"""
Understanding:
    input: A list of integers 
    output: a list of lists (triplets) that add up to 0

    - All triplets must be unique
    - All triplets must add up to 0
    - There can be no triplets that satify the conditions
    - The least number of values in list is 3

Match: 
    - Sorting, Two-pointers
    [-1,0,1,2,-1,-4] --> [-4,-1,-1,0,1,2]
Planning:
    - Sort the elements from smallest to largest
    - Create an array for the result
    - Iterate over each number in the sorted array
        - [[-1, -1, 2], [-1, 0, 1]]
                    c l r
        [-4,-1,-1,0,1,2]
        - set a left and right ponter to one after current number 
        - While the left is less than the right
            - compute sum
            - If the sum is 0: add the numbers to the result 
            - If the sum is greater than 0: lower right pointer
            - Increment left pointer
        
        
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[r] + nums[l]
                if sum == 0: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return res 