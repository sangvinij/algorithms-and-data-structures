# one-linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class ListNode:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def remove(self, data):
        if self.head is None:
            raise ValueError("empty list")

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        raise ValueError("element not in list")

    def get(self, index):
        if index < 0:
            raise IndexError("index must be positive")

        current_node = self.head
        current_index = 0

        while current_node:
            if current_index == index:
                return current_node.data

            current_node = current_node.next
            current_index += 1

        raise IndexError("index out of range")

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __str__(self):
        elements = []
        current_node = self.head

        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next

        return f"ListNode({' -> '.join(elements)})"


# doubly-linked-list


class Node2:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node

    def remove(self, data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next:
                    current_node.next.prev = current_node.prev

                return

            current_node = current_node.next

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert(self, data, position):
        if position <= 0:
            self.prepend(data)
        else:
            new_node = Node(data)
            current_node = self.head
            current_position = 0

            while current_node:
                if current_position == position - 1:
                    new_node.prev = current_node
                    new_node.next = current_node.next

                    if current_node.next:
                        current_node.next.prev = new_node

                    current_node.next = new_node
                    return

                current_node = current_node.next
                current_position += 1

            self.append(data)

    def __iter__(self):
        current_node = self.head

        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __str__(self):
        elements = []
        current_node = self.head

        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next

        return f"DoublyLinkedList({' <-> '.join(elements)})"
