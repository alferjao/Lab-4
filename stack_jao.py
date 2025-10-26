class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def print_stack(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current = self.top
            print("Stack elements (top → bottom):")
            while current:
                print(current.data)
                current = current.next

    # a. remove_beginning(self)
    def remove_beginning(self):
        if self.top is None:
            return None
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data

    # b. remove_at_end(self)
    def remove_at_end(self):
        if self.top is None:
            return None
        if self.top.next is None:
            removed_data = self.top.data
            self.top = None
            return removed_data

        current = self.top
        while current.next.next:
            current = current.next

        removed_data = current.next.data
        current.next = None
        return removed_data

    # c. remove_at(self, data)
    def remove_at(self, data):
        if self.top is None:
            return None

        # If the node to remove is the top
        if self.top.data == data:
            removed_data = self.top.data
            self.top = self.top.next
            return removed_data

        current = self.top
        while current.next:
            if current.next.data == data:
                removed_data = current.next.data
                current.next = current.next.next
                return removed_data
            current = current.next

        # Data not found
        return None
