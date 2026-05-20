# Stack Implementation With Size Limit Using Python
import sys

class Stack:

    def __init__(self, size):

        self.myStack = []          # Creating Stack
        self.stackSize = size      # Maximum Size of Stack

    def push(self, value):

        if self.isFull():
            print("Stack Overflow")

        else:
            self.myStack.append(value)
            print(value, "Inserted Into Stack")

    def pop(self):

        if self.isEmpty():
            print("Stack Underflow")

        else:
            deleted = self.myStack.pop()
            print(deleted, "Deleted From Stack")

    def peek(self):

        if self.isEmpty():
            print("Stack is Empty")

        else:
            print("Top Element:", self.myStack[-1])

    def display(self):

        if self.isEmpty():
            print("Stack is Empty")

        else:
            print("\nStack Elements:")

            for i in reversed(self.myStack):
                print(i)

    def isEmpty(self):

        if len(self.myStack) == 0:
            return True

        else:
            return False

    def isFull(self):

        if len(self.myStack) == self.stackSize:
            return True

        else:
            return False

    def deleteStack(self):

        self.myStack = []
        print("Entire Stack Deleted Successfully")


size = int(input("Enter Stack Size: "))

obj = Stack(size)

print("\nStack Created Successfully")

while True:

    print("\n1. Push Operation")
    print("2. Pop Operation")
    print("3. Peek Operation")
    print("4. Display Stack")
    print("5. Check Stack Empty")
    print("6. Check Stack Full")
    print("7. Delete Entire Stack")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:

        value = int(input("Enter Value To Push: "))
        obj.push(value)

    elif choice == 2:

        obj.pop()

    elif choice == 3:

        obj.peek()

    elif choice == 4:

        obj.display()

    elif choice == 5:

        if obj.isEmpty():
            print("Stack is Empty")

        else:
            print("Stack is Not Empty")

    elif choice == 6:

        if obj.isFull():
            print("Stack is Full")

        else:
            print("Stack is Not Full")

    elif choice == 7:

        obj.deleteStack()

    elif choice == 8:

        print("Program Exited Successfully")
        sys.exit()

    else:
        print("Invalid Choice")