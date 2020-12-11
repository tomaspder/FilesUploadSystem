'''Modulo para el manejo de archivos, lectura y formato'''
import os

def handler():
    file_content = {}
    file_headers = []

    for filename in os.listdir('uploads'):
        if filename != 'pdf_files':
            with open(os.path.join('uploads', filename), 'r') as fh:
                header = fh.readline().replace("\n","").split(';')
                file_headers.append(header)
                file_content[filename] = {'headers':header}
                file_content[filename]['content'] = list(fh.read().split("\n"))

    return file_content


def getFilesNames():
    files_list = list(handler().keys())
    return files_list



