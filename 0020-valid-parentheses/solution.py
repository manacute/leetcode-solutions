class Solution:
    def isValid(self, s: str) -> bool:
        remaining_chars = []
        matching_bracket = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for c in s:
            if c in "([{":
                remaining_chars.append(c)
            else:
                if len(remaining_chars) == 0:
                    return False
                if remaining_chars[-1] != matching_bracket[c]:
                    return False
                remaining_chars.pop()
                    
        return len(remaining_chars) == 0