import pandas as pd
import numpy as np

words = pd.read_csv('word_list.csv')
words = list(words['WORD_LIST'])

# Define Letters and Center
letters = ('l', 'o', 'u', 'm', 'n', 'i', 't')
center = 't'

# Specify non-selected letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
ban_list = alphabet

for letter in letters:
    ban_list.remove(letter)

# Remove non string objects from list
for word in words:
    if type(word) != str:
        words.remove(word)


# Remove any strings containing chars in ban_list
answers = []
flag = 1

for word in words:
    for letter in ban_list:
        if letter not in word and center in word:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        answers.append(word)

# Convert List into PD Dataframe and Find Length, Distinct Length
answers = pd.DataFrame(answers, columns=['Words'])
answers['Length'] = answers['Words'].str.len()
answers['Distinct Length'] = answers['Words'].apply(set).apply(len)


# Flag Pangrams
answers['Pangram'] = np.where(answers['Distinct Length'] == 7, True, False)
answers = answers.sort_values(by=['Length'], ascending=False)

# Export answers to CSV
answers.to_csv('Spelling Bee Answers.csv', sep=",", index=False)

