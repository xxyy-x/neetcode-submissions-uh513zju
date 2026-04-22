class Solution:
    def hammingWeight(self, n: int) -> int:
        
        s = bin(n)

        count = 0

        for i in s:
            if i == "1":
                count += 1
        
        return count