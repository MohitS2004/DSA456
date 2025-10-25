from typing import Any, Optional, List

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        """
        Initializes an empty linked list.
        Time Complexity: O(1) - Constant time
        """
        self.head = None

    def is_empty(self) -> bool:
        """
        Returns True if the linked list is empty, False otherwise.
        Time Complexity: O(1) - Constant time, just checking if head is None
        """
        return self.head is None

    def prepend(self, data: Any):
        """
        Insert a new node containing data at the beginning of the linked list.
        Time Complexity: O(1) - Constant time, always inserting at head
        """
        new_node = Node(data, self.head)
        self.head = new_node

    def append(self, data: Any):
        """
        Inserts a new node containing data at the end of the linked list.
        Time Complexity: O(n) - Linear time, must traverse entire list to find the end
        """
        new_node = Node(data)
        
        # If list is empty, new node becomes the head
        if self.is_empty():
            self.head = new_node
            return
        
        # Traverse to the last node
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Append the new node
        current.next = new_node

    def insert_after(self, target: Node, data: Any):
        """
        Inserts a new node containing data after the node target.
        Time Complexity: O(1) - Constant time, direct insertion after target node
        """
        if target is None:
            return
        
        new_node = Node(data, target.next)
        target.next = new_node

    def delete(self, target: Node) -> bool:
        """
        Deletes the node target from the linked list.
        Returns True if the deletion was successful, False otherwise.
        Time Complexity: O(n) - Linear time, must traverse list to find the node before target
        """
        if self.is_empty() or target is None:
            return False
        
        # Special case: deleting the head node
        if self.head == target:
            self.head = self.head.next
            return True
        
        # Find the node before the target
        current = self.head
        while current.next is not None:
            if current.next == target:
                current.next = target.next
                return True
            current = current.next
        
        return False  # Target not found

    def search(self, data: Any) -> Optional[Node]:
        """
        Searches the linked list for a node containing data.
        Returns the node if it's found, None otherwise.
        Time Complexity: O(n) - Linear time, worst case traverses entire list
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self) -> int:
        """
        Returns the number of nodes in the linked list.
        Time Complexity: O(n) - Linear time, must count all nodes
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def to_list(self) -> List[Any]:
        """
        Returns a list containing the data in the linked list in order.
        Time Complexity: O(n) - Linear time, must visit all nodes
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def print(self):
        """
        Prints all the elements in the linked list.
        Time Complexity: O(n) - Linear time, must visit all nodes
        """
        if self.is_empty():
            print("Empty list")
            return
        
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements))


# ============================================================================
# PART B: BIG-O ANALYSIS
# ============================================================================
"""
Big-O Analysis of Singly Linked List Operations (where n = size of the list):

1. __init__(self)
   T(n) = O(1)
   O(n) = O(1)
   Analysis: Simply initializes head to None. No iteration required.

2. is_empty(self) -> bool
   T(n) = O(1)
   O(n) = O(1)
   Analysis: Only checks if head is None. Single comparison operation.

3. prepend(self, data: Any)
   T(n) = O(1)
   O(n) = O(1)
   Analysis: Creates new node and sets it as head. No traversal needed.

4. append(self, data: Any)
   T(n) = O(n)
   O(n) = O(n)
   Analysis: Must traverse entire list to find the last node. In worst case,
   visits all n nodes.

5. insert_after(self, target: Node, data: Any)
   T(n) = O(1)
   O(n) = O(1)
   Analysis: Direct insertion after target node. No traversal needed since
   target node is already provided.

6. delete(self, target: Node) -> bool
   T(n) = O(n)
   O(n) = O(n)
   Analysis: Must traverse list to find the node before target. In worst case
   (target is last node or not found), visits all n nodes.

7. search(self, data: Any) -> Optional[Node]
   T(n) = O(n)
   O(n) = O(n)
   Analysis: Must potentially traverse entire list to find the node. In worst
   case (data not found or at end), visits all n nodes.

8. size(self) -> int
   T(n) = O(n)
   O(n) = O(n)
   Analysis: Must count all nodes in the list by traversing from head to end.
   Always visits all n nodes.

9. to_list(self) -> List[Any]
   T(n) = O(n)
   O(n) = O(n)
   Analysis: Must visit every node to extract data into a list. Always visits
   all n nodes.

10. print(self)
    T(n) = O(n)
    O(n) = O(n)
    Analysis: Must visit every node to print its data. Always visits all n nodes.

SUMMARY:
- O(1) operations: __init__, is_empty, prepend, insert_after
- O(n) operations: append, delete, search, size, to_list, print

Key Insight: Operations at the beginning of the list (prepend) are fast O(1),
but operations at the end (append) or requiring search are slow O(n) because
we must traverse the list. This is a fundamental characteristic of singly
linked lists without a tail pointer.
""" 

