from array_1 import array_1


#Given target array for an array to equal to
arr_1 = ['1', '2', '3', '4', None]


def main():
    length = int(input("Enter the length of the array: "))
    arr = array_1(length)

    while True:

        choice = input(
            "What would you like to do?\n(1) Get the Logical size of the array\n(2) Get the length of the array\n(3) Get the item at a given index \n(4) Set the item at a given index\n(5) Print the array\n(6) Are the arrays equal? \n(7) exit: \n"
        )

        if choice == "1":
            print(arr.get_logical_size())
        elif choice == "2":
            print(len(arr))
        elif choice == "3":
            index = int(input("Enter the index: "))
            print(arr[index])
        elif choice == "4":
            index = int(input("Enter the index: "))
            item = input("Enter the item: ")
            arr[index] = item
        elif choice == "5":
            print(arr)
        elif choice == "6":
            print (arr)
            print (arr_1)
            if arr == arr_1:
                print("The arrays are equal")
            else:
                print("The arrays are not equal")
        elif choice == "7":
            break

    print("Goodbye!")


main()
