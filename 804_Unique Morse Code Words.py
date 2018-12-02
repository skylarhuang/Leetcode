class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = set()
        morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        if len(words) >0:
            for word in words:
                tmp = ''
                for w in word:
                    tmp = tmp+morsecode[ord(w)-ord('a')]
                result.add(tmp)   
        else:
            return 0
        return len(result)