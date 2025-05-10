def multiple(message : str , repeat : int):
    for i in range(repeat):
        print(message)


def main():
    message = input("Enter a message :")
    repeat =int(input("Enter a number of times to repeat your message:"))
    multiple(message , repeat)



if __name__ == '__main__':
    main()


