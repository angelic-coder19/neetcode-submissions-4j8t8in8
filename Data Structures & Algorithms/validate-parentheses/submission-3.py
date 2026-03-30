class Solution:
    def isValid(self, s: str) -> bool:
        # Close characters and their corresponding open characters
        pairs = {")":"(", "}":"{", "]":"["}
        
        # Stack to keep track of opening characters
        open = []
        
        for c in s:
            if self.is_opening(c):
                open.append(c)
                
            elif open and pairs[c] == open[-1]:
                open.pop()
            else:
                return False
        
        return True if not open else False

    def is_opening(self, c: str) -> bool:
        match (c):
            case "(" | "{" | "[":
                return True
            case _:
                return False