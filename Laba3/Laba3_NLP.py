# -*- coding: utf-8 -*-
"""Laba3_NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n8OkjmtzGoR5hUcIimUIyOwx-rB7dWFY

# Лабораторная работа 3. "Анализ на основе RNN"
**Выполнила: Печкина Кристина, 932001 группа**
"""

!pip install rnnmorph

import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import re

# Импортируем RNNMorphPredictor и создаем экземпляр:
from rnnmorph.predictor import RNNMorphPredictor
predictor = RNNMorphPredictor(language='ru')

def parse_morph_tags(tag_str):
    if tag_str == '_':
        return {'Case': 'Null', 'Gender': 'Null', 'Number': 'Null'}

    tag_dict = {key: value for key, value in (part.split('=') for part in tag_str.split('|'))}

    return tag_dict

# Подключение к Google Диску
from google.colab import drive
drive.mount('/content/drive')
txt = open("/content/drive/MyDrive/Doc.txt")

# Прочитаем текст из файла
text = txt.read()
text = re.sub(r'[^\w\s]', '', text)

# Разбиваем текст на предложения
sentences = re.split(r'(?<=[.!?])\s+', text)

lem_and_tag = []

for sentence in sentences:
     words = word_tokenize(sentence)
     analyzed_words = predictor.predict(words)
     lem_and_tag.extend([(word.pos, word.normal_form, word.tag) for word in analyzed_words])

# Найдем пары соседних слов, удовлетворяющие условиям (совпадают по роду, числу и падежу):
coincidence = []

for i in range(len(lem_and_tag) - 1):
    (pos1, word1, tag1), (pos2, word2, tag2) = lem_and_tag[i], lem_and_tag[i + 1]

    tag1_dict, tag2_dict = parse_morph_tags(tag1), parse_morph_tags(tag2)

    if 'NOUN' in (pos1, pos2) and 'ADJ' in (pos1, pos2):
      if tag1_dict['Case']  == tag2_dict['Case']  and tag1_dict['Number'] == tag2_dict['Number'] and tag1_dict['Gender'] == tag2_dict['Gender']:
        coincidence.append((word1, word2))

print("Текст:")
print(text)

# Выводим найденные пары:
print("\nПары слов, удовлетворяющие условиям:")

for couple in coincidence:
    print(couple[0], couple[1])