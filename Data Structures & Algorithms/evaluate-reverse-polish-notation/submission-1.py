class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = []
        for t in tokens:
                match t:
                    case "+":
                        ans = int(ops.pop()) + int(ops.pop())
                        ops.append(ans)
                    case "-":
                        ans = int(ops[-2]) - int(ops[-1])
                        ops.pop()
                        ops.pop()
                        ops.append(ans)
                    case "*":
                        ans = int(ops.pop()) * int(ops.pop())
                        ops.append(ans)
                    case "/":
                        ans = int(ops[-2]) / int(ops[-1])
                        ops.pop()
                        ops.pop()
                        ops.append(int(ans))
                    case _:
                        ops.append(t)
        return int(ops[-1])   