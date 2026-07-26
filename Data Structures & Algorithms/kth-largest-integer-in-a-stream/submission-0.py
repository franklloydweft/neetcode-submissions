class KthLargest:
    """
    I barely covered streams AND heaps (aside from memory) 
    in my university education... so this is brand new learning 
    to me. Common UW Mad L.

    """

    def __init__(self, k: int, nums: List[int]):
        #MIN HEAP (complete binary tree w/ min value at root) of size k
        #for k largest value in stream at root of tree.
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        #popping values until we satisfy size. Larger values added at leaves
        #and shift tree by popping until k size, where root is kth largest
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #push the desired value
        heapq.heappush(self.minHeap,val)
        #pop off extra to satisfy k
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0] #root will be k distance from largest leaf