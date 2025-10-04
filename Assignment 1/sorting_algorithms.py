import random
import time
import matplotlib.pyplot as plt
import copy

# Test case generators
def generate_best_case(size, algorithm_type):
    """Generate best case scenario for different algorithms"""
    if algorithm_type in ['bubble', 'insertion', 'insertion_range']:
        # Already sorted list is best case for bubble and insertion sort
        return list(range(1, size + 1))
    elif algorithm_type == 'selection':
        # Selection sort has same complexity regardless, but sorted is conceptually best
        return list(range(1, size + 1))
    elif algorithm_type == 'quick':
        # Best case for quicksort is when pivot always divides evenly
        # We'll use a sorted list as a reasonable best case
        return list(range(1, size + 1))

def generate_worst_case(size, algorithm_type):
    """Generate worst case scenario for different algorithms"""
    if algorithm_type in ['bubble', 'insertion', 'insertion_range']:
        # Reverse sorted list is worst case for bubble and insertion sort
        return list(range(size, 0, -1))
    elif algorithm_type == 'selection':
        # Reverse sorted is worst case for selection sort too
        return list(range(size, 0, -1))
    elif algorithm_type == 'quick':
        # Worst case for quicksort is when pivot is always smallest/largest
        return list(range(size, 0, -1))

def generate_average_case(size):
    """Generate average case scenario (random list)"""
    return [random.randint(1, size * 2) for _ in range(size)]

def explain_cases():
    """Explain best, worst, and average case scenarios"""
    print("\n=== EXPLANATION OF BEST, WORST, AND AVERAGE CASES ===")
    print("\nBUBBLE SORT:")
    print("- Best Case O(n): Already sorted list - only n-1 comparisons, no swaps")
    print("- Worst Case O(n²): Reverse sorted list - maximum comparisons and swaps")
    print("- Average Case O(n²): Random list - expected n²/4 swaps")
    
    print("\nSELECTION SORT:")
    print("- Best Case O(n²): Always n²/2 comparisons regardless of input")
    print("- Worst Case O(n²): Same as best case - always scans remaining elements")
    print("- Average Case O(n²): Always n²/2 comparisons, n swaps")
    
    print("\nINSERTION SORT:")
    print("- Best Case O(n): Already sorted list - only n-1 comparisons")
    print("- Worst Case O(n²): Reverse sorted list - each element compared with all previous")
    print("- Average Case O(n²): Random list - each element compared with half of previous")
    
    print("\nQUICK SORT:")
    print("- Best Case O(n log n): Pivot always divides list evenly")
    print("- Worst Case O(n²): Pivot is always smallest/largest element")
    print("- Average Case O(n log n): Random pivot selection with good partitioning")
    print("=" * 60)

def bubble_sort(my_list, count_operations=False):
    """Bubble sort with optional operation counting"""
    if count_operations:
        return bubble_sort_with_count(my_list)
    
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

def bubble_sort_with_count(my_list):
    """Bubble sort that counts operations and returns T(n)"""
    operations = 0
    n = len(my_list)
    operations += 1  # n assignment
    
    for i in range(n - 1):
        operations += 1  # loop condition check
        for j in range(n - 1 - i):
            operations += 1  # inner loop condition check
            operations += 1  # comparison my_list[j] > my_list[j + 1]
            if my_list[j] > my_list[j + 1]:
                operations += 3  # 3 operations for the swap
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    
    return operations

def selection_sort(my_list, count_operations=False):
    """Selection sort with optional operation counting"""
    if count_operations:
        return selection_sort_with_count(my_list)
    
    n = len(my_list)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list

def selection_sort_with_count(my_list):
    """Selection sort that counts operations and returns T(n)"""
    operations = 0
    n = len(my_list)
    operations += 1  # n assignment
    
    for i in range(n - 1):
        operations += 1  # loop condition check
        min_idx = i
        operations += 1  # min_idx assignment
        
        for j in range(i + 1, n):
            operations += 1  # inner loop condition check
            operations += 1  # comparison my_list[j] < my_list[min_idx]
            if my_list[j] < my_list[min_idx]:
                min_idx = j
                operations += 1  # min_idx assignment
        
        operations += 3  # swap operation
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    
    return operations

def insertion_sort(my_list, count_operations=False):
    """Insertion sort with optional operation counting"""
    if count_operations:
        return insertion_sort_with_count(my_list)
    
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
    return my_list

def insertion_sort_with_count(my_list):
    """Insertion sort that counts operations and returns T(n)"""
    operations = 0
    
    for i in range(1, len(my_list)):
        operations += 1  # loop condition check
        key = my_list[i]
        operations += 1  # key assignment
        j = i - 1
        operations += 1  # j assignment
        
        while j >= 0 and my_list[j] > key:
            operations += 2  # while condition checks (j >= 0 and comparison)
            my_list[j + 1] = my_list[j]
            operations += 1  # array assignment
            j -= 1
            operations += 1  # j decrement
        
        my_list[j + 1] = key
        operations += 1  # final key assignment
    
    return operations

def quick_sort(my_list, count_operations=False):
    """Quicksort with optional operation counting"""
    if count_operations:
        operations = [0]  # Use list to maintain reference across recursive calls
        result = quick_sort_with_count(my_list, operations)
        return operations[0]
    
    if len(my_list) <= 1:
        return my_list
    
    pivot = my_list[len(my_list) // 2]
    left = [x for x in my_list if x < pivot]
    middle = [x for x in my_list if x == pivot]
    right = [x for x in my_list if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_with_count(my_list, operations):
    """Quicksort that counts operations and returns sorted list"""
    operations[0] += 1  # length check
    if len(my_list) <= 1:
        return my_list
    
    pivot = my_list[len(my_list) // 2]
    operations[0] += 1  # pivot assignment
    
    left = []
    middle = []
    right = []
    
    for x in my_list:
        operations[0] += 1  # comparison with pivot
        if x < pivot:
            left.append(x)
            operations[0] += 1  # append operation
        elif x == pivot:
            operations[0] += 1  # second comparison
            middle.append(x)
            operations[0] += 1  # append operation
        else:
            operations[0] += 1  # second comparison
            right.append(x)
            operations[0] += 1  # append operation
    
    left_sorted = quick_sort_with_count(left, operations)
    right_sorted = quick_sort_with_count(right, operations)
    
    operations[0] += len(left_sorted) + len(middle) + len(right_sorted)  # list concatenation
    return left_sorted + middle + right_sorted

def insertion_sort_range(my_list, left, right, count_operations=False):
    """Insertion sort for a specific range with optional operation counting"""
    if count_operations:
        return insertion_sort_range_with_count(my_list, left, right)
    
    for i in range(left + 1, right + 1):
        key = my_list[i]
        j = i - 1
        while j >= left and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
    return my_list

def insertion_sort_range_with_count(my_list, left, right):
    """Insertion sort for range that counts operations and returns T(n)"""
    operations = 0
    
    for i in range(left + 1, right + 1):
        operations += 1  # loop condition check
        key = my_list[i]
        operations += 1  # key assignment
        j = i - 1
        operations += 1  # j assignment
        
        while j >= left and my_list[j] > key:
            operations += 2  # while condition checks (j >= left and comparison)
            my_list[j + 1] = my_list[j]
            operations += 1  # array assignment
            j -= 1
            operations += 1  # j decrement
        
        my_list[j + 1] = key
        operations += 1  # final key assignment
    
    return operations

def test_tn_calculations():
    """Test T(n) calculations with best, worst, and average cases"""
    print("\n=== TESTING T(n) CALCULATIONS ===")
    test_size = 100
    
    algorithms = [
        ('Bubble Sort', bubble_sort, 'bubble'),
        ('Selection Sort', selection_sort, 'selection'),
        ('Insertion Sort', insertion_sort, 'insertion'),
        ('Quick Sort', quick_sort, 'quick'),
    ]
    
    for name, func, algo_type in algorithms:
        print(f"\n{name}:")
        
        # Best case
        best_case = generate_best_case(test_size, algo_type)
        best_case_copy = copy.deepcopy(best_case)
        best_operations = func(best_case_copy, count_operations=True)
        
        # Worst case  
        worst_case = generate_worst_case(test_size, algo_type)
        worst_case_copy = copy.deepcopy(worst_case)
        worst_operations = func(worst_case_copy, count_operations=True)
        
        # Average case
        average_case = generate_average_case(test_size)
        average_case_copy = copy.deepcopy(average_case)
        average_operations = func(average_case_copy, count_operations=True)
        
        print(f"  Best case operations: {best_operations}")
        print(f"  Worst case operations: {worst_operations}")
        print(f"  Average case operations: {average_operations}")

def measure_operations_vs_size():
    """Measure T(n) vs n for different list sizes using worst case"""
    sizes = [10, 50, 100, 500, 1000, 5000]  # Reduced for performance
    algorithms = [
        ('Bubble Sort', bubble_sort, 'bubble'),
        ('Selection Sort', selection_sort, 'selection'),
        ('Insertion Sort', insertion_sort, 'insertion'),
        ('Quick Sort', quick_sort, 'quick'),
    ]
    
    results = {name: [] for name, _, _ in algorithms}
    
    print("\n=== MEASURING OPERATIONS VS SIZE ===")
    for size in sizes:
        print(f"Testing size {size}...")
        for name, func, algo_type in algorithms:
            # Use worst case scenario
            test_list = generate_worst_case(size, algo_type)
            test_copy = copy.deepcopy(test_list)
            operations = func(test_copy, count_operations=True)
            results[name].append(operations)
            print(f"  {name}: {operations} operations")
    
    # Plot results
    plt.figure(figsize=(12, 8))
    for name in results:
        plt.plot(sizes, results[name], marker='o', label=name)
    
    plt.xlabel('List Size (n)')
    plt.ylabel('Number of Operations T(n)')
    plt.title('Algorithm Performance: Operations vs List Size (Worst Case)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('operations_vs_size.png')
    plt.show()
    
    return results

def measure_time_vs_size():
    """Measure execution time vs n for different list sizes using worst case"""
    sizes = [10, 50, 100, 500, 1000, 5000]  # Reduced for performance
    algorithms = [
        ('Bubble Sort', bubble_sort, 'bubble'),
        ('Selection Sort', selection_sort, 'selection'),
        ('Insertion Sort', insertion_sort, 'insertion'),
        ('Quick Sort', quick_sort, 'quick'),
    ]
    
    time_results = {name: [] for name, _, _ in algorithms}
    
    print("\n=== MEASURING EXECUTION TIME VS SIZE ===")
    for size in sizes:
        print(f"Testing size {size}...")
        for name, func, algo_type in algorithms:
            # Use worst case scenario
            test_list = generate_worst_case(size, algo_type)
            test_copy = copy.deepcopy(test_list)
            
            # Measure execution time
            start_time = time.time()
            func(test_copy, count_operations=False)  # Don't count operations, just time
            end_time = time.time()
            
            execution_time = end_time - start_time
            time_results[name].append(execution_time)
            print(f"  {name}: {execution_time:.6f} seconds")
    
    # Plot results
    plt.figure(figsize=(12, 8))
    for name in time_results:
        plt.plot(sizes, time_results[name], marker='o', label=name)
    
    plt.xlabel('List Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Algorithm Performance: Execution Time vs List Size (Worst Case)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('time_vs_size.png')
    plt.show()
    
    return time_results
    """Test all sorting algorithms with a list of 100 elements"""
    # Generate a random list of 100 elements
    test_list = [random.randint(1, 1000) for _ in range(100)]
    print(f"Original list (first 10): {test_list[:10]}...")
    
    # Test bubble sort
    bubble_list = copy.deepcopy(test_list)
    bubble_sorted = bubble_sort(bubble_list)
    print(f"Bubble sort result (first 10): {bubble_sorted[:10]}...")
    print(f"Bubble sort is correctly sorted: {bubble_sorted == sorted(test_list)}")
    
    # Test selection sort
    selection_list = copy.deepcopy(test_list)
    selection_sorted = selection_sort(selection_list)
    print(f"Selection sort result (first 10): {selection_sorted[:10]}...")
    print(f"Selection sort is correctly sorted: {selection_sorted == sorted(test_list)}")
    
    # Test insertion sort
    insertion_list = copy.deepcopy(test_list)
    insertion_sorted = insertion_sort(insertion_list)
    print(f"Insertion sort result (first 10): {insertion_sorted[:10]}...")
    print(f"Insertion sort is correctly sorted: {insertion_sorted == sorted(test_list)}")
    
    # Test quick sort
    quick_list = copy.deepcopy(test_list)
    quick_sorted = quick_sort(quick_list)
    print(f"Quick sort result (first 10): {quick_sorted[:10]}...")
    print(f"Quick sort is correctly sorted: {quick_sorted == sorted(test_list)}")
    
    # Test insertion sort range
    range_list = copy.deepcopy(test_list)
    range_sorted = insertion_sort_range(range_list, 0, len(range_list) - 1)
    print(f"Insertion sort range result (first 10): {range_sorted[:10]}...")
    print(f"Insertion sort range is correctly sorted: {range_sorted == sorted(test_list)}")

def main():
    """Test all sorting algorithms with a list of 100 elements"""
    # Generate a random list of 100 elements
    test_list = [random.randint(1, 1000) for _ in range(100)]
    print(f"Original list (first 10): {test_list[:10]}...")
    
    # Test bubble sort
    bubble_list = copy.deepcopy(test_list)
    bubble_sorted = bubble_sort(bubble_list)
    print(f"Bubble sort result (first 10): {bubble_sorted[:10]}...")
    print(f"Bubble sort is correctly sorted: {bubble_sorted == sorted(test_list)}")
    
    # Test selection sort
    selection_list = copy.deepcopy(test_list)
    selection_sorted = selection_sort(selection_list)
    print(f"Selection sort result (first 10): {selection_sorted[:10]}...")
    print(f"Selection sort is correctly sorted: {selection_sorted == sorted(test_list)}")
    
    # Test insertion sort
    insertion_list = copy.deepcopy(test_list)
    insertion_sorted = insertion_sort(insertion_list)
    print(f"Insertion sort result (first 10): {insertion_sorted[:10]}...")
    print(f"Insertion sort is correctly sorted: {insertion_sorted == sorted(test_list)}")
    
    # Test quick sort
    quick_list = copy.deepcopy(test_list)
    quick_sorted = quick_sort(quick_list)
    print(f"Quick sort result (first 10): {quick_sorted[:10]}...")
    print(f"Quick sort is correctly sorted: {quick_sorted == sorted(test_list)}")
    
    # Test insertion sort range
    range_list = copy.deepcopy(test_list)
    range_sorted = insertion_sort_range(range_list, 0, len(range_list) - 1)
    print(f"Insertion sort range result (first 10): {range_sorted[:10]}...")
    print(f"Insertion sort range is correctly sorted: {range_sorted == sorted(test_list)}")

def comprehensive_main():
    """Comprehensive test of all sorting algorithms and analysis"""
    print("=== SORTING ALGORITHMS ANALYSIS ===")
    
    # Step 1: Test basic sorting functionality with 100 elements
    print("\n=== STEP 1: BASIC SORTING TEST (100 elements) ===")
    test_list = [random.randint(1, 1000) for _ in range(100)]
    print(f"Original list (first 10): {test_list[:10]}...")
    
    # Test bubble sort
    bubble_list = copy.deepcopy(test_list)
    bubble_sorted = bubble_sort(bubble_list)
    print(f"Bubble sort result (first 10): {bubble_sorted[:10]}...")
    print(f"Bubble sort is correctly sorted: {bubble_sorted == sorted(test_list)}")
    
    # Test selection sort
    selection_list = copy.deepcopy(test_list)
    selection_sorted = selection_sort(selection_list)
    print(f"Selection sort result (first 10): {selection_sorted[:10]}...")
    print(f"Selection sort is correctly sorted: {selection_sorted == sorted(test_list)}")
    
    # Test insertion sort
    insertion_list = copy.deepcopy(test_list)
    insertion_sorted = insertion_sort(insertion_list)
    print(f"Insertion sort result (first 10): {insertion_sorted[:10]}...")
    print(f"Insertion sort is correctly sorted: {insertion_sorted == sorted(test_list)}")
    
    # Test quick sort
    quick_list = copy.deepcopy(test_list)
    quick_sorted = quick_sort(quick_list)
    print(f"Quick sort result (first 10): {quick_sorted[:10]}...")
    print(f"Quick sort is correctly sorted: {quick_sorted == sorted(test_list)}")
    
    # Test insertion sort range
    range_list = copy.deepcopy(test_list)
    range_sorted = insertion_sort_range(range_list, 0, len(range_list) - 1)
    print(f"Insertion sort range result (first 10): {range_sorted[:10]}...")
    print(f"Insertion sort range is correctly sorted: {range_sorted == sorted(test_list)}")
    
    # Step 2: Test T(n) calculations
    print("\n=== STEP 2: T(n) CALCULATION TESTING ===")
    explain_cases()
    test_tn_calculations()
    
    # Example from assignment for bubble sort
    print("\n=== ASSIGNMENT EXAMPLE: BUBBLE SORT WITH 50 ELEMENTS ===")
    listSize = 50
    rand_list = [random.randint(0, 101) for val in range(listSize)]
    rand_list.sort(reverse=True)  # Worst case scenario
    print(f"Worst case list for bubble sort (size {listSize})")
    bubble_steps = bubble_sort(copy.deepcopy(rand_list), count_operations=True)
    print(f"Steps needed for sorting: {bubble_steps}")
    
    # Step 3: Plot T(n) vs n
    print("\n=== STEP 3: PLOTTING T(n) VS n ===")
    operation_results = measure_operations_vs_size()
    
    # Step 4: Plot execution time vs n
    print("\n=== STEP 4: PLOTTING EXECUTION TIME VS n ===")
    time_results = measure_time_vs_size()
    
    # Analysis
    print("\n=== ANALYSIS AND INTERPRETATION ===")
    print("1. THEORETICAL COMPLEXITY:")
    print("   - Bubble Sort: O(n²) worst case, O(n) best case")
    print("   - Selection Sort: O(n²) all cases")
    print("   - Insertion Sort: O(n²) worst case, O(n) best case")
    print("   - Quick Sort: O(n²) worst case, O(n log n) average case")
    
    print("\n2. OBSERVED RESULTS:")
    print("   - The operation count plots should show quadratic growth for bubble, selection, and insertion sorts")
    print("   - Quick sort may show quadratic behavior in worst case (reverse sorted input)")
    print("   - Time measurements may vary due to implementation details and system performance")
    
    print("\n3. COMPARISON:")
    print("   - Operation counts provide theoretical insight into algorithm efficiency")
    print("   - Actual timing includes overhead from Python interpreter and system factors")
    print("   - Both metrics should generally follow the same trends for complexity analysis")

if __name__ == "__main__":
    # Run basic main first
    main()
    
    # Then run comprehensive analysis
    print("\n" + "="*60)
    comprehensive_main()