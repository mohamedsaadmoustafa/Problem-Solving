class Solution:
    def lcp(self, str1, str2):
        index1, index2 = 0, 0
        while index1 < len(str1) and index2 < len(str2):
            if str1[index2] != str2[index2]:
                break;
            index1, index2 = index1 + 1, index2 + 1
        return str1[:index1]

    def longestCommonPrefix(self, strs):
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        str0 = strs[0]
        for word in strs:
            str0 = self.lcp(str0, word)
        return str0

strs = ["flower","flow","flight"]
Solution().longestCommonPrefix(strs)
