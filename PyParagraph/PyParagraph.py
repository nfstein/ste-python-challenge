import os
import csv
import string

filepath = os.path.join('raw_data','sample.txt')

sentence_count = 0
word_count = 0
letter_count = 0
word_dict = {}
with open(filepath, 'r') as textfile:
    text = csv.reader(textfile, delimiter = " ")

    for passage in text:
        for word in passage:
            if '.' in word or '?' in word or '!' in word:
                sentence_count += 1
            
            letters = ''.join(i for i in word if i.isalpha())
            letter_count += len(letters)
            if len(letters) > 0:
                word_count += 1
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1

unique_words_total_length = 0
unique_word_count = len(word_dict)
for word in word_dict:
    unique_words_total_length += len(word)

unique_words_average_length = unique_words_total_length / unique_word_count

print("-----------------------------------")
print(f'Approximate Sentence Count - {sentence_count}')
print(f'Approximate Word Count - {word_count}')
print(f'Unique Word Count {unique_word_count}')
print(f'Approximate Letter Count - {letter_count}')
print(f'Average Word Length - {letter_count / word_count}')
print(f'Average Length of Unique Words - {unique_words_average_length}')
print(f'Average Sentence Length - {word_count/sentence_count}')