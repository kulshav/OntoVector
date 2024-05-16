import os

from langchain_community.document_loaders import Docx2txtLoader


def get_documents(folder_path):
    text_list = []

    files = [ext.lower() for ext in os.listdir(folder_path)]

    for file in files:
        if '.docx' in file or '.doc' in file:
            full_path = os.path.join(folder_path, file)
            docx_loader = Docx2txtLoader(full_path)
            docx_document = docx_loader.load()

            for doc in docx_document:
                text = doc.page_content
                text_list.append(text)

    return text_list

