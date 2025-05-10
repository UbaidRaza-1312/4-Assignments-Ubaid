def main():
    side1: float = float(input("What is the length of side 1 ? "))
    side2: float = float(input("What is the length of side 2 ? "))
    side3: float = float(input("What is the length of side 3 ? "))

    perimeter : str =  str(side1 + side2 + side3) 
    style = f"\033[1m\033[3m{perimeter}\033[0m" 

    print(f"The perimeter of the triangle is {style}")


if __name__ == '__main__':
    main()