class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashsetT = set()
        hashsetS = set()

        sortedT = ''.join(sorted(t))
        sortedS = ''.join(sorted(s))

        hashsetT.add(sortedT)
        hashsetS.add(sortedS)

        if hashsetT == hashsetS:
            return True 

        if hashsetT != hashsetS:
            return False


        


        