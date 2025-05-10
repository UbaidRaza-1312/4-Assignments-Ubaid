SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb


def main():
    adjective : str = input("Please type an adjective and press enter. ")
    noun : str = input("Please type an noun and press enter. ")
    verb : str = input("Please type an verb and press enter. ")

    style1 = f"\033[1m\033[3m{adjective}\033[0m"
    style2 = f"\033[1m\033[3m{noun}\033[0m"
    style3 = f"\033[1m\033[3m{verb}\033[0m"

    print(f"{SENTENCE_START} {style1} {style2} {style3} !")

if __name__ == '__main__':
    main()