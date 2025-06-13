#Prajwal Srivastava
#Week 2 Assignment

# singly linked list using OOP and delete nth node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if self.head is None:
                raise Exception("Cannot delete from an empty list.")
            if n <= 0:
                raise Exception("Invalid index. Index should be 1 or more.")
            if n == 1:
                self.head = self.head.next
                return
            current = self.head
            count = 1
            while current is not None and count < n - 1:
                current = current.next
                count += 1
            if current is None or current.next is None:
                raise Exception("Index out of range.")
            current.next = current.next.next
        except Exception as e:
            print("Error:", e)

my_list = LinkedList()
my_list.add_node(10)
my_list.add_node(20)
my_list.add_node(30)
my_list.add_node(40)

print("Original list:")
my_list.print_list()

print("\nDeleting 2nd node:")
my_list.delete_nth_node(2)
my_list.print_list()

print("\nTrying to delete 10th node:")
my_list.delete_nth_node(10)

print("\nTrying to delete from empty list:")
empty_list = LinkedList()
empty_list.delete_nth_node(1)
