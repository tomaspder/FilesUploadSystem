'''Modulo para la conversion de los archivos subidos como CSV a HTML y PDF'''
import pandas as pd
import pdfkit as pdf
from files_handler import getFilesNames

def converter():
    #configuro el path relativo a la ubicación de wkhtmltopdf
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)
    files = getFilesNames()
    styles = "<style>table {font-family: Arial, Helvetica, sans-serif;border-collapse: collapse;width: 100%;}td, th {border: 1px solid #ddd;padding: 8px;}tr:nth-child(even){background-color: #f2f2f2;}tr:hover {background-color: #ddd;}th {padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #4CAF50;color: white;}</style>"
    download_pdf = '<a href="/uploads/pdf_files/{file}"  download>Descargar PDF</a>'
    files_html = {}
    for i in files:
        #seteo los nombres de los archivos con la extension correspondiente
        csv_file = 'uploads/'+i
        html_file = csv_file[:-3]+'html'
        pdf_file = csv_file[:-3]+'pdf'
        dataframe = pd.read_csv(csv_file, sep=';')
        #obtengo el dataframe como string html, y le adhiero estilos y descarga de pdf
        str_html = download_pdf.format(file=pdf_file[8:]) + styles + dataframe.to_html()
        print(str_html)
        #creo el archivo html con el string anteriormente creado, y luego lo utilizo para crear el pdf
        with open('templates/'+html_file[8:], 'w') as f:
            f.write(str_html)
            f.close()
        pdf.from_file('templates/'+html_file[8:], 'uploads/pdf_files/'+pdf_file[8:], configuration=config)
        #diccionario con el nombre del archivo y su contenido html plano (para retornalo como vista con Flask)
        files_html[html_file[8:]] = str_html

    return files_html



