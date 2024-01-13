#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Use map and lambda to replace elements as needed
    new_list = list(map(lambda x: replace if x == search else x, my_list))

    return new_list

# Test case
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)  # Original list remains unchanged
