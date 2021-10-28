def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    p = head
    e = r = ListNode(None)

	# find out the length of the list
    n = 0
    while head:
        head = head.next
        n += 1

	# rearrange the nodes
    for i in range(n // k):    # for every group
        s = p                  # record the first node of a group that will soon become the last node of the reversed group
        for _ in range(k):     # for every node in a group
            t = p.next
            p.next = e.next    # put the current node right before the head of the reversed group
            e.next = p         # register p as the head of the reversed group
            p = t              # visit the next node in the original list
        e = s                  # update the end of the reversed group
    e.next = p                 # append the tail to the end
    return r.next
