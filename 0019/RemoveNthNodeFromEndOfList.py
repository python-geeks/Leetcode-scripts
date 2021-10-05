class Solution(object):

    def removeNthFromEnd(self, head, n):

        slow = head  # at the end points to the previous node of the target node i.e the node we want to delete
        fast = head  # at the end points to the last node
        for i in range(n):  # take fast pointer n steps ahead
            fast = fast.next

        if not fast:
            return slow.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head