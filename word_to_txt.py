import os
import docx2txt


def convert_docx_to_txt(docx_file):
    file_name, file_ext = os.path.splitext(docx_file)

    txt_file = file_name + ".txt"

    text = docx2txt.process(docx_file)

    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(text)


data_folder = os.path.join(os.getcwd(), 'data')


for filename in os.listdir(data_folder):
    if filename.endswith(".docx"):
        docx_file_path = os.path.join(data_folder, filename)
        convert_docx_to_txt(docx_file_path)

