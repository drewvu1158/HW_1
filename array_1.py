class array_1:
    def __init__(self, capacity):
        """Capacity is the static size of the array. Each index is initialized to None"""
        self._items = []
        self.logical_size = 0
        for i in range(capacity):
            self._items.append(None)

    def __len__(self):
        """Returns the capacity of this Array"""
        return len(self._items)

    def get_logical_size(self):
        """Returns the number of items in the array that arent NULL"""
        return self.logical_size

    def __str__(self):
        """Returns a string representation of this Array"""
        return str(self._items)

    def __iter__(self):
        """Returns an iterator over the Array"""
        return iter(self._items)

    def __getitem__(self, index):
        """Return the item at the given index"""
        return self._items[index]

    def __eq__(self, other):
        """Returns True if the two arrays are equal, False otherwise"""
        return self._items == other
    
    
    def __setitem__(self, index, new_item):
        """Adds the value 'new_item' to the array at the given index"""
        if index > self.logical_size:
            print("Index has not reached that point yet")
        elif new_item == "None":
            if index > self.logical_size:
                print("Index has not reached that point yet")
            if index + 1 == self.logical_size:
                self._items[index] = new_item
                self.logical_size = self.logical_size - 1
            else:
                print(
                    "Index is too small to delete, it needs to be the last index of the array, please try again!"
                )

        else:
            self._items[index] = new_item
            self.logical_size += 1
