"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if not headA:
        return headB
    elif not headB:
        return headA
    else:
        if headA.data < headB.data:
            tempA = headA.next
            headA.next = MergeLists(tempA, headB)
            return headA
        else:
            tempB = headB.next
            headB.next = MergeLists(headA, tempB)
            return headB




