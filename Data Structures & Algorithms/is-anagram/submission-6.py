class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash_map = {}
        t_hash_map = {}

        for s1 in s:
            if s1 not in s_hash_map:
                s_hash_map[s1] = 1
            else:
                s_hash_map[s1] += 1

        for t1 in t:
            if t1 not in t_hash_map:
                t_hash_map[t1] = 1
            else:
                t_hash_map[t1] += 1

        if s_hash_map == t_hash_map:
            return True
            
        return False
