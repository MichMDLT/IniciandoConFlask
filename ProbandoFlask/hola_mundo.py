from flask  import Flask

app = Flask(__name__) #NECESITAMOS unaInstancia --> nuevo objeto, que recibe como parámetro __name__
#hasta ahorita es normal el NOT FOUND
#Porque NO tengo una DIRECCIÓN a donde hacer la petición

"""
En la ARQ. CLIENTE-SERVIDOR:
Un cliente desde su navegador/movil hace una petición a un SERVER
EN ESTE CASO este será el servidor.

El Server tiene la obligación de manejar la PETICIÓN y responder 
en cualquier formato HTML, JSON, XML, etc.
"""

#Necesitamos indicar A QUE RUTA EL CLIENTE PUEDE ACCEDER y para eso:
#un decorador:
#Recibe un string, pero usaremos un / poraue NO queremos una ruta como tal
#Sino que al entrar al LOCALHOST 5000 responda :)
@app.route('/')#wrap o decorador = indica rutas a donde el USER puede entrar 

def index():
    return 'Hola mundito desde Flask!  B)' #regresa un string

# ↓ Solo se ejecuta si el archivo se corre directamente ↓
if __name__ == '__main__':
#Es una condición que verifica si el archivo Python se está ejecutando directamente 
# (por ejemplo, con python hola_mundo.py) 
# o si está siendo importado por otro archivo (como un módulo).
#COMO MÓDULO:
#   import hola_mundo  # Importas tu app Flask
#Entonces __name__ será 'hola_mundo' (el nombre del módulo), y el bloque del if no se ejecutará.

#Problema: Si otro archivo hace import hola_mundo, el servidor se iniciará (¡y eso no queremos!).

    app.run(debug=True)
#Este método inicia el servidor de desarrollo de Flask,
# y el parámetro debug=True activa el modo depuración, que incluye:
#Recarga automática: El servidor se reinicia automáticamente
# cuando modificas el código (¡muy útil durante el desarrollo!
#Depurador interactivo: Si hay un error, 
# te muestra un traceback detallado en el navegador e
# incluso permite ejecutar código en el contexto del error.
#Mensajes detallados: Muestra logs más descriptivos en la terminal.

#IMPORTANTE:
#El modo debug no debe usarse en producción porque puede exponer información sensible (como claves o rutas del sistema). 
# Solo es para desarrollo.