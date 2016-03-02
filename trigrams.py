import io

dictionary = {}


def list_words(word_list):
    for n in range(0, len(word_list) - 2):
        key = word_list[n], word_list[n + 1]
        value = word_list[n + 2]
        if key in dictionary:
            dictionary[key].append(value)
        else:
            value = [value]
            dictionary.update({key: value})


def main(path, word_count):
    infile = io.open(path, 'r')
    list_of_strings = infile.read().split()
    infile.close()
    list_words(list_of_strings)


if __name__ == '__main__':
    main('sherlock.txt', 200)
