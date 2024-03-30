

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def read_dictionary_file(file_path):
    words_with_frequencies = []

    with open(file_path, 'r') as file:
        for line in file:
            frequency, word = line.strip().split()
            words_with_frequencies.append((word, int(frequency)))
    return words_with_frequencies


if __name__ == '__main__':

    words_with_frequencies = read_dictionary_file('./data/dictionary.txt')
    print(words_with_frequencies)

    # Output:
    # [('apple', 10), ('banana', 20), ('cherry', 30), ('date', 40), ('elderberry', 50)]





