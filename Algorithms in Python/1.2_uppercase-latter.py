input_str_1 = "LucidProgramming"
input_str_2 = "lucidprogramming"


def uppercase_letter(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase leter"


print(uppercase_letter(input_str_1))
print(uppercase_letter(input_str_2))
