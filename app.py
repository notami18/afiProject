from openpyxl import load_workbook
from flask import Flask , render_template , request

# Carga del archivo Excel
wb = load_workbook ('data.xlsx')
sheet = wb.active

# Creación del diccionario
diccionario = {}
for row in sheet.iter_rows (min_row=2):
    palabra = row [0].value.strip().lower()
    pronunciacion = row [1].value.strip().lower()
    diccionario [palabra] = pronunciacion

# Aplicación Flask
app = Flask ( __name__ )


@app.route ( '/' )
def index():
    return render_template ( 'index.html' )


@app.route ( '/traducir' , methods=[ 'POST' ] )
def traducir():
    texto = request.form ['texto']
    traduccion = ''

    # Separación por palabras
    palabras = texto.split()

    # Traducción y concatenación
    for palabra in palabras:
        if palabra in diccionario:
            traduccion += diccionario[palabra]
        else:
            traduccion += palabra
        traduccion += ' '

    return render_template ( 'index.html' , traduccion=traduccion )


if __name__ == '__main__':
    app.run ( debug=True )
