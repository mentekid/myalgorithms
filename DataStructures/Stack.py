"""Implements a Stack Data Structure using a Python list
Author: Yannis Mentekidis
Date: August 12, 2015
"""

class stack:
    """Stack data structure

    Testing:
    >>> alist = [1, 2, 3, 4, 5]
    >>> S = stack(alist)
    >>> print S
    1 2 3 4 5

    >>> S.push(6)
    >>> print S
    1 2 3 4 5 6

    >>> alist = [7, 8, 9]
    >>> S.extend(alist)
    >>> print S
    1 2 3 4 5 6 7 8 9

    >>> print [S.pop() for i in range(10)]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, None]

    >>> S = stack()
    >>> S.push(-1)
    >>> S.push(-2)
    >>> S.push(-3)
    >>> print [S[i] for i in range(4)]
    [-1, -2, -3, None]

    >>> S = stack([1, 2, 3, 4])
    >>> T = S.copy()
    >>> T.push(5)
    >>> T
    1 2 3 4 5
    >>> S
    1 2 3 4
    """
    def __init__(self, alist = list()):
        """Initialize a stack with a list (default empty)"""
        self.content = alist[:] #force copy
        self.bottom = 0
        self.top = len(self.content)
        return

    def push(self, item):
        """Add item to the top of the stack"""
        self.content.append(item)
        self.top = len(self.content)
        return

    def extend(self, alist):
        """Add all list items to top of the stack"""
        self.content.extend(alist)
        self.top = len(self.content)
        return

    def pop(self):
        """Remove top item or None if stack is empty"""
        if self.top == self.bottom:
            return None
        self.top -= 1
        return self.content.pop()

    def copy(self):
        """Return a copy of the stack (not a pointer)"""
        return stack(self.content)

    def __repr__(self):
        return ' '.join([str(c) for c in self.content])

    def __getitem__(self, index):
        if self.top <= index:
            return None
        return self.content[index]

def main():
    pass

if __name__ == "__main__":
    main()
