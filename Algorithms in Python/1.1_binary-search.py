data = [2, 5, 7, 8, 9, 15, 20]
target = 12


def binary_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


print(binary_search(data, target))
