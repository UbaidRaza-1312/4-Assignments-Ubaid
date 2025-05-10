def main():
    num : float = float(input("Type a number to see its square : "))
    square :str = str(num** 2)
    style = f"\033[1m\033[3m{square}\033[0m" 


    print (f"{str(num)} squared is {style}")






if __name__ == '__main__':
    main()