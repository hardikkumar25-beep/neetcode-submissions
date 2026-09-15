class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        count1={}
        count2={}
        have=0
        if len(s)<len(t):
            return ""
        for char in t:
            count2[char]=count2.get(char,0)+1
        need=len(count2)
        min_len=float("inf")
        result=""
        for right in range(len(s)):
            count1[s[right]]=count1.get(s[right],0)+1
            if s[right] in count2 and count1[s[right]] == count2[s[right]]:
                have += 1
            while have==need:
                if right-left+1<min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]
                count1[s[left]]-=1
                if s[left] in count2 and count1[s[left]] < count2[s[left]]:
                    have -= 1
                left+=1
        return result
                


