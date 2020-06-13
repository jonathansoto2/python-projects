'''
Jonathan Soto

The program will provide the user with the options to 
push, pop, display and exit. 
According to the option entered, 
access its respective function using a switch statement.

In the function push(), firstly check if the stack is full. if full output "stack full"
 take the number to be inserted as input and store it in the variable num. 
 Copy the number to the array stk[] and increment the variable top by 1.

 In the function pop(), firstly check if the stack is empty. 
 If it is, then print the output as “Stack is Empty”. 

 Otherwise print the top most element of the array stk[] 
 and decrement the variable top by 1.

 In the function display(), using for loop print all the elements of the array.


'''

class Stack:

    def __init__(self, max):
        self.max = max
        self.items = []

    def isEmpty(self):
        return self.items == []
        

    def push(self , x):
        if len(self.items) > self.max:
            raise Exception('The stack is full. Pop items.')
        self.items.append(x)


    def pop(self):
        if len(self.items) == self.isEmpty():
            raise Exception('The stack is Empty, please add items to the stack.')
        elif len(self.items) > self.max:
            raise Exception('The stack is full.')
        

        return self.items.pop()

    def display(self):
        return self.items


print("1 - push")
print("2 - pop")
print("3 - display")
print("4 - exit")
s = Stack(10)

def play():

#Loops so user can push or pop from the stack 
    while True:
        try:
            user_choice = int(input("Enter 1, 2, 3, or 4: "))
        except ValueError:
            print("enter a valid choice")
            continue
        
        if user_choice == 1:
            item = input("What do you want to add to the Stack?: ")
            s.push(item)
        elif user_choice == 2:
            s.pop()
        elif user_choice == 3:
            print(s.display())
        elif user_choice == 4:
            print("Thanks for playing :p")
            return False

play()
