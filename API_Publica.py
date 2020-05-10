#libreria
import requests
import json
import os
import urllib

# direccion API publica que voy a utilizar
# https://api.jikan.moe/v3/search/anime?q=Dragon%20ball%20gt&limit=16

try:
    def menu():
        os.system('cls')
        print('**__MENU__**')
        print('1. Almacena el contenido de la pagina web en un json')
        print('2. Dame los titulos de la lista de Dragon Ball Z.')
        print('3. Obtener el numero de la ultima página.')
        print('4. SALIR')

        opciones=int(input('Elije una opción: '))
        return(opciones)
    
    def opciones1():
        if respuesta.status_code == 200:
            cont = respuesta.content
            file= open('anime.json', 'wb')
            file.write(cont)
            file.close()

    def opciones2():       
        if respuesta.status_code == 200:
            load= respuesta.json()
            resultado= load.get('results', [])

            if resultado:
                for i in resultado:
                    titulo = i['title']
                    print(titulo)

    def opciones3():
        if respuesta.status_code == 200:
            load= respuesta.json()
            resultado= load.get('last_page')
            print(resultado)

    while True:
        url='https://api.jikan.moe/v3/search/anime?q=Dragon%20ball%20gt&limit=16'
        respuesta=requests.get(url)
        
        opciones=menu()
        if opciones == 1:
            opciones1()

        elif opciones == 2:
           opciones2()

        elif opciones == 3:
            opciones3()
            
        elif opciones == 4:
            break

        input('Pulsa cualquier tecla para terminar...')
except:
    print('Ha surgido un error')