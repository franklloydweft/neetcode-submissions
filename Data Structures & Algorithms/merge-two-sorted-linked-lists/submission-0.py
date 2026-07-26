# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a merge list w/ dummy pointer
        temp = ListNode()
        mergeList = temp

        #while both ptrs are nonempty
        while list1 and list2:
            #first list val is smaller, insert and move ptr
            if list1.val<list2.val:
                mergeList.next = list1
                list1 = list1.next
            #second list val is smaller, insert and move ptr
            else:
                mergeList.next = list2
                list2 = list2.next
            #advance merge ptr
            mergeList = mergeList.next

        #handle lists being different sizes by appending the rest
        if list1:
            mergeList.next = list1
        elif list2:
            mergeList.next = list2

        #return the dummy pointer to list
        return temp.next

        