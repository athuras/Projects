#!/usr/bin/env python
'''
For when you need a tree for something
'''
from collections import defaultdict, deque


class Tree():
    '''Tree Object, contains value and child references'''
    def __init__(self, val=None, children=None):
        if children is None:
            children = defaultdict()
        self.value = val
        self.children = children

    def breadthFirst(self):
        '''Sequentially yield nodes in an unguided breadthFirst fashion'''
        q = deque([self])
        while len(q) > 0:
            node = q.popleft()
            yield node
            for i in node.children:
                q.append(node.children[i])
        return

    def orderedTraversal(self, mode):
        '''Defaults to preorder'''
        q = deque([self])
        while len(q) > 0:
            node = q.popleft()
            yield node
            aux = deque()
            for i in node.children:
                aux.append(node.children[i])
            if mode == "preorder":
                q.extend(aux)
            elif mode == "postorder":
                aux.reverse()
                q.extend(aux)
            else:
                q.extend(aux)
        return

    def depthFirst(self):
        '''Sequentially yield nodes in an unguided depth-first fashion'''
        q = deque([self])
        while len(q) > 0:
            node = q.pop()
            yield node
            for i in node.children:
                q.append(node.children[i])
        return

    def __contains__(self, item):
        '''Uses Breadth-first search to find Trees'''
        if item is self:
            return True
        else:
            for node in self.breadthFirst():
                if node is item:
                    return True
            return False

    def __str__(self):
        return "Tree: {value: %s, children: %s}" % (self.value, self.children.keys())

    def __repr__(self):
        '''
        Currently does not conform to the convention:
        >>Z = Tree()
        >>Tree(repr(Z)) == Z
        >>False  # True if following pickle protocol (I believe)
        '''
        return str(self)

    def clear(self):
        self.value = None
        self.children.clear()
