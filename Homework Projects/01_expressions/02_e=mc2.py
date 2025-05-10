c : int = 299792458

def main():
    mass: float = float(input("Enter kilos of mass : "))
    energy: float = mass * (c ** 2)

    style = f"\033[1m\033[3m{energy}\033[0m"
    
    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(c) + " m/s")
    
    print(str(style) + " joules of energy!")

if __name__ == '__main__':
    main()



