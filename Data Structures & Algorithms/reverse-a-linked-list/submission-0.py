# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #reverse all the pointers and swap first and last
        last, place = None, head

        while place:
            #store current place ptr
            temp = place.next
            #swap current place ptr
            place.next = last
            #swap last place's ptr
            last = place
            #reset current place
            place = temp
        #return swapped ptr (last is now first)    
        return last
        