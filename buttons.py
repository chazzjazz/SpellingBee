# Start building a button and UI for Input

# from tkinter import *
#
# root = Tk()
#
#
# def myClick():
#     mylabel = Label(root, text="Look, I clicked a button!")
#     mylabel.pack()
#
#
# myButton = Button(root, text="Click Me!", command=myClick)
# myButton.pack()
#
# root.mainloop()
import pandas as pd
import numpy as np

def solvePuzzle(letters, center):
    words = pd.read_csv('word_list.csv')
    words = list(words['WORD_LIST'])
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    ban_list = alphabet
    letters = [char for char in letters]
    answers = []
    flag = 1

    # Clear non-numeric chars
    for word in words:
        if type(word) != str:
            words.remove(word)

    for letter in letters:
        ban_list.remove(letter)

    # Remove any strings containing chars in ban_list
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

    # Export word list and length to CSV
    # answers.to_csv('Spelling Bee Answers.csv', sep=",", index=False)
    print(answers)


solvePuzzle('louimnt', 'm')
