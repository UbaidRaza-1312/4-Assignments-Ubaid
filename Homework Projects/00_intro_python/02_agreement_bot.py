def main():

    animal : str = input("What is your favorite animal ?")
    style = f"\033[1m\033[3m{animal}\033[0m"
    print(f"My favorite animal is also {style}")


if __name__ == '__main__':
    main()