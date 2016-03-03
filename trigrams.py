import io
import random


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


def create_text(dictionary, wordcount=50):
    choice = random.choice(list(dictionary.keys()))
    output = [choice[0], choice[1]]
    output.append(dictionary[choice][0])
    # append each word to our output list
    # find the next word until sentence is finished
    while len(output) <= wordcount:
        output = make_sentence(dictionary, output)
    output = ' '.join(output)
    print(output)


def make_sentence(dictionary, output):
    search_word = output[-1]
    for n in range(random.randint(3, 4)):
        for key in dictionary:
            if key[0] == search_word:
                output.append(key[1])
                search_word = dictionary[key][0]
                output.append(search_word)
    return output


def main(path, word_count):
    infile = io.open(path, 'r')
    text_string = infile.read()
    clean_text_string = remove_punctuation(text_string)
    list_of_strings = clean_text_string.split()
    infile.close()
    dictionary = list_words(list_of_strings)
    create_text(dictionary)


if __name__ == '__main__':
    main('sherlock.txt', 50)
