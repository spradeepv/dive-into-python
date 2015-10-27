"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

#Iterative
def Reverse(n):
  last = None
  current = n

  while(current is not None):
    nxt = current.next
    current.next = last
    last = current
    current = nxt

  return last

#Recursive
def Reverse(n,last):
  if n is None:
    return last
  nxt = n.next
  n.next = last
  return Reverse(nxt, n)








