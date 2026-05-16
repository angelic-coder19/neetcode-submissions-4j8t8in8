class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                temp_i, idx_i = stack.pop()
                res[idx_i] = idx - idx_i

            stack.append((temp, idx))

        return res