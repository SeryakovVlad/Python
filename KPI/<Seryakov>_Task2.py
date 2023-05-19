#'Introduction to programming':Task 2
#Seriakov Vlad, FB-21, V-10(22)
import re
sentence = re.findall(r'\w+', input('Напишіть речення: '))
count_of_letters = 1
largest_word_count = max(sentence,key=len)
for j in range(1,len(largest_word_count)+1):
    count_of_words = 0
    words = []
    for i in sentence:
        if count_of_letters == len(i):
            count_of_words += 1
            words.append(i)
    if count_of_words == 0:
        print(f'Слів з {count_of_letters} букв немає')
    if count_of_words != 0:
        print(f'Слова з {count_of_letters} букв {words} і їх {len(words)}')
    count_of_letters += 1