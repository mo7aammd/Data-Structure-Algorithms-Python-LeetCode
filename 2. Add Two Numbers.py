# https://leetcode.com/problems/add-two-numbers/
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        l3 = head
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 != None else 0
            l2Val = l2.val if l2 != None else 0
            value = l1Val + l2Val + carry
            carry = value // 10
            l3.next = ListNode(value % 10)
            l3 = l3.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next