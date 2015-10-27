"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def Reverse(head):
    if head:
        l = []
        new_head = Node()
        while head:
            l.append(head.data)
            head = head.next
        i = len(l) - 1
        data = l[i]
        head = Node(data=data)
        head.next = Node(data=l[i - 1])
        temp = head
        while i > 0:
            temp = temp.next
            i -= 1
            temp.data = l[i]
            if i == 0:
                temp.next = None
            else:
                temp.next = Node(l[i-1])
        return head
    else:
        return head