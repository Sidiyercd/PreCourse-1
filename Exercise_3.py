# Time Complexity : O(n)
#  Space Complexity :
#  Did this code successfully run on Leetcode :
#  Any problem you faced while coding this :

# implement Singly linked list
class ListNode:
    """
    A node in a singly-linked list.
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        new_node = ListNode(data)
        new_node.set_next(self.head)
        self.head = new_node

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == False:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data is not in the list")
        return current

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == key:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
