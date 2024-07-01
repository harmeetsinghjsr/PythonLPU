# Create an empty list
my_list = []

# Add elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Print the list
print("Original list:", my_list)

# Remove an element from the list
my_list.remove(2)

# Print the updated list
print("Updated list:", my_list)

# Accessing elements in a list
print("First element:", my_list[0])  # Output: 1
print("Last element:", my_list[-1])  # Output: 3

# Updating elements in a list
my_list[0] = 10
print("Updated list:", my_list)  # Output: [10, 2, 3]

# Finding the length of a list
print("Length of the list:", len(my_list))  # Output: 3

# Checking if an element exists in a list
print("Is 2 in the list?", 2 in my_list)  # Output: True
print("Is 5 in the list?", 5 in my_list)  # Output: False

# Sorting a list
my_list.sort()
print("Sorted list:", my_list)  # Output: [2, 3, 10]

# Reversing a list
my_list.reverse()
print("Reversed list:", my_list)  # Output: [10, 3, 2]

# Clearing a list
my_list.clear()
print("Cleared list:", my_list)  # Output: []
