def num_sum(nums):
    return sum(nums)

def main():
    user_input = input("Enter a list of numbers(SEPARATE THEM WITH A SINGLE SPACE): ")
    user_list = list(map(int, user_input.split()))
    result = num_sum(user_list)
    print("The sum is: ", result)

main()
