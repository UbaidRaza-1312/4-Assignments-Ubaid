def get_first_element(lst):

    print(lst[0])

def get_1st():
    lst = []
    elem : str = input ("Please enter an element of the list or press enter to stop. ")
    while elem!= "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_1st()
    get_first_element (lst)


if __name__ == '__main__':
    main()