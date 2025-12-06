"""
DSA456 Assignment 3 - Hash Table Implementations
Part B: ChainingTable and LinearProbingTable

Author: Assignment 3
Date: December 6, 2025
"""


class ChainingTable:
    """
    Hash table implementation using chaining for collision resolution.
    Uses a list of linked lists to handle collisions.
    Load factor threshold: 1.0
    """
    
    class Record:
        """Inner class to store key-value pairs"""
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
    
    def __init__(self, capacity=32):
        """Initialize table with given capacity (default 32)"""
        self.table = [None for _ in range(capacity)]
        self.cap = capacity
        self.size = 0
    
    def insert(self, key, value):
        """
        Insert a new key-value pair into the table.
        Returns True if successful, False if key already exists.
        Grows table if load factor exceeds 1.0
        """
        # Check if key already exists
        if self.search(key) is not None:
            return False
        
        # Calculate hash index
        idx = hash(key) % self.cap
        
        # Create new record
        new_record = self.Record(key, value)
        
        # Insert at the head of the chain
        if self.table[idx] is None:
            self.table[idx] = new_record
        else:
            new_record.next = self.table[idx]
            self.table[idx] = new_record
        
        self.size += 1
        
        # Check load factor and grow if necessary
        if self.size / self.cap > 1.0:
            self._grow()
        
        return True
    
    def modify(self, key, value):
        """
        Modify the value of an existing key.
        Returns True if successful, False if key not found.
        """
        idx = hash(key) % self.cap
        current = self.table[idx]
        
        while current is not None:
            if current.key == key:
                current.value = value
                return True
            current = current.next
        
        return False
    
    def remove(self, key):
        """
        Remove a key-value pair from the table.
        Returns True if successful, False if key not found.
        """
        idx = hash(key) % self.cap
        current = self.table[idx]
        prev = None
        
        while current is not None:
            if current.key == key:
                if prev is None:
                    # Removing head of chain
                    self.table[idx] = current.next
                else:
                    # Removing from middle or end
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        
        return False
    
    def search(self, key):
        """
        Search for a key in the table.
        Returns the value if found, None otherwise.
        """
        idx = hash(key) % self.cap
        current = self.table[idx]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def capacity(self):
        """Return the current capacity of the table"""
        return self.cap
    
    def __len__(self):
        """Return the number of records in the table"""
        return self.size
    
    def _grow(self):
        """Double the table capacity and rehash all records"""
        old_table = self.table
        self.cap *= 2
        self.table = [None for _ in range(self.cap)]
        self.size = 0
        
        # Rehash all records
        for chain_head in old_table:
            current = chain_head
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next


class LinearProbingTable:
    """
    Hash table implementation using linear probing for collision resolution.
    Uses tombstone method for deletions.
    Load factor threshold: 0.7
    """
    
    class Record:
        """Inner class to store key-value pairs"""
        def __init__(self, key, value):
            self.key = key
            self.value = value
    
    class Tombstone:
        """Marker for deleted records"""
        pass
    
    def __init__(self, capacity=32):
        """Initialize table with given capacity (default 32)"""
        self.table = [None for _ in range(capacity)]
        self.cap = capacity
        self.size = 0
    
    def insert(self, key, value):
        """
        Insert a new key-value pair into the table.
        Returns True if successful, False if key already exists.
        Grows table if load factor exceeds 0.7
        """
        # Check if key already exists
        if self.search(key) is not None:
            return False
        
        # Check load factor and grow if necessary
        if self.size / self.cap > 0.7:
            self._grow()
        
        # Find empty slot using linear probing
        idx = hash(key) % self.cap
        original_idx = idx
        
        while True:
            if self.table[idx] is None or isinstance(self.table[idx], self.Tombstone):
                self.table[idx] = self.Record(key, value)
                self.size += 1
                return True
            
            # Move to next slot
            idx = (idx + 1) % self.cap
            
            # Should never happen due to load factor check, but safety check
            if idx == original_idx:
                return False
    
    def modify(self, key, value):
        """
        Modify the value of an existing key.
        Returns True if successful, False if key not found.
        """
        idx = self._find_key(key)
        
        if idx is not None:
            self.table[idx].value = value
            return True
        
        return False
    
    def remove(self, key):
        """
        Remove a key-value pair from the table using tombstone method.
        Returns True if successful, False if key not found.
        """
        idx = self._find_key(key)
        
        if idx is not None:
            self.table[idx] = self.Tombstone()
            self.size -= 1
            return True
        
        return False
    
    def search(self, key):
        """
        Search for a key in the table.
        Returns the value if found, None otherwise.
        """
        idx = self._find_key(key)
        
        if idx is not None:
            return self.table[idx].value
        
        return None
    
    def capacity(self):
        """Return the current capacity of the table"""
        return self.cap
    
    def __len__(self):
        """Return the number of records in the table"""
        return self.size
    
    def _find_key(self, key):
        """
        Find the index of a key using linear probing.
        Returns the index if found, None otherwise.
        """
        idx = hash(key) % self.cap
        original_idx = idx
        
        while True:
            if self.table[idx] is None:
                # Empty slot means key not found
                return None
            
            if not isinstance(self.table[idx], self.Tombstone):
                if self.table[idx].key == key:
                    return idx
            
            # Move to next slot
            idx = (idx + 1) % self.cap
            
            # We've wrapped around
            if idx == original_idx:
                return None
    
    def _grow(self):
        """Double the table capacity and rehash all records"""
        old_table = self.table
        self.cap *= 2
        self.table = [None for _ in range(self.cap)]
        self.size = 0
        
        # Rehash all records
        for item in old_table:
            if item is not None and not isinstance(item, self.Tombstone):
                self.insert(item.key, item.value)
