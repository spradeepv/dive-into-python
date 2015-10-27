"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if head:
        temp = head
        while temp:
            if temp.data >= data:
                node = Node(data=data, next_node=temp, prev_node=temp.prev)
                temp.prev = node
                node.next = temp
                if node.prev:
                    node.prev.next = node
                    return head
                else:
                    return node
            if not temp.next:
                node = Node(data=data, next_node=None, prev_node=temp)
                temp.next = node
                break
            temp = temp.next
        return head
    else:
        node = Node(data=data)
        return node
