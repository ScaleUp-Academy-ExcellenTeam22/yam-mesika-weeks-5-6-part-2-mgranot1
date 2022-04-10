import statistics
from timeit import default_timer as timer
#filename = r"C:\Networks\5-6\words.txt"


def average_runtime(words_for_search):
    """
    :param words_for_search: List or Set of words
    :return: Average time between 1000 word 'zwitterion' searches
    """
    list_of_search_times = []
    for search in range(1000):
        start_search = timer()
        'zwitterion' in words_for_search
        end_search = timer()
        list_of_search_times.append(end_search - start_search)
    return statistics.mean(list_of_search_times)


def search_times():
    """
    Gets a path for a file with words.
    Prints the average time to search for a word in a file for a list and for a set.
    """
    file_path = input("Enter path of words.txt: ")
    # Reading all the words from the file
    with open(file_path) as file:
        words_list = file.readlines()
    # Average time of search within a list
    words_set = set(words_list)
    # Average time of search within a set
    average_runtime_list = average_runtime(words_list)
    average_runtime_set = average_runtime(words_set)
    print("Average time to search for a word in a list: ", average_runtime_list)
    print("Average time to search for a word in a set: ", average_runtime_set)

    

def main():
    search_times()

    
if __name__ == "__main__":
    main()
