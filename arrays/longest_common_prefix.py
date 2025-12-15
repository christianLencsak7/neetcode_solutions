class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        preFix = strs[0]
        result = ""
        howFarToGo = len(preFix)
        for j in range(howFarToGo):
            for i in strs:
                if j == len(i) or i[j] != preFix[j]:
                    return result
            result += strs[0][j]
        return result