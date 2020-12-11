'''Modulo para guardar los datos de los archivos CSV en MongoDB'''
import pymongo
from files_handler import handler

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Uploads"]
mycol = mydb["files"]

list_files = []
files = handler()
for i in files:
    #Mongo no soporta keys con '.' - eg. 'autos.csv' pasa a ser 'autos-csv'
    list_files.append({i.replace(".","-"):files[i]})

mycol.insert_many(list_files)



'''
if __name__ == '__main__':
    #devuelve la primer coincidencia del find
    #print(mycol.find_one())
    #devuelve el objeto cursor
    #print(mycol.find())
    #Precio descendente
    #print(mycol.find_one(sort=[("precio", pymongo.DESCENDING)]))'''