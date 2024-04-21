from stop_words import get_stop_words
import json

stop_words = get_stop_words('en')

random_paragrapsh = open('random_paragraphs.txt', 'r').read()
print("length with stop words",len(random_paragrapsh))
for word in stop_words:
    random_paragrapsh = random_paragrapsh.replace(word, '')
    random_paragrapsh = random_paragrapsh.replace(word.title(), '')
    random_paragrapsh = random_paragrapsh.replace(word.upper(), '')
    random_paragrapsh = random_paragrapsh.replace(word.capitalize(), '')
print("length with stop words", len(random_paragrapsh))

word_count_dict = {}
for word in random_paragrapsh.split():
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

print(word_count_dict)