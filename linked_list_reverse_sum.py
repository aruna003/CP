# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l=None
        prev=None
        carry=0
        while l1 is not None or l2 is not None or carry!=0:
            
            if l is None:
                l=ListNode()
                front=l
                prev=l
            else:
                l=ListNode()
                prev.next=l

            if l1 is not None and l2 is not None:
                sum=l1.val+l2.val+carry
                l1=l1.next
                l2=l2.next

            elif l1 is None and l2 is None and carry!=0:
                sum=carry

            elif l2 is None:
                sum=l1.val+carry
                l1=l1.next

            elif l1 is None:
                sum=l2.val+carry
                l2=l2.next
    
            carry=0

            if sum<=9:
                l.val=sum
            else:
                l.val=sum%10
                carry=sum//10
            # print(l.val)

            prev=l

        return front
