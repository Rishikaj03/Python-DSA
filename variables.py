#why python is called as dynamically typed language? -the datatype of a variable is determined automatically during program execution, and the programmer does not need to declare the variable type explicitly. It has both compiler and interpreter. Type checking happens at runtime
age =22
name="Rishika"
pi=3.14
result = True
print(type(age))
print(type(pi))
print(type(name))
print(type(result))

#checking address by using "ID" key
print(id(age))

#why all fundamentals datatype are imutable - because once created, their values cannot be changed. Immutability provides security, better memory optimization, hashing support, and reliable program behavior. the interpreter checks the datatype of variables during runtime and assigns the appropriate type automatically.
math = 50
che =50
phy=50
print(id(math))
print(id(che))
print(id(phy))