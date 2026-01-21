def main():
    user_input = input("Enter a list of numbers (SEPARATED WITH A SINGLE SPACE): ")
    user_list = list(map(int, user_input.split()))

    even = [num for num in user_list if num % 2 == 0]

    if even:
        print("The list is: ", even)
    else:
        print(None)

main()
