
import spacy
import spacy_cleaner

from spacy import Language
from spacy_cleaner.processing import removers, replacers, mutators

from preprocessing.docx_loader import get_documents
from configs.settings import data_settings


def model_loader() -> Language:
    nlp = spacy.load('ru_core_news_sm')

    return nlp


def doc_parser(nlp: Language, data: str):

    new_data = nlp(data)

    for token in new_data:
        print(f"Токен: {token.text}, Лемма: {token.lemma_}, Позиция: {token.pos_}, "
              f"Тэг: {token.tag}, Зависимость: {token.dep_}, Стиль: {token.shape_}, Альфа: {token.is_alpha}, Стоп: {token.is_stop}")


if __name__ == '__main__':
    nlp = model_loader()
    documents = get_documents(data_settings.raw_data_dir)
    for doc in documents:
        doc_parser(nlp, doc)



