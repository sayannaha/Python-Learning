#Count the occurrence of each element from a list
sample_list = [1, 2, 8, 1, 3, 2, 3, 2, 4]
print("Original list ", sample_list)
count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("Printing count of each item  ", count_dict)