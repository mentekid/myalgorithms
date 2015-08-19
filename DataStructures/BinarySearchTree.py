"""Implementation of a Binary Search Tree data structure
Author: Yannis Mentekidis
Date: August 14, 2015
"""
from bisect import bisect_left

def binary_search(array, key, low = 0, high = None):
    """Binary search in an array using bisect_left"""
    if high is None:
        high = len(array)
    pos = bisect_left(array, key, low, high)
    if pos is not high and array[pos] is key:
        return pos
    return -1

class BST:

    def __init__(self, item = None):
        """Initializes a Binary Search Tree node"""
        self.left = None
        self.right = None
        self.content = item
        return

    def __repr__(self, depth = 0, retstr = ""):
        """Prints a binary tree in a pretty, tabbed format"""
        retstr = "\t"*depth + str(self.content) + "\n"

        if self.left is not None:
            retstr += self.left.__repr__(depth+1, retstr)
        if self.right is not None:
            retstr += self.right.__repr__(depth+1, retstr)
        return retstr

    def insert(self, item):
        """Inserts an item into the BST"""
        if self.content == None:
            self.content = item
        elif self.content < item: #big items go right
            if self.right is None: #was leaf
                self.right = BST(item)
                return
            self.right.insert(item)
            return
        else: #small items go left
            if self.left is None: #was leaf
                self.left = BST(item)
                return
            self.left.insert(item)
            return
        return

    def add(self, array):
        """Inserts item of an array into the BST"""
        for x in array:
            self.insert(x)
        return

    def search(self, key):
        """Search for a key. Return the subtree with root the key.
        Return None if key not found"""
        if self.content is None:
            return None
        elif key == self.content:
            return self
        elif self.content < key:
             #None or recursion
             if self.right is None:
                 return None
             return self.right.search(key)
        elif self.content > key:
            if self.left is None:
                return None
            return self.left.search(key)
        else:
            #this should NEVER happen (throw exception?)
            print "WARNING[in BST.search()]: Unexpected if branch"
            return

    def copy(self):
        """Returns a copy of the tree"""
        newnodes = [x.content for x in self.preorder()]
        copy = BST()
        copy.add(newnodes)
        return copy

    def delete(self, key):
        """Delete the node with value equal to key. Deletion rules:
            * If the node is a leaf, simply delete it
            * If the node only has one child, assign child to parent
            * If the node has two children, copy node's inorder successor's
            content to node's content and delete the successor"""

        #recursively find the parent of the node for deletion
        isLeftChild = True
        if self.left is None and self.right is None:
            return -1 #node not found
        elif self.left.content == key:
            isLeftChild = True
            parent = self
            node = self.left
        elif self.right.content == key:
            isLeftChild = False
            parent = self
            node = self.right
        elif self.content < key:
            return self.right.delete(key) #key in right subtree
        elif self.content > key:
            return self.left.delete(key) #key in left subtree
        else:
            #THIS HAPPENS! DEBUG! (@deleting root of tree)
            print "WARNING[in BST.delete()]: unexpected if branch"
            return


        #case 1: node is leaf
        if node.left is None and node.right is None:
            if isLeftChild: #which leaf to delete, left or right
                parent.left = None
            else:
                parent.right = None
            return
        #case 2a: node has only a right child
        elif node.left is None and node.right is not None:
            if isLeftChild:
                parent.left = node.right
            else:
                parent.right = node.right
            return
        #case 2b: node has only a left child
        elif node.right is None and node.left is not None:
            if isLeftChild:
                parent.left = node.left
            else:
                parent.right = node.left
            return
        #case 3: node has 2 children
        else:
            #find inorder successor of node
            inorder = node.inorder()
            successor = binary_search([x.content for x in inorder], key) + 1
            node.content = inorder[successor].content
            node.delete(node.content)
            return




    def inorder(self):
        """Returns the nodes of the tree in inorder traversal

        Note: since this is a BST, this is the increasing order of the nodes!
        """
        nodes = []
        if self.left:
            nodes.extend(self.left.inorder())
        nodes.append(self)
        if self.right:
            nodes.extend(self.right.inorder())

        return nodes

    def preorder(self):
        """Returns the nodes of the tree in preorder traversal"""
        nodes = [self]
        if self.left:
            nodes.extend(self.left.preorder())
        if self.right:
            nodes.extend(self.right.preorder())
        return nodes

    def postorder(self):
        """Returns the nodes of the tree in postorder traversal"""
        nodes = []
        if self.left:
            nodes.extend(self.left.postorder())
        if self.right:
            nodes.extend(self.right.postorder())
        nodes.append(self)
        return nodes


def main():
    myBST = BST()
    anArray = [50, 30, 70, 20, 40, 60, 80]
    myBST.add(anArray)
    print myBST
    myBST.delete(20)
    print myBST
    myBST.delete(30)
    print myBST
    myBST.delete(70)
    print myBST
    return

if __name__ == "__main__":
    main()
