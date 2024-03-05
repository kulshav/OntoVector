import os

import spacy


nlp = spacy.load("ru_core_news_sm")  # ru_core_news_lg -> larger model


def tokenize_text(txt_file):
    # Открытие файла для чтения
    with open(txt_file, 'r', encoding='utf-8') as f:
        text = f.read()

    doc = nlp(text)

    for token in doc:
        print(token.text)


txt_file = os.path.join(os.getcwd(), 'data/data_1.txt')
print(txt_file)
tokenize_text(txt_file)
