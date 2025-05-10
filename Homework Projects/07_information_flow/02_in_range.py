def range(n , low , high):
    if n >= low and n <= high:
        return True
    
    return False

def main():
    n = int(input("Enter a number"))
    low = int(input("Enter a lower bound"))
    high = int(input("Enter the higher bound: "))
    
    if range(n, low, high):
        print(f"{n} is between {low} and {high}, inclusive.")
    else:
        print(f"{n} is NOT between {low} and {high}.")


if __name__ == '__main__':
    main()