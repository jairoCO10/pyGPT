from dotenv import load_dotenv #pip install python-dotenv

import os
# carga las variables de entorno desde el archivo .env
load_dotenv()

'''
se llaman las key necesarias para el uso de las api 
en este caso  la configuracion del archivo .env es la sigiente 
GPT_KEY=
OPW_KEY=
despues del igual se pone la key sin comillas
se le asigna un nombre al a key y se llama con el comando de abajo
'''
GPT_KEY = os.getenv("GPT_KEY")
OPW_KEY = os.getenv("OPW_KEY")
