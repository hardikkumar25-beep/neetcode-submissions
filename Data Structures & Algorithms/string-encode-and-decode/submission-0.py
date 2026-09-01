class Solution:
    def encode(self, strs: List[str]) -> str:
        final_string=""
        for strings in strs:
            final_string+=str(len(strings))+'#'+ strings
        return final_string
    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
        while i<len(s):
            start=i
            while s[i]!='#':
                i+=1
            length=int(s[start:i])
            i+=1
            word=s[i:i+length]
            result.append(word)
            i+=length
        return result
