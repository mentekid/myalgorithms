"""Implements a basic Queue using a Python list
Author: Yannis Mentekidis
Date: August 12, 2015
"""

class queue:
    """Queue data structure

    Testing:
    >>> alist = [1, 2, 3, 4, 5] #test constructor
    >>> Q = queue(alist)
    >>> print Q #test __repr__
    1 2 3 4 5

    >>> Q.enqueue(6) #test enqueue function
    >>> print Q
    1 2 3 4 5 6

    >>> alist = [7, 8, 9]
    >>> Q.extend(alist) #test extend function
    >>> print Q
    1 2 3 4 5 6 7 8 9

    >>> print [Q.dequeue() for i in range(10)] #test dequeue function
    [1, 2, 3, 4, 5, 6, 7, 8, 9, None]

    >>> Q = queue() #test empty constructor
    >>> Q.enqueue(1)
    >>> Q.enqueue(2)
    >>> Q.enqueue(3)
    >>> print Q
    1 2 3
    >>> print [Q[i] for i in range(10)] #test __getitem__
    [1, 2, 3, None, None, None, None, None, None, None]

    >>> Q = queue([1, 2, 3, 4]) #test copy (modifying S leaves Q unaffected)
    >>> S = Q.copy()
    >>> S.enqueue(5)
    >>> S
    1 2 3 4 5
    >>> Q
    1 2 3 4
    """
    def __init__(self, alist = list()):
        """Turns a list into a new Queue"""
        self.bottom = 0
        self.top = len(alist) #points one above the top item
        self.content = alist[:] #force copy

    def enqueue(self, item):
        """Adds a new item to the end of the queue"""
        self.content.append(item)
        self.top = len(self.content)

    def dequeue(self):
        """Removes and returns item 0, if it exists. Returns None if not"""
        if self.top == self.bottom:
            return None #empty queue
        else:
            self.top -= 1
            return self.content.pop(0)

    def extend(self, alist):
        """Adds all items on a list to the end of the queue"""
        self.content.extend(alist)
        self.top = len(self.content)

    def peek(self, i = 0):
        """Returns item i from the queue without removing it."""
        if i >= self.top:
            return None
        return self.content[i]

    def copy(self):
        """Returns a copy of the stack"""
        return queue(self.content)

    def __getitem__(self, index):
        """Overload for the [] operator"""
        return self.peek(index)

    def __repr__(self):
        """Overload for print"""
        return ' '.join([str(item) for item in self.content])

def main():
    pass

if __name__ == "__main__":
    main()
