"""
DSA456 Assignment 3 - Unit Tests
Tests for ChainingTable and LinearProbingTable implementations
"""

from hash_tables import ChainingTable, LinearProbingTable


def test_chaining_table():
    """Test ChainingTable implementation"""
    print("Testing ChainingTable...")
    
    table = ChainingTable(capacity=8)
    
    # Test insert
    assert table.insert("key1", "value1") == True
    assert table.insert("key2", "value2") == True
    assert table.insert("key3", "value3") == True
    assert table.insert("key1", "duplicate") == False  # Duplicate key
    print("✓ Insert tests passed")
    
    # Test search
    assert table.search("key1") == "value1"
    assert table.search("key2") == "value2"
    assert table.search("key3") == "value3"
    assert table.search("nonexistent") == None
    print("✓ Search tests passed")
    
    # Test modify
    assert table.modify("key1", "new_value1") == True
    assert table.search("key1") == "new_value1"
    assert table.modify("nonexistent", "value") == False
    print("✓ Modify tests passed")
    
    # Test length
    assert len(table) == 3
    print("✓ Length tests passed")
    
    # Test capacity
    assert table.capacity() == 8
    print("✓ Capacity tests passed")
    
    # Test remove
    assert table.remove("key2") == True
    assert table.search("key2") == None
    assert len(table) == 2
    assert table.remove("nonexistent") == False
    print("✓ Remove tests passed")
    
    # Test growth (load factor > 1.0)
    for i in range(10):
        table.insert(f"grow_key{i}", f"grow_value{i}")
    assert table.capacity() > 8  # Should have grown
    assert table.search("grow_key5") == "grow_value5"
    print("✓ Growth tests passed")
    
    # Test collision handling
    table2 = ChainingTable(capacity=4)
    table2.insert("a", 1)
    table2.insert("e", 2)  # May collide with "a"
    table2.insert("i", 3)  # May collide with "a" and "e"
    assert table2.search("a") == 1
    assert table2.search("e") == 2
    assert table2.search("i") == 3
    print("✓ Collision handling tests passed")
    
    print("All ChainingTable tests passed!\n")


def test_linear_probing_table():
    """Test LinearProbingTable implementation"""
    print("Testing LinearProbingTable...")
    
    table = LinearProbingTable(capacity=16)
    
    # Test insert
    assert table.insert("key1", "value1") == True
    assert table.insert("key2", "value2") == True
    assert table.insert("key3", "value3") == True
    assert table.insert("key1", "duplicate") == False  # Duplicate key
    print("✓ Insert tests passed")
    
    # Test search
    assert table.search("key1") == "value1"
    assert table.search("key2") == "value2"
    assert table.search("key3") == "value3"
    assert table.search("nonexistent") == None
    print("✓ Search tests passed")
    
    # Test modify
    assert table.modify("key1", "new_value1") == True
    assert table.search("key1") == "new_value1"
    assert table.modify("nonexistent", "value") == False
    print("✓ Modify tests passed")
    
    # Test length
    assert len(table) == 3
    print("✓ Length tests passed")
    
    # Test capacity
    assert table.capacity() == 16
    print("✓ Capacity tests passed")
    
    # Test remove (tombstone method)
    assert table.remove("key2") == True
    assert table.search("key2") == None
    assert len(table) == 2
    assert table.remove("nonexistent") == False
    print("✓ Remove tests passed")
    
    # Test growth (load factor > 0.7)
    table2 = LinearProbingTable(capacity=8)
    for i in range(6):  # 6/8 = 0.75 > 0.7, should trigger growth
        table2.insert(f"grow_key{i}", f"grow_value{i}")
    assert table2.capacity() > 8  # Should have grown
    assert table2.search("grow_key3") == "grow_value3"
    print("✓ Growth tests passed")
    
    # Test collision handling with linear probing
    table3 = LinearProbingTable(capacity=4)
    table3.insert("a", 1)
    table3.insert("e", 2)  # May collide with "a"
    table3.insert("i", 3)  # May collide with "a" and "e"
    assert table3.search("a") == 1
    assert table3.search("e") == 2
    assert table3.search("i") == 3
    print("✓ Collision handling tests passed")
    
    # Test tombstone handling
    table4 = LinearProbingTable(capacity=8)
    table4.insert("test1", "value1")
    table4.insert("test2", "value2")
    table4.remove("test1")
    assert table4.search("test1") == None
    assert table4.search("test2") == "value2"  # Should still find test2
    table4.insert("test3", "value3")  # Should reuse tombstone slot
    assert table4.search("test3") == "value3"
    print("✓ Tombstone handling tests passed")
    
    print("All LinearProbingTable tests passed!\n")


def test_comprehensive():
    """Comprehensive tests for both implementations"""
    print("Running comprehensive tests...")
    
    # Test with various data types as keys
    for TableClass in [ChainingTable, LinearProbingTable]:
        table = TableClass()
        
        # String keys
        table.insert("string_key", "string_value")
        assert table.search("string_key") == "string_value"
        
        # Integer keys
        table.insert(42, "int_value")
        assert table.search(42) == "int_value"
        
        # Tuple keys (immutable)
        table.insert((1, 2), "tuple_value")
        assert table.search((1, 2)) == "tuple_value"
        
        print(f"✓ {TableClass.__name__} handles various key types")
    
    # Test large dataset
    for TableClass in [ChainingTable, LinearProbingTable]:
        table = TableClass(capacity=32)
        
        # Insert 100 records
        for i in range(100):
            assert table.insert(f"key_{i}", i * 2) == True
        
        # Verify all records
        for i in range(100):
            assert table.search(f"key_{i}") == i * 2
        
        # Modify all records
        for i in range(100):
            assert table.modify(f"key_{i}", i * 3) == True
        
        # Verify modifications
        for i in range(100):
            assert table.search(f"key_{i}") == i * 3
        
        # Remove half the records
        for i in range(0, 100, 2):
            assert table.remove(f"key_{i}") == True
        
        # Verify removals
        for i in range(0, 100, 2):
            assert table.search(f"key_{i}") == None
        for i in range(1, 100, 2):
            assert table.search(f"key_{i}") == i * 3
        
        print(f"✓ {TableClass.__name__} handles large dataset")
    
    print("All comprehensive tests passed!\n")


if __name__ == "__main__":
    print("=" * 50)
    print("DSA456 Assignment 3 - Hash Table Tests")
    print("=" * 50 + "\n")
    
    test_chaining_table()
    test_linear_probing_table()
    test_comprehensive()
    
    print("=" * 50)
    print("All tests completed successfully! ✓")
    print("=" * 50)
