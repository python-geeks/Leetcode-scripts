# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: ListNode, head2  : ListNode) -> ListNode:
        cur1 = head1
        cur2 = head2

        newList = []

        while(cur1 is not None and cur2 is not None):
            if(cur1.val < cur2.val):
                newList.append(cur1.val)
                cur1 = cur1.next
            else:
                newList.append(cur2.val)
                cur2 = cur2.next

        while(cur1 is not None):
            newList.append(cur1.val)
            cur1 = cur1.next

        while(cur2 is not None):
            newList.append(cur2.val)
            cur2 = cur2.next

        head = self.createList(newList)
        return head

    def createList(self,a):
        head = None
        tail = None

        for currData in a:
            newNode = ListNode(currData)

            if(head is None):
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode

        return head

    
        


