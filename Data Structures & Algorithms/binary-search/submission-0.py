class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search with pointers (no recursion)

        #init pointers at both ends
        lp,rp = 0, len(nums)-1

        #while we have not crossed the middle
        while lp<=rp:
            #calculate pivot location (may have overflow with large ints)
            #avoid overflow with l + ((r-l)//2) with half the distance + left
            pivot = (lp+rp)//2
            #target is smaller than the value at pivot, move left
            if nums[pivot] > target:
                rp = pivot - 1
            #target is larger than value at pivot, move right
            elif nums[pivot] < target:
                lp = pivot + 1
            #otherwise, we are at the target. return index.
            else:
                return pivot
        #case where target isn't found
        return -1