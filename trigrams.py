import io
import random
import sys


def list_words(word_list):
    dictionary = {}
    for n in range(0, len(word_list) - 2):
        key = tuple(word_list[n:n + 2])
        value = word_list[n + 2]
        dictionary.setdefault(key, []).append(value)
    return dictionary


def remove_punctuation(list_of_words):
    list_of_words = list_of_words.lower()
    return ''.join([c for c in list_of_words if c not in (':', ']',
    '[', '#', '*', '(', ')', '-', '!', '?', ',', "'", '"', '.')])


def create_text(dictionary, wordcount):
    choice = random.choice(list(dictionary.keys()))
    output = [choice[0], choice[1]]
    output.append(dictionary[choice][0])

    while len(output) < wordcount:
        output = make_sentence(dictionary, output)
    output = output[:wordcount]
    return ' '.join(output)


def make_sentence(dictionary, output):
    search_word = output[-1]
    for n in range(random.randint(1, 3)):
        for key in dictionary:
            if key[0] == search_word:
                output.append(key[1])
                search_word = dictionary[key][0]
                output.append(search_word)
    return output


def write_to_file(output):
    outfile = io.open('output.txt', 'w')
    outfile.write(output)
    outfile.close()


def main(path, word_count):
    infile = io.open(path, encoding='utf-8')
    text_string = infile.read()
    infile.close()
    # execute funtions
    clean_text_string = remove_punctuation(text_string)
    list_of_strings = clean_text_string.split()
    dictionary = list_words(list_of_strings)
    output = create_text(dictionary, word_count)
    write_to_file(output)

if __name__ == '__main__':
    word_count = int(sys.argv[2])
    main(sys.argv[1], word_count)
