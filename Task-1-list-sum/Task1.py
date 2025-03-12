user_input = input("Enter a list of integers separated by spaces: ")
numbers = list(map(int, user_input.split()))

total_sum = sum(numbers)
print(f"The sum of all the integers in the list is: {total_sum}")
