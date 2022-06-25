def get_total_transactions_in_month(trans_file, month):
    """function returns the total transacted amount (as a float) during the month and year as indicated by
the parameter month."""
    # Add zero padding to month, will add only if month is single digit
    month = month.split('/')
    if len(month[0]) == 1:              # if month is only 1 digit, e.g: 9, make it 09
        month[0] = month[0].zfill(2)
    month = '/'.join(month)             # join back the list of strings to single string

    final_amount = 0
    data = open(trans_file)         # open text file
    for each_line in data:
        each_line = each_line.rstrip()         # remove '\n' char--> to remove spacing between lines
        each_line = each_line.split('  ')       # convert text to a list, separated by double whitespace
        date = each_line[0]
        date_splitted = date.split('/')
        new_month = ""
        if int(date_splitted[0]) < 10:               # pad number with 0 infront to make it double digit
            new_month += str(date_splitted[0]).zfill(2)   # add 0 to make the number double digit(convert to str first)
        month_year_in_file = new_month+"/"+str(date_splitted[2])      # concatenate together
        money_spent = each_line[1]

        # Convert from string to float
        money_spent = float(money_spent.replace('$', ''))                    # To remove '$' char
        if month_year_in_file == month:
            final_amount += money_spent

    # Use python string formatting to show 1dp.   Convert string to a float
    final_amount_formatted = float("{:.1f}".format(final_amount))
    return final_amount_formatted


#print(get_total_transactions_in_month('my_transactions.txt', '04/2015'))
#print(get_total_transactions_in_month('my_transactions.txt', '9/2016'))
#print(get_total_transactions_in_month('my_transactions.txt', '01/2017'))
