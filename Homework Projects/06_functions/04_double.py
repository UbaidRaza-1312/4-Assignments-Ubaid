def double(num : int):
    return num * 2


def main():
    num= int(input("Enter a number : "))
    num2 = double(num)
    print(f"Double that is  {num2}")


if __name__ == '__main__':
    main()