#!/usr/bin/env python
# coding: utf-8

# # Лабораторная работа 1. "Предобработка текста"
# **Выполнила: Печкина Кристина, 932001 группа**

# In[1]:


#Токенизация
import nltk
from nltk.tokenize import word_tokenize

#Сегментация
import nltk
from nltk import sent_tokenize

#Лемматизация
import pymorphy2
m = pymorphy2.MorphAnalyzer()


# In[2]:


# Проверка на то, является ли слово сущ или прил
def is_noun_or_adj(word):
    parsed_word = m.parse(word)[0]
    return any(tag in parsed_word.tag for tag in ['NOUN', 'ADJF'])


# In[3]:


# Совпадают ли слова по роду, числу и падежу
def match_pairs(word1, word2):
    parsed_word1 = m.parse(word1)[0]
    parsed_word2 = m.parse(word2)[0]

    if ('NOUN' in parsed_word1.tag or 'ADJF' in parsed_word1.tag) and ('NOUN' in parsed_word2.tag or 'ADJF' in parsed_word2.tag):
        return parsed_word1.tag.gender == parsed_word2.tag.gender and parsed_word1.tag.number == parsed_word2.tag.number and parsed_word1.tag.case == parsed_word2.tag.case
    return False


# In[6]:


# Прочитаем текст из файла
with open('Doc.txt', 'r', encoding='utf-8') as file:
    text = file.read()

    print("Текст:")
    print(text)

# Найдем пары
    sentences = sent_tokenize(text)

    print("\nПары слов, удовлетворяющие условиям:")

    for sentence in sentences:
# Токенизируем предложение на слова
        words = word_tokenize(sentence)

        # Проходим по словам и ищем пары, удовлетворяюще условиям
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if is_noun_or_adj(word1) and is_noun_or_adj(word2) and match_pairs(word1, word2):
              W1 = m.parse(word1)[0].normal_form
              W2 = m.parse(word2)[0].normal_form
              print(" ",W1, W2)


# In[ ]:




