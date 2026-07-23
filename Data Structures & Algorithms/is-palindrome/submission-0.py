class Solution:
    def isPalindrome(self, s: str) -> bool:

        new = ""

        for char in s:
            if char.isalnum():
                new += char

        new = new.lower()

        r = len(new) - 1

        for l in range(len(new)):
            if new[l] != new[r]:
                return False
            r -= 1
        return True
  

            

        