class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        n = len(s) // 2
        count = 1
        if len(s) != len(t): return False
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        for ch in t:
            if seen.get(ch, 0) == 0:
                return False
            seen[ch] -= 1
        return True
