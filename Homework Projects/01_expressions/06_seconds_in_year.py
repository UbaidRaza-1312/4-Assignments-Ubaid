days_in_year = 365
hours_in_day = 24
min_in_hour = 60
second_in_hour = 60

def main(): 
    total_seconds = days_in_year*hours_in_day*min_in_hour*second_in_hour

    print(f"There are {total_seconds} seconds in a year!")
if __name__ == '__main__':
    main()