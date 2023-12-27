# Pokedex Django
Proyecto de Pokedex en Django(migrado de Laravel)

*Este proyecto se migro de Laravel a Django, tratando de que la funcionalidad sea migrada casi al 100%(esto puede variar dada a las limitantes del framework Django en comparación con Laravel o viceversa)*

---

## Pre requisitos

Para poder levantar este entorno de desarrollo se deben tener instalados en la PC lo siguiente:

1. Python >= v3.10
2. La libreria de Python "venv".
3. Git

>##### ***Nota: este proyecto se probo en Ubuntu 22.04 con WSL 2.***

---

## Instalar el ambiente virtual de desarrollo

1. Creamos nuestro entorno: `python3 -m venv entornos/pokedex`
2. Activamos el entorno: `cd entornos/pokedex && . bin/activate`
3. Clonamos el codigo fuente: `git clone https://github.com/krsrk/pokedex-django.git pokedex-site`
4. Navegar a la carpeta del proyecto: `cd pokedex-site`
5. Instalamos los requerimientos del proyecto: `pip install -r requirements.txt`
6. Iniciamos el servidor de desarrollo: `python manage.py runserver 8080`
7. Revisamos el sitio en el explorador de internet: **http://localhost:8080**

---
