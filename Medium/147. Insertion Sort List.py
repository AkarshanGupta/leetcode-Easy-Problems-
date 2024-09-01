class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        current = head

        while current and current.next:
            if current.val <= current.next.val:
                current = current.next
            else:
                # Extract the node to be inserted
                to_insert = current.next
                current.next = to_insert.next

                # Find the insertion point
                prev = dummy
                while prev.next and prev.next.val <= to_insert.val:
                    prev = prev.next

                # Insert the node
                to_insert.next = prev.next
                prev.next = to_insert

        return dummy.next
