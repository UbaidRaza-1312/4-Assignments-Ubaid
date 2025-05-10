def main():
    number : int = [1,2,3,4]

    for i in range(len(number)):
        elem = number[i]
        number[i] = elem * 2

    print(number)

main()