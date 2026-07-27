class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        t_counts = {}
        for char in s:
            if char not in s_counts.keys():
                s_counts[char] = 1
            else:
                s_counts[char] += 1
        
        for char in t:
            if char not in s_counts.keys():
                return False
            if char not in t_counts.keys():
                t_counts[char] = 1
            else:
                t_counts[char] += 1
        
        for key in s_counts.keys():
            if key not in t_counts.keys():
                return False
            if s_counts[key] != t_counts[key]:
                return False

        return True

        