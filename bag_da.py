# Name: Mitchell Davis
# OSU Email: davismit@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 4/25/22
# Description: Creates methods to implement a Bag data structure and various manipulation methods


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Accepts an object and adds it to the Bag
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Accepts an object and removes ONE instance of that object from the Bag
        """
        for i in range(self._da.length()):
            if self._da[i] == value:
                self._da.remove_at_index(i)
                return True

        return False

    def count(self, value: object) -> int:
        """
        Accepts an object and returns the number of times that object is in the Bag
        """
        count = 0
        for i in range(self._da.length()):
            if self._da[i] == value:
                count += 1

        return count

    def clear(self) -> None:
        """
        Removes all objects from the Bag
        """
        for i in range(self._da.length()):
            self._da.remove_at_index(0)

    def equal(self, second_bag: "Bag") -> bool:
        """
        Determines if two bags contain all the same objects and quantities. Does not consider order
        """
        if self._da.length() != second_bag._da.length():
            return False
        self_val_list = Bag()
        for i in range(self._da.length()):
            if self_val_list.count(self._da[i]) == 0:
                self_val_list.add(self._da[i])
        for i in range(self_val_list._da.length()):
            if self.count(self_val_list._da[i]) != second_bag.count(self_val_list._da[i]):
                return False

        return True





    def __iter__(self):
        """
        Begins an iteration by starting an index variable
        """
        self._index = 0

        return self

    def __next__(self):
        """
        Returns the next value in the Bag, unless there are no more. Increments index to next Value
        """
        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index = self._index + 1
        return value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
