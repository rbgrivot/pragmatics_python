def print_times_table(times_value):
    count = 1
    while count < 15:
        result  = count * times_value
        print(count, 'times', times_value, 'equals', result )
        count = count + 1