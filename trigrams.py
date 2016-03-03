import io
import random
import sys


def list_words(word_list):
    dictionary = {}
    for n in range(0, len(word_list) - 2):
        key = tuple(word_list[n:n + 2])
        value = word_list[n + 2]
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]
    return dictionary


def remove_punctuation(list_of_words):
    return ''.join([c for c in list_of_words if c not in (':', ']',
    '[', '#', '*', '(', ')', '-', '!', '?', ',', "'", '"', '.')])


def create_text(dictionary, wordcount=50):
    choice = random.choice(list(dictionary.keys()))
    output = [choice[0], choice[1]]
    output.append(dictionary[choice][0])

    while len(output) < wordcount + 1:
        output = make_sentence(dictionary, output)
        print('Sentence created')
    output = ' '.join(output)
    print(output)


def make_sentence(dictionary, output):
    search_word = output[-1]
    for n in range(random.randint(2, 4)):
        for key in dictionary:
            if key[0] == search_word:
                output.append(key[1])
                search_word = dictionary[key][0]
                output.append(search_word)
    return output


def main(path, word_count):
    infile = io.open(path, 'r')
    text_string = infile.read()
    infile.close()
    clean_text_string = remove_punctuation(text_string)
    list_of_strings = clean_text_string.split()
    dictionary = list_words(list_of_strings)
    create_text(dictionary)


if __name__ == '__main__':
    #print(str(sys.argv))
    main(sys.argv[1], sys.argv[2])
