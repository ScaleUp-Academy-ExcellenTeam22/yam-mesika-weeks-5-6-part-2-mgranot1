

def possible_divisions(my_number):
    """
    :param my_number: a number for checking if it able to be perfect dish
    :return: a list of all possible divisions of dish portions
    """
    list_possible_divisions=[]
    for part in range(1,my_number):
        if my_number % part == 0:
            list_possible_divisions.append(part)
    return list_possible_divisions


def perfect_dish():
    """
    :return: Perfectly divisible numbers
    """
    my_number = 6 # The smallest size that sustains the division
    while True: # A loop that always works
        list_possible_divisions = possible_divisions(my_number)
        if sum(list_possible_divisions) == my_number:
            print(list_possible_divisions)
            yield my_number
        my_number += 1


def main():
    generator_iterator = perfect_dish()
    for my_number in range(4):
        print(next(generator_iterator))


if __name__ == "__main__":
    main()