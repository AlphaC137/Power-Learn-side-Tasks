set1 = set(map(int, input("Enter the first set of integers (separated by spaces): ").split()))
set2 = set(map(int, input("Enter the second set of integers (separated by spaces): ").split()))

common_elements = set1 & set2  # This is the intersection of set1 and set2

# Printing the common elements
print(f"Common elements between the two sets: {common_elements}")
