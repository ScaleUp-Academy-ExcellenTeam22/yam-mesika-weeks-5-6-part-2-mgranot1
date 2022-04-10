def interleave(*iterables):
    """
    Standard version
    :param iterables: Unknown amount of iterables
    :return: List that includes the members of the iterables intertwined
    """
    return [j[i] for i in range(len(iterables[0])) for j in [it for it in iterables]]


def interleave_generator(*iterables):
    """
    Generator version
    :param iterables: Unknown amount of iterables
    :return: The members of the iterables intertwined
    """
    for i in range(len(iterables[0])):
        for j in [it for it in iterables]:
            yield j[i]
         


def main():
    # Standard version
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    # Generator version
    enerator_iterator = interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))
    for generator_iterator in enerator_iterator:
        print(generator_iterator)


if __name__ == "__main__":
    main()
