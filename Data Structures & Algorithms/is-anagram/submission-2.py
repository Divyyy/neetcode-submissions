class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        coS = {}
        coT = {}
        for i in range(len(s)):
            coS[s[i]] = 1+coS.get(s[i], 0)
            coT[t[i]] = 1+coT.get(t[i], 0)
        return coS == coT 
        