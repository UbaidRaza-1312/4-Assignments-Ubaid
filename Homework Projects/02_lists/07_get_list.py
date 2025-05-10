def main():
    lst = []

    val= input("Enter your value :")
    while val :
        lst.append(val)
        val = input("Enter your value :")

    print(f"Here's the list: {lst}")


if __name__ == '__main__':
    main()