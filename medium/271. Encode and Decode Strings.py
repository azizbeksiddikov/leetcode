# Link: https://leetcode.com/problems/encode-and-decode-strings/description/

class Solution:

    def encode(self, strs: List[str]) -> str:
        output_text = ""
        
        for word in strs:
            output_text += str(len(word)) + "#" + word
        
        return output_text

    def decode(self, s: str) -> List[str]:
        decoded = []
        
        while True:
            if not s: 
                return decoded
            
            ele_index = s.index("#")
            word_len = int(s[:ele_index])
            
            word = s[ele_index+1: ele_index+1+(word_len)]
            s = s[ele_index+word_len+1:]
            
            decoded.append(word)
