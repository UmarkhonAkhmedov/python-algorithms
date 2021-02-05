input_str_1 = "abc de"
input_str_2 = "lucidprogramming"
vowels = "aeiou"


def iterative(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str.isalpha():
            count += 1
    return count


print(iterative(input_str_1))
print(iterative(input_str_2))