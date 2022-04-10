
def perfect_dish():
    """
    Perfect_num is number that when we sum up all its complete divisions we will get it ourselves
    Perfect_divider divides the number without a remainder
    :return: Perfect numbers
    """
    perfect_num = 6  # The smallest size that sustains the division
    while True:
        list_perfect_divider = [divider for divider in range(1, perfect_num) if perfect_num % divider == 0]
        if sum(list_perfect_divider) == perfect_num:
            yield perfect_num
        perfect_num += 1


def main():
    generator_iterator = perfect_dish()
    for my_number in range(4):
        print(next(generator_iterator))


if __name__ == "__main__":
    main()
