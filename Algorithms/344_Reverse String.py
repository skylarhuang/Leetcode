class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = []
        for i in range(len(s)):
            new.append(s[len(s)-i-1])
        return ''.join(new)
    
        ##return s[::-1]