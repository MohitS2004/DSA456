# DSA456 Assignment 3 - Table Implementations

## Overview
This assignment implements and analyzes different table data structures, focusing on hash tables with collision resolution strategies.

## Files

- `analysis.md` - Part A: Time complexity analysis of SortedTable member functions
- `hash_tables.py` - Part B: Implementation of ChainingTable and LinearProbingTable
- `sorted_table.py` - Original SortedTable implementation (provided for reference)
- `test_tables.py` - Unit tests for hash table implementations

## Part A: SortedTable Analysis

Analyzes the time complexity of the following functions:
- `insert(key, value)` - O(n²)
- `modify(key, value)` - O(n)
- `remove(key)` - O(n)
- `search(key)` - O(n)
- `capacity()` - O(1)
- `__len__()` - O(n)

See `analysis.md` for detailed analysis and improvement suggestions.

## Part B: Hash Table Implementations

Implements two hash table variants:

### ChainingTable
- Uses chaining for collision resolution
- Load factor threshold: 1.0
- Grows by doubling capacity when threshold exceeded

### LinearProbingTable
- Uses linear probing for collision resolution
- Load factor threshold: 0.7
- Grows by doubling capacity when threshold exceeded

## Usage

```python
# ChainingTable example
table = ChainingTable(capacity=16)
table.insert("key1", "value1")
table.insert("key2", "value2")
value = table.search("key1")  # Returns "value1"
table.modify("key1", "new_value")
table.remove("key2")

# LinearProbingTable example
table = LinearProbingTable(capacity=16)
table.insert("key1", "value1")
table.insert("key2", "value2")
value = table.search("key1")  # Returns "value1"
table.modify("key1", "new_value")
table.remove("key2")
```

## Running Tests

```bash
python test_tables.py
```

## Requirements

- Python 3.x
- No external libraries (uses only built-in Python features)

## Author

Assignment for DSA456 - Fall 2025
