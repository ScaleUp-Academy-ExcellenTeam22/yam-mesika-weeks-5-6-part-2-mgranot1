line1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
line2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
line3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
lines = [line1, line2, line3]
#  file_path = r"C:\Networks\5-6\states.txt"

def find_special_state(states):
    """
    :param states: List of countries in the United States
    :return: country written on one line on the keyboard
    """
    for state in states:
        set_letters_of_state = set()
        for letter in state:
            set_letters_of_state.add(letter)
            set_letters_of_state.discard('\n')
        # Check if a row on the keyboard contains all the letters of the country
        for line in lines:
            if line.issuperset(set_letters_of_state):
                return state


def main():
    file_path = input("Enter path of states.txt: ")
    # Reading all the states from the file
    with open(file_path) as file:
        states = file.readlines()
    # Finding the country written on one line on the keyboard
    special_state = find_special_state(states)
    print(special_state)


if __name__ == "__main__":
    main()
