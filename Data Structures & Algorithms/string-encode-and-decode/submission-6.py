class Solution:

    
    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        out_str = ""
        for word in strs:
            out_str += str(len(word)) + self.delimiter + word
        return out_str
                

    def decode(self, s: str) -> List[str]:
        word_list = []
            
        i = 0
        j = 0
        while i < len(s):
            while s[j] is not self.delimiter:
                j += 1
            curr_str_len = int(s[i:j])
            curr_str = s[j+1:j+1+curr_str_len]
            word_list.append(curr_str)
            i = j + 1 + curr_str_len
            j = i

        return word_list

