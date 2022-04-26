# Name: Mitchell
# OSU Email: davismit@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 4/25/22
# Description: Creates methods for a dynamic array object for various manipulations


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Resizes a DynamicArray capacity to new_capacity
        """
        #print(new_capacity >= self._size)
        if new_capacity > 0 and new_capacity >= self._size:
            self._capacity = new_capacity
            old_data = self._data
            old_size = self._size
            self._data = StaticArray(new_capacity)
            self._size = 0
            #print("size is " + str(self._size))
            for index in range(old_size):
                #print(
                self.append(old_data.get(index))
                #print(self._data[index])


    def append(self, value: object) -> None:
        """
        appends an input value on the end of the DynamicArray _data Static Array, increasing size
        Doubles Capacity if overflowed
        """
        if self._size >= self._capacity:
            self.resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        inserts an input value into the input index, and shifts all subsequent values 1
        doubles capacity if overflowed
        """
        if index > self._size or index < 0:
            raise DynamicArrayException()
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        if index == self._size:
            self.append(value)
        else:
            old_data = self._data
            old_size = self._size
            self._data = StaticArray(self._capacity)
            self._size = 0

            for i in range(old_size):
                if i == index:
                    self.append(value)
                self.append(old_data[i])


    def remove_at_index(self, index: int) -> None:
        """
        Removes the value at the specified index and shift all subsequent values to fill
        Halves capacity of DA if less than a quarter is occupied
        """
        #Initial checks
        if index >= self._size or index < 0 or self._size == 0:
            raise DynamicArrayException()

        #check if resize is needed, then resize
        if self._capacity > 10 and self._size < self._capacity / 4:
            new_size = self._size * 2
            if new_size < 10:
                new_size = 10
            self.resize(new_size)

        #remove at index

        old_data = self._data
        old_size = self._size
        self._data = StaticArray(self._capacity)
        self._size = 0

        #Copy every value of the old array unless at the removal index
        for i in range(old_size):
            if i != index:
                self.append(old_data[i])


    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        returns a DynamicArray that is a subset of the DA starting at input index with the specified size
        """
        #input validation


        if start_index < 0 or start_index >= self._size or start_index + size > self._size or size < 0:
            raise DynamicArrayException()
        if size == 0:
            return DynamicArray()

        #iterate "size" number of times and
        new_da = DynamicArray()
        index = start_index
        for i in range(size):
            new_da.append(self.get_at_index(index))
            index += 1

        return new_da

    def merge(self, second_da: "DynamicArray") -> None:
        """
        appends all values of the second_da in order to the end of the self DA
        """
        for i in range(second_da._size):
            self.append(second_da[i])

    def map(self, map_func) -> "DynamicArray":
        """
        accepts a function as a parameter and performs that function on all values of the DA
        returns a different DA of the results of each
        """
        new_da = DynamicArray()
        for i in range(self._size):
            new_da.append(map_func(self[i]))
        return new_da

    def filter(self, filter_func) -> "DynamicArray":
        """
        Accepts a function and returns a DA of all values that return True when the function is applied
        """
        new_da = DynamicArray()
        for i in range(self._size):
            if filter_func(self[i]):
                new_da.append(self[i])
        return new_da

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Sequentially applies a function to each value of the DA, with a cumulative result
        accepts an initializer to be the starting value
        """
        new_da = DynamicArray()


        i = 0
        if initializer is not None:
            cumulative_value = initializer
            #Corner case handling, if no values, just return initializer if present
            if self._size == 0:
                return cumulative_value
        else:
            #corner case handling, if no values or initializer, return None
            if self._size == 0:
                return None
            cumulative_value = self[i]
            i += 1


        while i < self._size:
            cumulative_value = (reduce_func(cumulative_value, self[i]))
            #print(f"debug {cumulative_value}")
            i += 1

        return cumulative_value

def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    TODO: Write this implementation
    """
    mode_da = DynamicArray()

    current_val = arr[0]
    current_count = 0
    max_count = 0
    current_leader = False

    for i in range(arr.length()):
        if arr[i] == current_val:
            current_count += 1
            #If current counter matched the max - first time

        else:
            current_val = arr[i]
            current_count = 1
            current_leader = False

        if current_count == max_count and current_leader is False:
            current_leader = True
            mode_da.append(current_val)
        if current_count > max_count:
            current_leader = True
            mode_da = DynamicArray()
            mode_da.append(current_val)
            max_count = current_count
    return(mode_da, max_count)





# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# MD TEST - remove at index")
    da = DynamicArray()
    try:
        da.remove_at_index(0)
    except Exception as e:
        print("Exception raised: ", type(e))

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")

    print("gradescope failed test")
    da = DynamicArray()
    da.append(54789)
    print(da)
    try:
        print(da.slice(1,0))
    except:
        print("Exception raised")