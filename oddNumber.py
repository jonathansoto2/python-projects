''' Jonathan Soto MWF 1/14/19 CSC240
User will enter an odd number (1-49) and will return
a series of Asterisks* that increment to the odd number
entered
The program will terminate when the user inputs (99)
The user will reenter a number if it is not odd and/or in range
'''

def oddNumber():

    starter = 0
    while starter == 0:
    #userInput = input("Enter an odd number between 1 - 49:")
        #check to see if its an odd number
        userInput = input("please enter an odd number between 1 - 49: ")
        userInput = int(userInput)
        thingLine = "*"
    

    #if the input is odd do this 
    
        if userInput % 2 == 1 and userInput > 0 and  userInput < 50:
            n = 0
            for i in range(1, userInput + 1): 
                # loop to print spaces 
                for j in range (1, (userInput - i) + 1): 
                    print(end = " ") 
                
                # loop to print star 
                while n != (2 * i - 1): 
                    print("*", end = "") 
                    n = n + 1
                n = 0
                
                # line break 
                print()  
        
            k = 1
            n = 1
            for i in range(1, userInput): 
                # loop to print spaces 
                for j in range (1, k + 1): 
                    print(end = " ") 
                k = k + 1
                
                # loop to print star 
                while n <= (2 * (userInput - i) - 1): 
                    print("*", end = "") 
                    n = n + 1
                n = 1
                print() 

        elif userInput == 99:
            starter = 1


        #if the input is even
        else:
            print("Try another number")

if __name__ == "__main__":
    oddNumber()
    print("thank you !")