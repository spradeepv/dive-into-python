#Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def CompareLists(headA, headB):
    if headA and headB:
        while headA and headB:
            dataA = headA.data
            dataB = headB.data
            #print dataA, dataB, headA.next, headB.next
            if dataA != dataB or (not headA.next and headB.next) or (headA.next and not headB.next):
                return 0
            else:
                headA = headA.next
                headB = headB.next
        return 1
    elif headA or headB:
        return 0
