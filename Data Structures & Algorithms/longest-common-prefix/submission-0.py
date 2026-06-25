class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first =strs[0]
        for i in range(len(first),0,-1):
            prefix = first[:i]
            found = True
            for word in strs:
                if not word.startswith(prefix):
                    found = False
                    break
            if found:
                return prefix
        return ""
        