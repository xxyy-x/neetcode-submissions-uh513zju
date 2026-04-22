class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for i in range(n+1):
            tmp = bin(i)
            res.append(tmp.count("1"))
        
        return res
            