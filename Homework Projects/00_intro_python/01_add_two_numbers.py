def main():
    print ("This add two numbers ")
    
    num1 : str = input("Enter your first number:")
    num1 : int = int(num1)

    num2 : str = input("Enter your second number:")
    num2 :int = int(num2)

    total : str = num1 + num2
    print("The total is " + str(total) +  ".")

if __name__ == '__main__':
    main()