# #queue with size limit
# import sys
# class Queue:
#     def __init__(self, size):
#         self.myQueue = []      #create Queue
#         self.queueSize = size  #stackk size defined

#     def isFull(self):
#         if len(self.myQueue) == size:
#             return True
#         else:
#             return False
    
#     def enQueue(self, value):
#         if self.isFull():
#             print("Queue is full.")
#         else:
#             self.myQueue.append(value)
    
#     def display(self):
#         print(self.myQueue)

#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False

#     def deQueue(self, value):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             self.myQueue.pop(0)

#     def peek(self):
    
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Top Element:", self.myQueue[-1])

#     def deleteQueue(self):
#         self.myQueue = None

# size = int(input("Enter the size of the Queue: ") )
# obj = Queue(size)
# print("Queue has created ")
# while True:
#     print("1. Enqueue Operation: ")
#     print("2. Display Queue: ")
#     print("3. Dequeue Operation: ")
#     print("4. Peek Operation: ")
#     print("5. Delete Queue: ")
#     print("6. Exit ")

#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         value = int(input("Enter the element to add in queue: "))
#         obj.enQueue(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.deQueue()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deleteQueue()
#     elif choice == 6:
#         print("Program Exited Successfully")
#         sys.exit()
#     else:
#         print("INVALID OPTION")

#----------------------------------------------------------------------------------------------------------------