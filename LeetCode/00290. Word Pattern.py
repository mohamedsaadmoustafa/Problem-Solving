class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return [*map(pattern.index, pattern)] == [*map(s.index, s)]
