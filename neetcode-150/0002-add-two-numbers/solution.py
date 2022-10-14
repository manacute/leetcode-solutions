# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = ListNode(0)
        current_total = total
        current_l1 = l1
        current_l2 = l2
        carry = 0
        
        while current_l1 or current_l2 or carry:
            val = 0 
            if current_l1:
                val += current_l1.val
                current_l1 = current_l1.next
            if current_l2:
                val += current_l2.val
                current_l2 = current_l2.next
            
            val += carry
            carry = 0
            if val > 9:
                carry = 1
                val %= 10
            
            current_total.next = ListNode(val)
            current_total = current_total.next
        
        return total.next