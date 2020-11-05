class DynamicList():

    def __init__(self) -> None:
        self._size = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)

    def __len__(self):
        return self._size

    def _check_index_in_bounds(self, index):
        if not 0 <= index < self._size:
            raise IndexError('index is out of bounds')

    def __getitem__(self, index):
        self._check_index_in_bounds(index)
        return self._array[index]

    def __repr__(self):
        items_str = ', '.join(list(map(str, [val for val in self._array if val])))
        return f'[{items_str}]'

    def append(self, element):
        if self._size == self._capacity:
            self._resize(2*self._capacity)  # arbitrary doubling up the capacity

        self._array[self._size] = element
        self._size += 1

    def remove(self, index):
        self._check_index_in_bounds(index)
        array_prefix = self._array[0:index]
        array_suffix = self._array[index + 1:]
        self._array = array_prefix + array_suffix
        self._size -= 1
        self._capacity -= 1

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for index in range(self._size):
            new_array[index] = self._array[index]

        self._array = new_array
        self._capacity = new_capacity

    def _make_array(self, capacity):
        return [None] * capacity
