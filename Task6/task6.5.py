user_input = input("Enter a list of numbers (SEPARATED WITH A SINGLE SPACE): ")
user_list = list(map(int, user_input.split()))
even = [num for num in user_list if num % 2 == 0]
def main():
    original = "The original List: ", user_list
    modified = "The modified List: ", even
    return original, modified
func_print = main()
print(func_print)