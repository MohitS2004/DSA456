# in this assignment used sentinal node with doubly linkedlist

class Node:
    def __init__(self, data, next = None, prev = None) -> None:

        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data

class LinkedList:
    def __init__(self, front = None, back = None) -> None:

        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        self._size = 0

    def insert(self, data):
        cur = self.sentinel.next
        while cur is not self.sentinel and cur.data < data:
            cur = cur.next
        node = Node(data)
        prev = cur.prev
        prev.next = node
        node.prev = prev
        node.next = cur
        cur.prev = node
        self._size += 1
        return node

    def remove(self, data):
        cur = self.sentinel.next
        while cur is not self.sentinel:
            if cur.data == data:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                self._size -= 1
                return True
            cur = cur.next
        return False

    def is_present(self, data):
        cur = self.sentinel.next
        while cur is not self.sentinel:
            if cur.data == data:
                return True
            if cur.data > data:
                return False
            cur = cur.next
        return False

    def __len__(self):
        return self._size


"""
PART C: TIME COMPLEXITY ANALYSIS
=================================

Let n = number of nodes in the linked list

1. insert(self, data) - O(n)
   ------------------------
   Best case: O(1)
   - Occurs when inserting the smallest value (new front element)
   - We immediately find that sentinel.next.data >= new data
   - Only need to update 4 pointers, no traversal required
   
   Worst case: O(n)
   - Occurs when inserting the largest value (new back element)
   - Must traverse all n nodes to reach the sentinel at the end
   - Then perform constant-time pointer updates
   
   Average case: O(n)
   - On average, we traverse approximately n/2 nodes
   - Still linear in terms of n
   
   Explanation:
   The function walks through the list comparing each node's data with the new value
   until it finds the correct insertion position. In the worst case, this requires
   checking all n nodes. The actual insertion (4 pointer updates) is O(1), but the
   search dominates, giving us O(n) overall complexity.


2. remove(self, data) - O(n)
   -------------------------
   Best case: O(1)
   - Occurs when removing the first element
   - Found immediately at sentinel.next
   - Pointer updates are constant time
   
   Worst case: O(n)
   - Occurs when removing the last element or when element doesn't exist
   - Must traverse all n nodes to find it (or determine it's not present)
   
   Average case: O(n)
   - On average, element is found after checking n/2 nodes
   
   Explanation:
   Must perform linear search through the list to find the node containing the data.
   Once found, removal is O(1) (just 2 pointer updates), but the search takes O(n)
   in the worst case. We can't use binary search because linked lists don't support
   random access, even though they're sorted.


3. is_present(self, data) - O(n)
   ------------------------------
   Best case: O(1)
   - Occurs when data is at the front, OR
   - When the first node's value is already greater than search value
     (we can stop immediately due to sorted property)
   
   Worst case: O(n)
   - Occurs when data is at the end, OR
   - When data is larger than all elements (must check all n nodes)
   
   Average case: O(n)
   - Even with early stopping optimization, average is still linear
   
   Explanation:
   This is a linear search through the sorted list. While we have an optimization
   that stops if cur.data > search_value (using the sorted property), this doesn't
   change the worst-case complexity. We still need to potentially check all n nodes.
   The sorted property helps in practice but doesn't improve Big-O complexity.


4. __len__(self) - O(1)
   --------------------
   Best case: O(1)
   Worst case: O(1)
   Average case: O(1)
   
   Explanation:
   This function simply returns the self._size variable, which is maintained as
   nodes are inserted and removed. No traversal or computation is needed - it's
   just a variable lookup, which is constant time regardless of list size.


SUMMARY OF BIG-O COMPLEXITIES:
===============================
insert(data):      O(n) - must traverse to find insertion position
remove(data):      O(n) - must traverse to find node to remove
is_present(data):  O(n) - must traverse to find node (linear search)
__len__():         O(1) - direct variable access

IMPORTANT NOTE:
All three search-based operations (insert, remove, is_present) are O(n) because
linked lists do not support random access. Even though our list is sorted, we
cannot use binary search (which would be O(log n)) because we cannot jump to
the middle element in constant time. We must traverse from the beginning,
following next pointers sequentially.

If we needed O(log n) search, we would use a different data structure like
a balanced binary search tree (AVL, Red-Black tree) or skip list.
"""


# Testing
if __name__ == "__main__":
    lst = LinkedList()
    
    # Test insert - maintains sorted order
    for v in [3, 1, 4, 2, 5, 2]:
        lst.insert(v)
    
    # Test __len__
    print("Length:", len(lst))
    
    # Test is_present
    print("is_present(2):", lst.is_present(2))
    print("is_present(9):", lst.is_present(9))
    
    # Test remove
    print("remove(2):", lst.remove(2))
    print("remove(9):", lst.remove(9))
    
    print("Final length:", len(lst))
