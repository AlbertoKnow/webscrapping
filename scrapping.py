from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

MUNDO = "https://elcomercio.pe/mundo/"
ELECCIONES = "https://elcomercio.pe/elecciones/"
POLITICA = "https://elcomercio.pe/politica/"
ECONOMIA = "https://elcomercio.pe/economia/"
LIMA = "https://elcomercio.pe/lima/"
DEPORTE = "https://elcomercio.pe/deporte-total/"
TECNOLOGIA = "https://elcomercio.pe/tecnologia/"

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/mundo')
def mundo():

    req = requests.get(MUNDO)

    status_code = req.status_code

    lista = []

    if status_code == 200:
        html = BeautifulSoup(req.text, 'html.parser')

        entradas = html.find_all(
            'h2', {
                'class': 'fs-wi__title'}
        )

        """images = html.find(
            'img',  {'class': 'lazy fs-wi__img loaded'}
        )

        print(images.get('src')

        for i in req.find('img', {'class': 'lazy fs-wi__img loaded'}):
            i.get('src')
            print(i)"""

        for entrada in entradas:
            titulo = entrada.find_all('a')

            for i in titulo:
                lista.append(i.text)

    else:
        print("Status code: " + status_code)

    context = {
        'titulares': lista
    }

    return render_template("titulares.html", **context)


@app.route('/elecciones2022')
def elecciones():

    req = requests.get(ELECCIONES)

    status_code = req.status_code

    lista = []

    if status_code == 200:
        html = BeautifulSoup(req.text, 'html.parser')

        entradas = html.find_all(
            'h2', {
                'class': 'fs-wi__title'}
        )

        for entrada in entradas:
            titulo = entrada.find_all('a')

            for i in titulo:
                lista.append(i.text)

    else:
        print("Status code: " + status_code)

    context = {
        'titulares': lista
    }

    return render_template("titulares.html", **context)


@app.route('/politica')
def politica():

    req = requests.get(POLITICA)

    status_code = req.status_code

    lista = []

    if status_code == 200:
        html = BeautifulSoup(req.text, 'html.parser')

        entradas = html.find_all(
            'h2', {
                'class': 'fs-wi__title'}
        )

        for entrada in entradas:
            titulo = entrada.find_all('a')

            for i in titulo:
                lista.append(i.text)

    else:
        print("Status code: " + status_code)

    context = {
        'titulares': lista
    }

    return render_template("titulares.html", **context)


@app.route('/economia')
def economia():

    req = requests.get(ECONOMIA)

    status_code = req.status_code

    lista = []

    if status_code == 200:
        html = BeautifulSoup(req.text, 'html.parser')

        entradas = html.find_all(
            'h2', {
                'class': 'fs-wi__title'}
        )

        for entrada in entradas:
            titulo = entrada.find_all('a')

            for i in titulo:
                lista.append(i.text)

    else:
        print("Status code: " + status_code)

    context = {
        'titulares': lista
    }

    return render_template("titulares.html", **context)


@app.route('/lima')
def lima():

    req = requests.get(LIMA)

    status_code = req.status_code

    lista = []

    if status_code == 200:
        html = BeautifulSoup(req.text, 'html.parser')

        entradas = html.find_all(
            'h2', {
                'class': 'fs-wi__title'}
        )

        for entrada in entradas:
            titulo = entrada.find_all('a')

            for i in titulo:
                lista.append(i.text)

    else:
        print("Status code: " + status_code)

    context = {
        'titulares': lista
    }

    return render_template("titulares.html", **context)


@app.route('/deportes')
def deportes():

    req = requests.get(DEPORTE)

    status_code = req.status_code

    lista = []

    if status_code == 200:
        html = BeautifulSoup(req.text, 'html.parser')

        entradas = html.find_all(
            'h2', {
                'class': 'fs-wi__title'}
        )

        for entrada in entradas:
            titulo = entrada.find_all('a')

            for i in titulo:
                lista.append(i.text)

    else:
        print("Status code: " + status_code)

    context = {
        'titulares': lista
    }

    return render_template("titulares.html", **context)


@app.route('/tecnologia')
def tecnologia():

    req = requests.get(TECNOLOGIA)

    status_code = req.status_code

    lista = []

    if status_code == 200:
        html = BeautifulSoup(req.text, 'html.parser')

        entradas = html.find_all(
            'h2', {
                'class': 'fs-wi__title'}
        )

        for entrada in entradas:
            titulo = entrada.find_all('a')

            for i in titulo:
                lista.append(i.text)

    else:
        print("Status code: " + status_code)

    context = {
        'titulares': lista
    }

    return render_template("titulares.html", **context)


app.run(debug=True)
