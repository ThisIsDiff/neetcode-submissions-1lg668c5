"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import deque
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        current = Node(0) #current index of the new list
        newhead = current # head of the new list
        prev = None 
        index = head # current index of the original list
        nodeDict = {} # keeps track of which node in copy list corrsponds to original list 
        q = deque() 
        while (index):
            #keeps track of random
            q.append(index.random)
            
            nodeDict[index] = current

            #initialize new nodes and copy over elements from original
            current.val = index.val
            current.next = Node(0)
            current.random = None

            #moving along the list
            prev = current
            current = current.next
            index = index.next
        # #ending the linkedlist 
        prev.next = None

        #add back random
        current = newhead
        while (q):
            node = q.popleft()
            if (node):
                current.random = nodeDict.get(node)
            current = current.next
        return newhead