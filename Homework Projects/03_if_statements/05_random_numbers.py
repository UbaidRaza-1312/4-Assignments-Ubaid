import random

def main():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    for num in random_numbers:
        print('\033[1;3m' + str(num) + '\033[0m', end=' ')
    print()

if __name__ == '__main__':
    main()
