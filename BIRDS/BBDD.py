import pymongo

# Conectarse al servidor de MongoDB
cliente = pymongo.MongoClient("mongodb://localhost:27017/")

# Crear una base de datos llamada "mi_base_de_datos"
mi_base_de_datos = cliente['TFG']

# Crear una colección llamada "mi_coleccion"
facebook = mi_base_de_datos['facebook']
twitter = mi_base_de_datos['twitter']
# Crear un documento