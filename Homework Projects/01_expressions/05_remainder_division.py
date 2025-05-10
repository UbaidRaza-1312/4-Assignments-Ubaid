def main():
    num1 : int = int(input("Please enter an integer to be divided: "))
    num2 : int = int(input("Please enter an integer to  divided by : "))

    quotient :int = num1//num2
    remainder : int = num1 % num2

    style = f"\033[1m\033[3m{quotient}\033[0m"
    style1 = f"\033[1m\033[3m{remainder}\033[0m"

    print(f"The result of this division is {style} with a remainder of {style1}")


if __name__ == '__main__':
    main()