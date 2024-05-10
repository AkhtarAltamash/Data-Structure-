
# # For Singly Linked List

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# if __name__ == "__main__":
#     # Creating a Singly Linked List
#     sll = SinglyLinkedList()

#     # Appending elements to the linked list
#     sll.append(1)
#     sll.append(2)
#     sll.append(3)
#     sll.append(4)

#     # Displaying the linked list
#     sll.display()
#     sll.append(8)
#     sll.display()


# ________________________________

# for dubbly linked list

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#         new_node.prev = current

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" <-> ")
#             current = current.next
#         print("None")

# if __name__ == "__main__":
#     # Creating a Doubly Linked List
#     dll = DoublyLinkedList()

#     # Appending elements to the linked list
#     dll.append(1)
#     dll.append(2)
#     dll.append(3)
#     dll.append(4)

#     # Displaying the linked list
#     dll.display()


# ________________________________________

# for circular linked list 

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class CircularLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             new_node.next = self.head
#             return
#         current = self.head
#         while current.next != self.head:
#             current = current.next
#         current.next = new_node
#         new_node.next = self.head

#     def display(self):
#         if not self.head:
#             print("List is empty")
#             return
#         current = self.head
#         while True:
#             print(current.data, end=" -> ")
#             current = current.next
#             if current == self.head:
#                 break
#         print("(Head)")

# if __name__ == "__main__":
#     # Creating a Circular Linked List
#     cll = CircularLinkedList()

#     # Appending elements to the linked list
#     cll.append(1)
#     cll.append(2)
#     cll.append(3)
#     cll.append(4)

#     # Displaying the linked list
#     cll.display()


# ____________________________My code _______________________________________________

# Singly

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next =None
        
        
# #create nodes:

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)

# #connecting node 

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# # Printing the linked list 

# current = node1

# while current is not None:
#     print(current.data, end=" --> ")
#     current=current.next
    
# print("None")


# ________________________


# double 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# # Creating nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# # Connecting nodes
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# node3.next = node4
# node4.prev = node3
# node4.next = None  # Setting the next attribute of the last node to None

# current = node1

# while current is not None:
#     print(current.data, end=" --> ")
#     current = current.next

# print("None")


# _________________________________________

# circular

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Creating nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# # Connecting nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node1  # Making the last node point back to the first node

# current = node1

# while True:
#     print(current.data, end=" --> ")
#     current = current.next
#     if current == node1:
#         break

# print("(Head)")
