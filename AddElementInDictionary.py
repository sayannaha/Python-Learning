#Iterate a given list and check if a given element exists as a key’s value in a dictionary.
#If not, delete it from the list
roll_number = [100, 1, 101, 2, 102, 3, 4, 103]
sample_dict = {'Jhon': 100, 'Emma': 101, 'Kelly': 102, 'Jason': 103}
print("List:", roll_number)
print("Dictionary:", sample_dict)
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("after removing unwanted elements from list:", roll_number)