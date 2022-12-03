from mongodb import PyMongo

varmongo = {}
varmongo["host"] = "localhost"
varmongo["db"] = "itj_estudiantes"
varmongo["port"] = 27017
varmongo["timeout"] = 1000
varmongo["user"] = ""
varmongo["password"] = "root"

lista = [
    {
        "idProducto": 1850,
        "productoNombreCorto": "William Lawsons Std",
        "productoNombreLargo": "Whisky William Lawsons Std 750 ml",
        "productoDescripcion": "Es un whisky afrutado de cuerpo ligero, se caracteriza por su aroma a pastel de manzana y su sabor a cereal tostado y al tofee, con un final suave.",
        "productoTipo": 1,
        "productoPresentacion": "Botella",
        "productoCosto": 170.5,
        "productoGanancia": 15,
        "productoDescuento": 0,
        "productoExistencia": 1000,
        "productoImagen": "Whisky-1850.webp"
    },
    {
        "idProducto": 1450,
        "productoNombreCorto": "Outer Space",
        "productoNombreLargo": "Vodka Outer Space 750 ml",
        "productoDescripcion": "Es un vodka hecho con maíz 100% americano, sin gluten, el diseño de su botella es único y llamativo. Tiene aromas y sabores a frutos secos.",
        "productoTipo": 1,
        "productoPresentacion": "Botella",
        "productoCosto": 700.5,
        "productoGanancia": 15,
        "productoDescuento": 0,
        "productoExistencia": 1000,
        "productoImagen": "Vodka-1450.webp"
    },
    {
        "idProducto": 850,
        "productoNombreCorto": "Ron Antillano Blanco",
        "productoNombreLargo": "Ron Antillano Blanco C/Vaso/Macerador 1L",
        "productoDescripcion": "",
        "productoTipo": 1,
        "productoPresentacion": "Botella",
        "productoCosto": 150.5,
        "productoGanancia": 15,
        "productoDescuento": 0,
        "productoExistencia": 1000,
        "productoImagen": "Ron-850.webp"
    }
]

def insertar(lista):
    obj = PyMongo(varmongo)
    obj.conectar_mongodb()
    for lis in lista:
        insertLista = {
            'idProducto': lis['idProducto'],
            'productoNombreCorto': lis['productoNombreCorto'],
            'productoNombreLargo': lis['productoNombreLargo'],
            'productoDescripcion': lis['productoDescripcion'],
            'productoTipo': lis['productoTipo'],
            'productoPresentacion': lis['productoPresentacion'],
            'productoCosto': lis['productoCosto'],
            'productoGanancia': lis['productoGanancia'],
            'productoDescuento': lis['productoDescuento'],
            'productoExistencia': lis['productoExistencia'],
            'productoImagen': lis['productoImagen']
        }
        resp = obj.insertar('Examen', insertLista)
    obj.desconectar_mongodb()
    print('Campos insertados')

insertar(lista)