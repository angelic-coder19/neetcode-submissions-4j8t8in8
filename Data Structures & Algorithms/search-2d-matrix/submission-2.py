"""
U:
 Input: matrix of integers, integer target
 Output: True if integer exists within matrix, False if it does not exist

 Entire matrix is in increasing order
 Every first element of one row is larger than the last element of the previous row
  
M:
 Binary Search

P:
    - Find the row to perform binary search on 
    - For each row in the matrix
        - Check if the target is in the range (greater than first less than last)
            - If it is in range perform bianry search on that row
    - return False cause then we never returned True earlier

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if matrix[row][0] <= target <= matrix[row][len(matrix[row]) - 1]:
                l, r = 0, len(matrix[row]) - 1
                while l <= r:
                    mid = (l + r) // 2 
                    if matrix[row][mid] == target:
                        return True
                    
                    elif matrix[row][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1 
                return False
        return False
