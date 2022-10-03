import collections

def countLetters(s: str) -> dict:
    c = collections.Counter()
    for char in s:
        c[char] += 1
    return c

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = countLetters(s)
        t_char = countLetters(t)
        
        return (s_char == t_char)