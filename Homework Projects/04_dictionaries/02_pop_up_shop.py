def main():
    furits = {'apple' : 20 , 'pineapple' : 50 , 'mango' : 30 , 'kiwi' : 1.9 , 'orange' : 40 , }

    total_cost = 0
    for furit_name in furits:
        price = furits[furit_name]
        amount = int(input(f"How many ( {furit_name} ) do you buy ? :"))
        total_cost += (price *amount)

        style = f"\033[1m\033[3m{total_cost}\033[0m"

    print(f"Your total is $ {style}")


if __name__ == '__main__':
    main()