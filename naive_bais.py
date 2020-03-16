# -- coding: utf-8 --
"""
Created on Sun OCT 20 16:30 2019

@author: DHRUVI RAJPUT
"""

import os
import operator

location = '20_newsgroups'
total_txt_files = []

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''
def remove_punctuation(string):
    global punctuations
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, " ")
    return string


def test(line):
    list_of_words = remove_punctuation(line).split()
    for wrd in list_of_words:
        # count_word = count_word + 1
        if wrd not in word_dict:
            word_dict[wrd] = 1
        else:
            word_dict[wrd] = word_dict[wrd] + 1
    return word_dict

def test2(w):
    global final_prob, number , folder_words_count,word_dict
    if word_dict[w] == 0:
        final_prob[(w, i)] = (0.01 / folder_words_count[i]) * number
    else:
        final_prob[(w, i)] = (word_dict[w] / folder_words_count[i]) * number

def test3(i,j):
    with open(os.path.join(os.path.join(location, i), j), 'r') as ind:
        words_set = set()
        for lines in ind:
            words_set.update(remove_punctuation(lines).split())
    return words_set


def test4(k):
    probability = prob[k]
    for w in words_set:
        if (w, k) not in final_prob:
            probability = (probability * 0.01 * number / folder_words_count[k])
        else:
            probability = (probability * final_prob[(w, k)]) * 100
    probabilities[k] = probability
    return probabilities




cnt = 0
X_dict = {}
Y_dict = {}
folder_list = []
classList = []
for className in (os.listdir(location)):
    classList.append(className)
    for txt_file in os.listdir(os.path.join(location, className)):
        folder_list.append(txt_file)
        cnt = cnt + 1
    X_dict[className] = folder_list[0:(len(folder_list)) // 2]
    lower_limit = len(folder_list)//2
    Y_dict[className] = folder_list[len(folder_list) // 2:]
    total_txt_files.append(len(folder_list))
    folder_list = []



folder_words_count= {}
number  = 500
prob = {}
for i in range(0, len(total_txt_files)):
    prob[(classList[i])] = total_txt_files[i] / cnt


count_word = 0

word_dict = {}
final_prob = {}
for i in X_dict:
    for j in X_dict[i]:
        count = 0
        with open(os.path.join(os.path.join(location, i), j), 'r') as ind:
            for line in ind:
                word_dict = test(line)
    folder_words_count[i] = sum(word_dict.values())
    for w in (word_dict.keys()):
        test2(w)
    word_dict = {}




probabilities = {}
word_counts = {}
a = 0
count = 0
for i in Y_dict:
    for j in Y_dict[i]:
        count = count + 1
        words_set = test3(i,j)
        for k in X_dict:
            probabilities=test4(k)
        if i == max(probabilities.items(), key=operator.itemgetter(1))[0]:
            a = a + 1

print("Final Accuracy = ",a/count)