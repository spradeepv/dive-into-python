#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    p = head
    q = head
    while position > 0:
        position -= 1
        p = p.next
    while p.next:
        q = q.next
        p.p.next
    return q.data

