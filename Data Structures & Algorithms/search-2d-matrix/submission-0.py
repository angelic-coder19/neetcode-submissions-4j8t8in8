class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:

            if row[0] <= target <= row[-1]:
                l, r = 0, len(row) - 1 
                while r >= l:
                    idx = int((r + l) / 2)

                    if row[idx] == target:
                        return True
                    
                    elif row[idx] > target:
                        r = idx - 1
                    
                    else:
                        l = idx + 1            


        return False