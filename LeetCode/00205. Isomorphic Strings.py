class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map, reverse_map = {}, {}

        for ss, tt in zip(s, t):
            if (ss in map and map[ss] != tt) or ((tt in reverse_map and reverse_map[tt] != ss)): 
                return False
            map[ss], reverse_map[tt] = tt, ss
        return True
