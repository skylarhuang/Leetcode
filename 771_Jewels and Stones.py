class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """        
        num = 0
        if len(S) == 0:
            return num
        else:
            for s in S:
                if s in J:
                    num += 1
            return num