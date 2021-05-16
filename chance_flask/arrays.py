"""Module with arrays implementations"""
import ctypes


# Implements the Array ADT using array capabilities of the ctypes module.

class Array:
    """Creates an array with size elements"""
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)
        # Put min-max values
        self.minimal = 200
        self.maximal = 0

    def min(self):
        """Returns minimal value in the array"""
        return self.minimal

    def max(self):
        """Returns maximal value in the array"""
        return self.maximal

    def average(self):
        """Returns average value in the array"""
        sum_elements = 0
        for element in self:
            sum_elements += element
        return round(sum_elements / self._size, 3)

    def __len__(self):
        """Returns the size of the array"""
        return self._size

    def __getitem__(self, index: int):
        """Gets the contents of the index element"""
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index: int, value):
        """Puts the value in the array element at index position"""
        assert 0 <= index < len(self), "Array subscript out of range"
        self._elements[index] = value

        if value > self.maximal:
            self.maximal = value
        if value < self.minimal:
            self.minimal = value

    def clear(self, value):
        """Clears the array by setting each element to the given value"""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """ Returns the array's iterator for traversing the elements"""
        return _ArrayIterator(self._elements)

    def __repr__(self):
        """Returns a string that represents array"""
        repr_str = '['
        for element in self:
            repr_str += str(element) + ', '
        return repr_str[:len(repr_str)-2] + ']'

class _ArrayIterator:
    """Represents iterator for the Array ADT"""
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration



class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    @staticmethod
    def _make_array(c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def __repr__(self):
        """Returns a string that represents dynamic array"""
        repr_str = '['
        for element in self:
            repr_str += str(element) + ', '
        return repr_str[:len(repr_str)-2] + ']'
