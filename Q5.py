def convert_to_list(num_list_str):
    """function returns a list that corresponds to num_list_str, i.e., it converts the string representation of the list
to the list itself."""
    final_list = []
    final_output_list = []
    num_list_str = num_list_str.strip('[]')     # remove leading [ and trailing ] from num_list_str
    input_as_list = num_list_str.split(',')     # split string separated by ',' to a list
    for each_string in input_as_list:
        list_of_chars = list(each_string)       # get a list of every char in each_string
        if '[' not in list_of_chars and ']' not in list_of_chars:    # if it's a number only
            final_list.append(int(each_string))
        elif '[' in list_of_chars:
            final_list.append('[')                  # '[' Will be before number
            for char in list_of_chars:
                if char != '[':                     # if char is a number
                    final_list.append(int(char))
        elif ']' in list_of_chars:
            for char in list_of_chars:
                if char != ']':
                    final_list.append(int(char))    # if char is a number
            final_list.append(']')                  # ']' will be after number

    for each_item in final_list:
        if type(each_item) == int:
            final_output_list.append(each_item)
        elif type(each_item) == str:                # if item is '[' or ']'

    return final_list
print(convert_to_list('[4,5,[6,7],[8,[9,10]],11]'))


# LEFTOVER ISSUE: How to combine a string repre of '[' or ']' with int number in the final list
# -------------> How to get 10 instead of 1, 0 being separated
# -------------> How to get two ]] instead of one ] in final list