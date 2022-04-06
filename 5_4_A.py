def interleave(*iterables):
    """
    Standard version
    :param iterables: Unknown amount of iterables
    :return: the list of separated members of the iterables
    """
    list_of_items = []
    for iterable in iterables:
        for item in iterable:
            list_of_items.append(item)
    return list_of_items


def interleave_generator(*iterables):
    """
    Generator version
    :param iterables: Unknown amount of iterables
    :return: the separated members of the lists
    """
    for iterable in iterables:
        for item in iterable:
            yield item


def main():
    # Standard version
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    # Generator version
    enerator_iterator = interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))
    for generator_iterator in enerator_iterator:
        print(generator_iterator)


if __name__ == "__main__":
    main()
