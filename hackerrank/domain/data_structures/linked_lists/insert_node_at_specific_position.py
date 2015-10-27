"""
 Insert Node at the end of a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    node = Node(data=data)
    if position == 0:
        if head:
            node.next = head
        return node
    temp = head
    while position > 1:
        position -= 1
        if not temp.next:
            temp.next = Node()
        temp = temp.next
    q = temp.next
    temp.next = node
    node.next = q
    return head


