def count_names_with_space(name_list):
    """function counts how many names in name_list contain at least a space and returns the count"""
    count = 0
    # To check for each char in each string, use list()
    for each_name in name_list:
        list_of_char = list(each_name)    # convert string to list of individual chars
        if ' ' in list_of_char:           # if the list has space, add 1 to count variable
            count += 1

    return count
#print(count_names_with_space(['George W. Bush', 'George Washington', 'Bill',
#'Gates', 'Bill Gates']))
#print(count_names_with_space(['Mark', 'George', 'William']))
print(count_names_with_space([]))