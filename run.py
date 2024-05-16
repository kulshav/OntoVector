from configs.settings import data_settings as dts
from preprocessing.docx_loader import get_documents
from preprocessing.tokenizer import tokenize_text

if __name__ == "__main__":
    text = get_documents()[0]
    sentence_tokens = tokenize_text(text=text, token_type=dts.sentence_tokenizer)
    print(sentence_tokens)
