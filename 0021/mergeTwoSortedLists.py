# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: ListNode, head2  : ListNode) -> ListNode:
        cur1 = head1
        cur2 = head2

        # list to store the values of the linked lists in sorted order
        newList = []

        # traversing through the linked list 1 and linked list 2
        while(cur1 is not None and cur2 is not None):
            # adding the smaller of the two values to newList
            if(cur1.val < cur2.val):
                newList.append(cur1.val)
                cur1 = cur1.next
            else:
                newList.append(cur2.val)
                cur2 = cur2.next

        # incase there are any elements left in linked list 1
        # we add them to mewList
        while(cur1 is not None):
            newList.append(cur1.val)
            cur1 = cur1.next

        # incase there are any elements left in linked list 1
        # we add them to mewList        
        while(cur2 is not None):
            newList.append(cur2.val)
            cur2 = cur2.next

        # we create a linked list from the newList
        head = self.createList(newList)
        return head

    def createList(self,a):

        # traverse through the list and create a linked list
        # return head of the newly created linked list
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

    
        


