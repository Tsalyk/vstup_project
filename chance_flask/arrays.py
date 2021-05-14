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

    def clear(self, value):
        """Clears the array by setting each element to the given value"""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """ Returns the array's iterator for traversing the elements"""
        return _ArrayIterator(self._elements)


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
