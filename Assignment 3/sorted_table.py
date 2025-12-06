"""
DSA456 Assignment 3 - SortedTable Implementation (Provided for Reference)
This is the original implementation with inefficiencies for analysis purposes.
"""


class SortedTable:
    # packaging the key-value pair into one object
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, cap=32):
        # this initializes a list of of capacity length with None
        self.the_table = [None for i in range(cap)]
        self.cap = cap

    def insert(self, key, value):
        if (self.search(key) != None):
            return False

        if (len(self) == self.cap):
            # increase the capacity if list is full
            new_table = [None for i in range(self.cap * 2)]
            for i in range(self.cap):
                new_table[i] = self.the_table[i]
            self.the_table = new_table
            self.cap *= 2

        self.the_table[len(self)] = self.Record(key, value)
        size = len(self)
        for i in range(0, size - 1):
            for j in range(0, size - 1 - i):
                if (self.the_table[j].key > self.the_table[j + 1].key):
                    tmp = self.the_table[j]
                    self.the_table[j] = self.the_table[j + 1]
                    self.the_table[j + 1] = tmp
        return True

    def modify(self, key, value):
        i = 0
        while (i < len(self) and self.the_table[i].key != key):
            i += 1
        if (i == len(self)):
            return False
        else:
            self.the_table[i].value = value
            return True

    def remove(self, key):
        i = 0
        size = len(self)
        while (i < size and self.the_table[i].key != key):
            i += 1
        if (i == size):
            return False
        while (i + 1 < size):
            self.the_table[i] = self.the_table[i + 1]
            i += 1
        self.the_table[i] = None
        return True

    def search(self, key):
        i = 0
        size = len(self)
        while i < size and self.the_table[i].key != key:
            i += 1
        if i == size:
            return None
        else:
            return self.the_table[i].value

    def capacity(self):
        return self.cap

    def __len__(self):
        i = 0
        count = 0
        while (i < len(self.the_table)):
            if (self.the_table[i] != None):
                count += 1
            i += 1
        return count
