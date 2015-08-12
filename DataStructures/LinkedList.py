""" Linked List implementation in Python
Author: Yannis Mentekidis
Date: August 12, 2015
"""

class Node:
    def __init__(self, idx, value, prev = None, nxt = None):
        self.idx = idx
        self.value = value
        self.prev = prev
        self.nxt = nxt

    def setnxt(self, nxt):
        self.nxt = nxt

    def getnxt(self):
        return self.nxt

    def setprev(self, prev):
        self.prev = prev

    def getprev(self):
        return self.prev

    def __repr__(self):
        return "[" + str(self.idx) + ":" + str(self.value) + "]"

class LinkedList:
    """
    >>> L = LinkedList(['a', 'b', 'c', 'd']) #test constructor and overloads
    >>> print L
    [0:a], [1:b], [2:c], [3:d]
    >>> len(L)
    4
    >>> L[0]
    'a'
    >>> L[-1]
    Traceback (most recent call last):
        ...
    IndexError

    >>> L.append('e') #test append, extend
    >>> L
    [0:a], [1:b], [2:c], [3:d], [4:e]

    >>> L.extend(['f', 'g', 'h'])
    >>> L[5]
    'f'
    >>> L[6]
    'g'
    >>> L[7]
    'h'

    >>> L.pop(0) #test pop
    [0:a]
    >>> print [L.pop(0) for i in range(5)]
    [[0:b], [0:c], [0:d], [0:e], [0:f]]
    >>> L.pop(len(L)-1)
    [1:h]
    >>> L.pop(1)
    Traceback (most recent call last):
        ...
    IndexError

    >>> L = LinkedList() #test empty constructor and insert, search
    >>> L.insert('b')
    >>> L.insert('a', 0)
    >>> L.insert('c')
    >>> L
    [0:a], [1:b], [2:c]

    >>> L.search('b')
    1
    >>> L.search('f')
    -1

    """

    def __init__(self, alist = list()):
        """Insert items from alist into the linked list"""
        self.length = len(alist) #first empty position in LinkedList

        if self.length == 0: #empty list -> empty LinkedList
            self.start = Node(None, None, None, None)
            return

        self.start = Node(0, alist[0])
        current = self.start
        for i in range(1, self.length):
            temp = Node(i, alist[i], current, None)
            current.setnxt(temp) #add temp to the linked list
            current = temp
        return


    def __len__(self):
        return self.length


    def __repr__(self):
        """Prints the LinkedList, separated by commas. Format: [idx:value]"""
        reprstr = str(self.start)
        current = self.start
        if len(self) == 0:
            return '[]'
        while current.getnxt() is not None:
            current = current.getnxt()
            reprstr += ', ' + str(current)
        return reprstr

    def __getitem__(self, index):
        """Overload for [] operation"""
        return self.get(index)

    def append(self, item):
        """Insert a single item at the end of the LinekdList"""
        if len(self) == 0: #empty list
            self.start = Node(0, item, None, None)
            self.length = 1
            return
        current = self.start
        while(current.nxt is not None): #traverse till you find end
            current = current.getnxt()

        new = Node(self.length, item, current, None) #new item at end of list
        current.setnxt(new) #add new item
        self.length+=1 #count new item


    def extend(self, alist):
        """Add all items in alist into the LinkedList"""
        for item in alist:
            self.append(item)
        return


    def insert(self, item, position = None):
        """Add an item to a given point in the LinkedList"""

        if len(self) == 0: #empty list
            self.start = Node(0, item, None, None)
            self.length = 1
            return

        if position == None: #default position is end of list
            position = self.length

        if position == self.length: #if position is end of list, append's job
            self.append(item)
            return
        elif position > self.length or position < 0: #if list is not big enough, stop
            raise(IndexError)
        elif position == 0: #special case - add to LinkedList beginning
            pos = 0
            new = Node(0, item, None, self.start)
            self.start = new
        else: #general case: position is in range 1:N
            current = self.start
            pos = 0
            #find insertion position
            while current.getnxt() is not None and pos < position - 1:
                current = current.getnxt()
                pos += 1

            #insert between current and current's next
            prev = current
            nxt = prev.getnxt()
            new = Node(position, item, prev, nxt)
            prev.setnxt(new)
            nxt.setprev(new)

        #increment all indices after insertion point
        current = new
        while current.getnxt() is not None:
            current = current.getnxt()
            current.idx += 1
        self.length += 1
        return

    def search(self, key):
        """Sequential search for a key in LinkedList"""
        current = self.start
        pos = 0
        while current is not None:
            if current.value == key:
                return pos
            pos += 1
            current = current.getnxt()
        return -1

    def get(self, idx):
        """Return the value of item number idx"""
        if idx < 0 or idx >= len(self):
            raise(IndexError) #index out of bounds
        pos = 0
        current = self.start

        while True:
            if idx == pos:
                return current.value
            pos+=1
            current = current.getnxt()

    def pop(self, idx = 0):
        """Remove item idx from the LinkedList"""
        pos = 0
        current = self.start

        if idx >= len(self) or idx < 0:
            raise(IndexError) #index out of bounds

        #find deletion position
        while pos < idx and current is not None:
            pos += 1
            current = current.getnxt()

        #current is the item to be deleted
        deleted = current
        previous = deleted.getprev()
        newnext = deleted.getnxt()
        if previous is not None: #happens when trying to delete item 0
            previous.setnxt(newnext)
        else:
            self.start = newnext

        if newnext is not None: #happens when trying to delete item N
            newnext.setprev(previous)

        current = newnext
        while current is not None:
            current.idx -= 1
            current = current.getnxt()
        self.length -= 1

        return deleted
