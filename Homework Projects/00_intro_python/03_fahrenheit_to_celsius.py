def main():
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit : "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    style = f"\033[1m\033[3m{degrees_celsius}\033[0m"

    print(f"Temperature : {degrees_fahrenheit}F = {style}C")

if __name__ == '__main__':
    main()