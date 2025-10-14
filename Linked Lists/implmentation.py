# linked list are, as the name suggest , a list which is linked.
# It contains of nodes which contain data and a pointer to the next node in the list
#  The list is connected with the help of these pointers.
# These nodes are scattered in memory , quite like the buckets in a hash table
# the node where the list starts is called the head of the list and
# node where it ends, or is called the tail of the list.
# The average time complexity of some operations involving linked list as follows:
# Look-up : O(n)
# Insert: O(n)
# delete: O(n)
# Append: O(1)
# preappend: O(1)

# Python doesn't have a built-in implemenation of linked lists, we have to build it
# on our own. So, here we follows

#First we define a class Node which will act as a blueprint for each of our nodes.

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if  self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def insert(self, position, data):
        if position >= self.length:
            if position > self.length:
                print("The position not available, inserting at the end of the list")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length +=1


    def print_list(self):
        if self.head == None:
            print("empty")
        else:
            current_node = self.head
            while(current_node != None):
                print(current_node.data, end=" ")
                current_node = current_node.next
        print()

    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        while current_node.next != None and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next != None:
            current_node.next =  current_node.next.next
            if current_node.next == None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Given value not found")

    def delete_by_position(self, position):
        if self.head == None:
            print("Linked list is empty. Nothing to delete")
            return
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return

        if position >= self.length:
            position = self.length - 1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return

ll = LinkedList()
ll.append(10)
ll.print_list()
ll.append(20)
ll.print_list()
ll.insert(2,30)
ll.print_list()
ll.delete_by_position(2)
ll.print_list()
ll.delete_by_position(1)
ll.print_list()
ll.delete_by_position(0)
ll.print_list()

