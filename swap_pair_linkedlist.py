# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next==None:
            return head
        i=head
        head=i.next
        # first swap
        i.next=head.next
        head.next=i
        current= i

        while current.next and current.next.next:
            i = current.next
            j = current.next.next
            k = current.next.next.next

            # Swap the nodes
            current.next = j
            j.next = i
            i.next = k

            # Move current two steps forward
            current = i


        return head
