#ACCESS other files in same dir
import words

print(words.NOUNS)

# Iterate over the array
for element in words.NOUNS:
    print(element)
    for letter in element:
        print(letter)


print("Better " + words.NOUNS[20])

better = "Better"
print(better.join(words.NOUNS[20]))
print(words.ADJECTIVES[5] + words.NOUNS[5])
print(words.ADJECTIVES[5] + " " + words.NOUNS[5])
print(words.ADJECTIVES[5],words.NOUNS[5])

msg = words.ADJECTIVES[5] + " " + words.NOUNS[5]
sub_msg = msg[3:5]
print(sub_msg)

sub_NOUNS = words.NOUNS[1:6]
print(sub_NOUNS)

path = 'data/books/the_sign_of_the_four.txt'

def find_potentaial_names(path_to_file , titles=["Mr.", "Mrs.", "Ms.", "Dr."]):
    with open(path_to_file, encoding="UTF-8") as fp:
        all_text = fp.read()

    all_text = all_text.replace('\n', ' ')
    words = all_text.split()
    names = []

    for idx, word in enumerate(words):
        if (word[0].isupper) and (words[idx - 1] in titles):
            names.append(word)
        elif word[0] == word[0].upper():
            pass
        else:
            pass
    return set(names)

import glob

books_path = glob.glob("data/books/*");

print(books_path)

#def top_ten_for_books(books_path):


def count_words(path_to_file):
    word_freq = {}
    with open(path_to_file, encoding="UTF-8") as fp:
        all_text = fp.read()
    
    all_text = all_text.replace('\n', ' ')
    words = all_text.split()

    for word in words:
        word_freq.setdefault(word, 0)
        word_freq[word] += 1

    return word_freq

def find_top_ten(dictonary):
    topTen = {}

    for word in dictonary:
        pass

if __name__ == '__main__':
    #print(find_potentaial_names(path, titles=["Mr."]))
    print(count_words(path))