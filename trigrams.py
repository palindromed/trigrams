import io


def list_words(word_list):
    dictionary = {}
    for n in range(0, len(word_list) - 2):
        key = word_list[n], word_list[n + 1]
        value = word_list[n + 2]
        if key in dictionary:
            dictionary[key].append(value)
        else:
            value = [value]
            dictionary.update({key: value})
    return dictionary


def remove_punctuation(list_of_words):
    return ''.join([c for c in list_of_words if c not in (':', ']', '[', '#', '*', '(', ')',  '-', '!', '?', ',', "'", '"', '.')])


def create_text(dictionary):
    pass


def main(path, word_count):
    infile = io.open(path, 'r')
    text_string = infile.read()
    text_string = remove_punctuation(text_string)
    print(text_string)
    list_of_strings = text_string.split()
    infile.close()
    dictionary = list_words(list_of_strings)
    create_text(dictionary)


if __name__ == '__main__':
    main('sherlock.txt', 200)
