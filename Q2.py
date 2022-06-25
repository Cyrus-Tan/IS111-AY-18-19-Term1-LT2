def get_prices_in_range(price_list, low, high):
    """function returns a list that contains all the prices between low (inclusive) and high (inclusive) from
price_list."""
    final_list = []
    # Iterate through each item in list, and compare with low and high
    for number in price_list:
        if number > low or number == low:
            if number < high or number == high:
                final_list.append(number)
    return final_list
#print(get_prices_in_range([249.99, 24.49, 10.0, 100.0], 0.0, 30.0))
#print(get_prices_in_range([15.0, 10.9, 5.0], 5.0, 20.0))
#print(get_prices_in_range([108.9, 354.8], 0.0, 100.0))
#print(get_prices_in_range([], 0.0, 100.0))