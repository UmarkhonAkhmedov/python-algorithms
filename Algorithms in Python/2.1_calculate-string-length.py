input_str_1 = "LucidProgramming"


def calculate_string(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count


print(calculate_string(input_str_1))