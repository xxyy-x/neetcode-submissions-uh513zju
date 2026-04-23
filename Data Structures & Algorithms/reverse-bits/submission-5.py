class Solution:
    def reverseBits(self, n: int) -> int:
        d = 31
        num = 0
        while d > -1:
            if n & 1:
                num += 2**d
            n = n >> 1
            d -= 1
        
        return num
                