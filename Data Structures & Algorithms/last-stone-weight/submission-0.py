class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)
        print(stones)
        while len(stones)>1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1<stone2:
                newStone = stone2-stone1
                heapq.heappush_max(stones,newStone)
            elif stone2<stone1:
                newStone = stone1-stone2
                heapq.heappush_max(stones,newStone)
        if len(stones)==0:
            return 0
        return stones[len(stones)-1]

        