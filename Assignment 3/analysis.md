# Part A: SortedTable Analysis

## Time Complexity Analysis

### 1. `insert(self, key, value)`

**Time Complexity: O(n²)**

**Analysis:**
- `self.search(key)` is called first → O(n) - linear search through the table
- If the table is full, capacity doubling occurs → O(n) - copying all elements to new table
- Adding the new record at the end → O(1)
- Bubble sort to maintain sorted order → O(n²) - nested loops with comparisons and swaps
- **Overall:** O(n) + O(n) + O(n²) = **O(n²)** dominated by bubble sort

**Issues:**
- Bubble sort is highly inefficient
- Search is performed using linear search despite the table being sorted

---

### 2. `modify(self, key, value)`

**Time Complexity: O(n)**

**Analysis:**
- Linear search through the table until the key is found → O(n)
- Modifying the value once found → O(1)
- **Overall:** **O(n)**

**Issues:**
- Despite the table being sorted, linear search is used instead of binary search
- Could be optimized to O(log n) with binary search

---

### 3. `remove(self, key)`

**Time Complexity: O(n)**

**Analysis:**
- Linear search to find the key → O(n)
- Shifting all elements after the removed element left → O(n)
- Setting the last element to None → O(1)
- **Overall:** O(n) + O(n) = **O(n)**

**Issues:**
- Linear search instead of binary search
- Shifting operation is unavoidable for maintaining contiguous array

---

### 4. `search(self, key)`

**Time Complexity: O(n)**

**Analysis:**
- Linear search through the table until the key is found → O(n)
- **Overall:** **O(n)**

**Issues:**
- **Major inefficiency:** The table is sorted, but linear search is used
- Should use binary search for O(log n) complexity

---

### 5. `capacity(self)`

**Time Complexity: O(1)**

**Analysis:**
- Simply returns the stored capacity value → O(1)
- **Overall:** **O(1)**

**No issues - optimal implementation**

---

### 6. `__len__(self)`

**Time Complexity: O(n)**

**Analysis:**
- Iterates through the entire table counting non-None elements → O(n)
- **Overall:** **O(n)**

**Issues:**
- Should maintain a counter variable to track the number of records
- Could be optimized to O(1) by storing the count as an instance variable

---

## Part B: Suggestions for Improvement

### Major Improvements:

1. **Use Binary Search Instead of Linear Search**
   - Since the table is sorted, implement binary search for `search()`, `modify()`, and `remove()`
   - This would reduce complexity from O(n) to O(log n)

2. **Replace Bubble Sort with Binary Search Insertion**
   - Instead of adding to the end and bubble sorting, find the correct position using binary search
   - Insert at that position by shifting elements once
   - This would reduce `insert()` from O(n²) to O(n)

3. **Maintain a Size Counter**
   - Add `self.size` variable to track the number of records
   - Update it during `insert()` and `remove()`
   - Makes `__len__()` O(1) instead of O(n)

4. **Optimize the Search in Insert**
   - The `insert()` method calls `search()` to check for duplicates
   - When doing binary search insertion, this check can be integrated
   - Eliminates redundant search operation

### Summary Table:

| Function | Current Complexity | Improved Complexity | Improvement Method |
|----------|-------------------|---------------------|-------------------|
| insert() | O(n²) | O(n) | Binary search + single shift |
| modify() | O(n) | O(log n) | Binary search |
| remove() | O(n) | O(n) | Binary search (shift is unavoidable) |
| search() | O(n) | O(log n) | Binary search |
| capacity() | O(1) | O(1) | Already optimal |
| __len__() | O(n) | O(1) | Maintain size counter |
