import random

def main():
    secret_num = random.randint(1,99)
    print("I am thinking of a number between 1 and 99...")

    guess = int(input("Enter a guess : "))

    while guess != secret_num:
        if guess < secret_num:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        print()
        guess = int(input("Enter a guess : "))

    print(f"Congrats! The number was : {str(secret_num)}")



if __name__ == '__main__':
    main()
