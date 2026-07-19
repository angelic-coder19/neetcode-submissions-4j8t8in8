"""
U:
    input: Two arrays, both in ascending order
    output: the median of the two arrays as a float

    - There can be no elements in both arrays or just one of them
    - There can be two numbers in the middle of the array
    - Must run in O(log(n + m)) where n and m are the number of elements in arrays
M: 
    - Two pointers, math,
P:
    - Find the lenghts of both arrays: n, m
    - Find the position of the median: (len(n) + len(m)) / 2
    - 
    - set and index counter to keep track of what point we are through the whole 
        - If number at l is smaller than at r: 
            
            - increment l
        -  
R:
    pos = 2 
    [1,2]    [3]
       l      r 
    1, 2


    pos = 2
    [1, 3]   [2, 4]
        l     r
    1, 2, 3
    (2 + 3) / 5 = 2.5
E:
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Name the arrays and ensure that A is smaller
        A, B = nums1, nums2
        
        # Find the total length and half 
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A): 
            A, B = B, A

        # Loop untill a valid split is found 
        l, r = 0, len(A) - 1
        while True:
            # Find the middle 
            m = (l + r) // 2
            j = half - m - 2

            Aleft = A[m] if m >= 0 else -float("inf")
            Aright = A[m + 1] if (m + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else -float("inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
 
            # Check for a valid split
            if Aleft <= Bright and Bleft <= Aright:
                # Odd case
                if total % 2:
                    return min(Aright, Bright)
                # Even case
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # Continue binary search if left 
            if Aleft > Bright:
                r = m - 1
            else:
                l = m + 1



