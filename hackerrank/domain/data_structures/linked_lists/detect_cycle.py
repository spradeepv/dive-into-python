"""
 Check if linked list has cycle
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return 0 if no cycle else return 1
"""

def HasCycle(head):
    aDict = {}
    if head:
        while head:
            nxt = head.next
            if nxt:
                if aDict.has_key(nxt.data):
                    return 1
                else:
                    aDict.update({nxt.data: 1})
            head = head.next
    return 0