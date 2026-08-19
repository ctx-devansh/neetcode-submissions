class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Assume first full word is the suffix
        current_suffix = strs[0]
        # Loop through each word other than the first
        for word in strs[1:]:
            i = 0
            # break if i < the min len(current suffix) or len(word)
            # or break if the current char being checked are different
            while i < min(len(current_suffix),len(word)) and current_suffix[i] == word[i]:
                i += 1
            # Only keep the part that is same in both strings
            current_suffix = current_suffix[0:i]
        return current_suffix