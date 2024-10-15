

def cancellation(input_list, stop_word):
    output_list = []
    for item in input_list:
        if item == stop_word:
            break
        output_list.append(item)
    return output_list

    pass

def copy_all_but_skip_word(input_list, skip_word):
    output_list = []
    for item in input_list:
        if item != skip_word:
            output_list.append(item)
    return output_list

    pass

def my_average(input_list):
    total = 0
    for num in input_list:
        total += num
    return total / len(input_list)

    pass

