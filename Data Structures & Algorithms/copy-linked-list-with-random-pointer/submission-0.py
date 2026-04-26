"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:

    
    nodes = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        
        # Construct new node
        newNode = Node(head.val, None, None)

        self.nodes[head] = newNode
        newNode.next = self.copyRandomList(head.next) 
        

        if head.random is None:
            newNode.random = None
        else:
            newNode.random = self.nodes[head.random]

        return newNode
