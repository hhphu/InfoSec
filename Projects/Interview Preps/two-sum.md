# TWO SUM

**URL:** https://leetcode.com/problems/add-two-numbers/description/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        sum = 0 
        borrow = 0
        current = dummyHead

        while (l1 or l2 or borrow):
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            sum = digit1 + digit2 + borrow
            digit = sum % 10
            borrow = sum // 10

            newNode = ListNode(digit)
            current.next = newNode
            current = current.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result = dummyHead.next
        dummyHead.next = None

        return result
```
