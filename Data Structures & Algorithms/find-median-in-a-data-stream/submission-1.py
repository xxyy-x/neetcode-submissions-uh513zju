import heapq

class MedianFinder:

    def __init__(self):
        
        self.right = []
        self.left = []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.right, num)

        val = heapq.heappop(self.right)

        heapq.heappush(self.left, -val)

        if len(self.right) < len(self.left):
            tmp = - (heapq.heappop(self.left))
            heapq.heappush(self.right, tmp)
        

    def findMedian(self) -> float:
        
        if len(self.right) > len(self.left):
            return self.right[0]
        
        return (self.right[0] - (self.left[0])) / 2

        