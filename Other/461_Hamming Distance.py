## XOR 的使用方法
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return (bin(x^y).count("1"))