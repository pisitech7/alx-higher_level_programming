#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the original list and replace elements as needed
    for item in my_list:
        # If the element matches 'search', replace it with 'replace'
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list

# Test case
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)  # Original list remains unchanged
