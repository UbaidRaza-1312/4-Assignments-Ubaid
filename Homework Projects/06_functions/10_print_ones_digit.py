def print_one_digit(num : int):
    print("The one digit  is " , num % 10)


def main():
    num = int(input(" Enter anumber :"))
    print_one_digit(num)    


if __name__ == '__main__':
    main()
