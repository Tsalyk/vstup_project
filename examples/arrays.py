"""
File: arrays.py
An Array is a restricted list whose clients can use
only [], len, iter, and str.
To instantiate, use
<variable> = array(<capacity>, <optional fill value>)
The fill value is None by default.
"""


class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self._items[index] = newItem


class ArrayExpanded(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        self._logicalSize = 0
        # Track the capacity and fill value for adjustments later
        self._capacity = capacity
        self._fillValue = fillValue
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index.
        Precondition: 0 <= index < size()"""
        #if index < 0 or index >= self.size():
        #    raise IndexError("Array index out of bounds")
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Precondition: 0 <= index < size()"""
        #if index < 0 or index >= self.size():
        #    raise IndexError("Array index out of bounds")
        self._items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        return self._logicalSize

    def grow(self):
        """Increases the physical size of the array if necessary."""
        # Double the physical size if no more room for items
        # and add the fillValue to the new cells in the underlying list
        for count in range(len(self)):
            self._items.append(self._fillValue)

    def shrink(self):
        """Decreases the physical size of the array if necessary."""
        # Shrink the size by half but not below the default capacity
        # and remove those garbage cells from the underlying list
        newSize = max(self._capacity, len(self) // 2)
        for count in range(len(self) - newSize):
            self._items.pop()

    def insert(self, index, newItem):
        """Inserts item at index in the array."""
        if self.size() == len(self):
            self.grow()
        if index >= self.size():
            self._items[self.size()] = newItem
        else:
            index = max(index, 0)
            # Shift items down by one position
            for i in range(self.size(), index, -1):
                self._items[i] = self._items[i - 1]

            # Add new item and increment logical size
            self._items[index] = newItem
        self._logicalSize += 1

    def pop(self, index):
        """Removes and returns item at index in the array.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        itemToReturn = self._items[index]
        # Shift items up by one position
        for i in range(index, self.size() - 1):
            self._items[i] = self._items[i + 1]
        # Reset empty slot to fill value
        self._items[self.size() - 1] = self._fillValue
        self._logicalSize -= 1
        if self.size() <= len(self) // 4 and len(self) > self._capacity:
            self.shrink()
        return itemToReturn

    def __eq__(self, other):
        """Returns True if the two arrays are equal or
        False otherwise."""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        if self.size() != other.size():
            return False
        for index in range(self.size()):
            if self[index] != other[index]:
                return False
        return True
