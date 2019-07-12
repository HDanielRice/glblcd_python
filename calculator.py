def calculate():
    opr = input("Enter the operation you want to perform: ")
    if opr in "ADD , add":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print (num1 + num2)
        
    elif opr in "MULTIPLY , multiply":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print (num1 * num2)
            
    elif opr in "DIVISION , division":
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print (num1 / num2)
                
    elif opr in "SUBTRACT , subtract":
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print (num1 - num2)
                
    else:
         print("invalid")
calculate()
        
                
                
    

    