"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    aDict = {}
    if head:
        curr = head
        while curr:
            #print curr.data
            if aDict.has_key(curr.data):
                prev.next = curr.next
                #print prev.data, curr.next
                #if prev.next:
                #    curr.next = prev.next
                #else:
                #    curr.next = None
            else:
                aDict.update({curr.data: 1})
                prev = curr
            curr = curr.next
    return head
