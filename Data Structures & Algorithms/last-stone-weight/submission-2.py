class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #make a max heap of stones
        heapq.heapify_max(stones)
        #loop while there are more than 1 stone remaining
        while len(stones)>1:
            #pop off the two heaviest
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            #compare and SMASH
            if stone1<stone2:
                newStone = stone2-stone1
                heapq.heappush_max(stones,newStone)
            elif stone2<stone1:
                newStone = stone1-stone2
                heapq.heappush_max(stones,newStone)
            #do nothing if they equal, they are just popped
        #if none are left return 0
        if len(stones)==0:
            return 0
        #return the farthest leaf node, this is the lightest
        return stones[len(stones)-1]

        