# #Stack using Linked List

# class Node:
#     def __init__(self, value = None):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode  #yield is used to return value
#             curNode = curNode.next

# class Stack:
#     def __init__(self):
#         self.LinkedList = LinkedList()

#     def __str__(self):
#         values = [str(x.value) for x in self.LinkedList]
#         return '\n'.join(values)

#     def isEmpty(self):
#         if self.LinkedList.head ==None:
#             return True
#         else:
#             return False

#     def push(self,value):
#         node = Node(value)
#         node.next =self.LinkedList.head
#         self.LinkedList.head = node

#     def pop(self):
#         if self.isEmpty():
#             return "There is no element in the stack"
#         else:
#             nodeValue = self.LinkedList.head.value
#             self.LinkedList.head = self.LinkedList.head.next
#             return nodeValue
        
#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element in the stack"
#         else:
#             return self.LinkedList.head.value
        
#     def delete(self):
#         self.LinkedList.head = None

# customStack = Stack()

# print(customStack.isEmpty())

# customStack.push(1)
# customStack.push(2)
# customStack.push(3)

# print("Top element is:", customStack.peek())
# print("Popped element:", customStack.pop())
# print("Popped element:", customStack.pop())
# print("Top element is:", customStack.peek())

# customStack.delete()
# print(customStack)
# print(customStack.isEmpty())
# print(customStack.pop())

#=========================================================================================================================
# #Queue Linked List
# class Node:

#     def __init__(self, value=None):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return str(self.value)


# class LinkedList:

#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode   #We use yield to return value sequentially
#             curNode = curNode.next

# class Queue:

#     def __init__(self):
#         self.LinkedList = LinkedList()

#     def __str__(self):
#         values = [str(x.value) for x in self.LinkedList]
#         return '\n'.join(values)

#     def enqueue(self, value):
#         newNode = Node(value)
#         if self.LinkedList.head is None:
#             self.LinkedList.head = newNode
#             self.LinkedList.tail = newNode
#         else:
#             self.LinkedList.tail.next = newNode
#             self.LinkedList.tail = newNode

#     def isEmpty(self):
#         if self.LinkedList.head is None:
#             return True
#         else:
#             return False

#     def dequeue(self):
#         if self.isEmpty():
#             return "There is no node in the queue"
#         else:
#             tempNode = self.LinkedList.head
#             # If only one node exists
#             if self.LinkedList.head == self.LinkedList.tail:
#                 self.LinkedList.head = None
#                 self.LinkedList.tail = None

#             else:
#                 self.LinkedList.head = self.LinkedList.head.next
#             return tempNode.value

#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element in the queue"
#         else:
#             return self.LinkedList.head.value

# # Create Queue
# customQueue = Queue()

# # Insert elements
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)

# # Display Queue
# print("Queue Elements:")
# print(customQueue)

# # Peek front value
# print("Front Value:")
# print(customQueue.peek())

# # Remove element
# print("Dequeued Element:")
# print(customQueue.dequeue())

# # Display queue again
# print("Queue After Dequeue:")
# print(customQueue)

#========================================================================================================
#_________GRAPH________

# class Graph:

#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list.keys():
#             self.adjacency_list[vertex] = []
#             return True
#         return False

#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex, ":", self.adjacency_list[vertex])

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
#             self.adjacency_list[vertex1].append(vertex2)
#             self.adjacency_list[vertex2].append(vertex1)
#             return True
#         return False
    
#     def remove_vertex(self, vertex):
#         if vertex in self.adjacency_list.keys():
#             for other_vertex in self.adjacency_list[vertex]:
#                 self.adjacency_list[other_vertex].remove(vertex)
#             del self.adjacency_list[vertex]
#             return True
#         return False

# my_graph = Graph()

# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")
# my_graph.add_vertex("E")

# my_graph.add_edge("A", "B")
# my_graph.add_edge("A", "C")
# my_graph.add_edge("A", "D")
# my_graph.add_edge("B", "E")
# my_graph.add_edge("C", "D")
# my_graph.add_edge("D", "E")

# my_graph.print_graph()
# my_graph.remove_vertex("D")
# print("After removing the vertex: ")
# my_graph.print_graph()

#==========================================================================================
#Static Method#
# class Student:
#     #by using class name we can access static method
#     @staticmethod #decorator
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=",firstname,lastname)

#     @staticmethod
#     def contact_detail(mobile_no, rollno):
#         print("your contact detail=", mobile_no, rollno)

# Student.get_personal_detail("prashant","jha")
# Student.contact_detail(545654646,1001)

#============================================================================================
#single level inheritance

# class College:
#     def college_name(self):
#         print("Modern College")

# class Student(College):
#     def student_info(self):
#         print("Name: Prashant Jha")
#         print("Branch: Mechanical")
    
# obj = Student()
# obj.college_name()
# obj.student_info()

# #==============================================================
# #Multilevel Inheritance
# class College:
#     def college_name(self):
#         print("Modern College")

# class Student(College):
#     def student_info(self):
#         print("Name: Prashant Jha")
#         print("Branch: Mehanical")

# class Exam(Student):
#     def subject(self):
#         print("Subject1: Design Engineering")
#         print("Subject2: Math")
#         print("Subject3: C-Language")

# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()
#==========================================================
#Multiple inheritance
# class SubjMarks:
#     math = int(input("Enter paper marks of math: "))
#     DE = int(input("Enter paper marks of DE: "))
#     c = int(input("Enter paper marks of c: "))
#     english = int(input("Enter paper marks of english: "))

# class PracMarks:
#     cpract = int(input("Enter paper marks of c practical: "))

# class Result(SubjMarks,PracMarks):
#     print("if student pass in both = subject and practical paper then pass")
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
#             print("pass")
#         else:
#             print("fail")

# obj = Result()
# obj.total()
#==============================================================================
# class Rbi:
#     def home_loan(self):
#         print("Home Loan ROI = 8%")

#     def education_loan(self):
#         print("Education loan = 9%")
#         super().education_loan()
# class Sbi(Rbi):
#     def education_loan(self):
#         print("Education loan = 10%")
#         #super().education_loan()
# obj = Sbi()
# obj.education_loan()
#=================================================================================
# class Rbi:
#     def __init__(self):
#         print("Parent class Constructor")

# class Sbi(Rbi):
#     def __init__(self):
#         print("Child class constructor")

# obj = Sbi()