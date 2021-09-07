from __future__ import print_function
from builtins import input
from builtins import range
from builtins import object
class Node(object):
    def __init__(self, data: int) -> int:
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, new_data: int) -> int:
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return self.head.data

    def middle_element(self) -> int:
        """
        >>> link = LinkedList()
        >>> link.middle_element()
        No element found.
        >>> link.push(5)
        5
        >>> link.push(6)
        6
        >>> link.push(8)
        8
        >>> link.push(8)
        8
        >>> link.push(10)
        10
        >>> link.push(12)
        12
        >>> link.push(17)
        17
        >>> link.push(7)
        7
        >>> link.push(3)
        3
        >>> link.push(20)
        20
        >>> link.push(-20)
        -20
        >>> link.middle_element()
        12
        >>>
        """
        slow_pointer = self.head
        fast_pointer = self.head
        if self.head:
            while fast_pointer and fast_pointer.__next__:
                fast_pointer = fast_pointer.next.__next__
                slow_pointer = slow_pointer.__next__
            return slow_pointer.data
        else:
            print("No element found.")


if __name__ == "__main__":
    link = LinkedList()
    for i in range(int(input().strip())):
        data = int(input().strip())
        link.push(data)
    print(link.middle_element())
