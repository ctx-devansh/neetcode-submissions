class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        categs = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for chr in word:
                counts[ord(chr) - ord('a')] += 1
            categs[tuple(counts)].append(word)
        return list(categs.values())