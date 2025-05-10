def add(my_list , data):
    for i in range(3):
        my_list.append(data)

def main():
    message = input("Enter your message to copies")
    my_list = []
    print(f"List before: {my_list}" )
    add(my_list, message)
    print(f"List after: {my_list}")


if __name__ == "__main__":
    main()