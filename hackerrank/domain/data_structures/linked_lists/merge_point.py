"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

def FindMergeNode(headA, headB):
    data = None
    while headA:
        temp = headB
        found = False
        while temp:
            dataA = headA.data
            dataB = temp.data
            #print dataA, dataB
            if dataA == dataB:
                data = dataA
                found = True
                break
            else:
                temp = temp.next
        if found:
            break
        headA = headA.next
        headB = headB.next
    return data

