# Amino Phishing

[![Build Status](https://travis-ci.org/Fedeya/amino-phishing.svg?branch=master)](https://travis-ci.org/Fedeya/amino-phishing)
[![Python 3.6](https://img.shields.io/badge/python-3.6%20%7C%203.7-green.svg)](https://www.python.org/downloads/release/python-360/)



### Phishing para la red social Amino que suplanta una comunidad

  ![alt text](https://i.imgur.com/EG1q7yf.png) 



## Termux - Instalacion

 Aqui se vera la instalacion en **Android** **Termux**


```
apt install php git openssh python
pip3 install colorama
git clone https://github.com/Fedeya/amino-phishing.git
```

## Arch - Manjaro - Instalacion

 Aqui se vera la instalacion  en **Arch Linux y Distribuciones Basadas en Arch Linux**


```
sudo pacman -S php git openssh python python-pip
pip3 install colorama --user
git clone https://github.com/Fedeya/amino-phishing.git
```

## Uso:

```
cd amino-phishing
python3 aminophishing.py
```

## Agregar Imagenes


Para añadir imagenes al resultado final de la comunidad falsa solo deben ser metidas en la carpeta de **images** de la raiz del repositorio y luego ser llamadas con su extension desde el script python 

> Importante el nombre de la imagen no debe contener espacios

> En el caso de no querer imagenes dejar el espacio vacio

### Ejemplo

```
cp ~/Imágenes/portada.jpg ~/amino-phishing/images/
```
![alt text](https://i.imgur.com/9HUdBFA.png)
