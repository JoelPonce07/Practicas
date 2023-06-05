#Importamos la libreria psycopg2
import psycopg2

#Declaramos las variables
dbname = 'alumno'
user = 'postgres'
password = '1234'
host = 'localhost'
port = '5432'

#Creamos una función para establecer la conexion a la BD
def conectar():

    #Dentro de este bloque hacemos un manejo de excepciones
    #Si Try tiene un error automaticamente ejecutara except
    try:
        #Parámetros de conexión tipo diccionario
        #Creamos conexion con la libreria psycopg2
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )

        return connection

    #Except mostrará un mensaje de error
    except psycopg2.Error as e:
        print('Error al conectar a la base de datos:', e)


#Funcion Crear
def crear_registro():
    #creamos una nueva variable y en ella nos conectamos a la BD mediante
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor() #Creamos el cursor
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))

            query = "Insert into estudiantes (nombre, apellido, edad) values (%s, %s, %s)"

            dato = (nombre, apellido, edad) #Creamos una variable y colocamos los parametros
            cursor.execute(query, dato) # Ejecuta una consulta
            conn.commit() #Confirma los cambios realizados

            print ("Se agregó a la lista un nuevo estudiante")

        except psycopg2.Error as e:
            print("Error al agregar los datos del estudiante", e)

        finally:
            conn.close() #Cerramos la conexion
            cursor.close()  #Cerramos el cursor


#Funcion Mostrar
def mostrar_estudiantes():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            query = "select id, nombre, apellido, edad from estudiantes"

            cursor.execute(query) # Ejecuta una consulta
            estudiantes = cursor.fetchall() # Trae los resultados de un select

            if estudiantes:
                print("\nListado de estudiantes:")
                for estudiante in estudiantes:
                    print(
                        f"id: {estudiante[0]}, nombre: {estudiante[1]}, apellido: {estudiante[2]}, edad: {estudiante[3]}")

            else:
                print("No hay estudiantes registrados.")

        except psycopg2.Error as e:
            print("Error al mostrar el listado de estudiantes")

        finally:

            conn.close()
            cursor.close()


#Funcion Modificar
def modificar_estudiante():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            id = int(input("Ingrese el id del estudiante a modificar: "))
            nombre = input("Ingrese el nuevo nombre del estudiante: ")
            apellido = input("Ingrese el nuevo apellido del estudiante: ")
            edad = int(input("Ingrese la nueva edad del estudiante: "))

            query = "update estudiantes set nombre = %s, apellido = %s, edad = %s where id = %s"
            dato = (nombre, apellido, edad, id)

            cursor.execute(query, dato)
            conn.commit() #Guardara los cambios

            if cursor.rowcount > 0: #Hara un recuento de filas de la BD
                print("Se modificó los datos del estudiante")
            else:
                print("No existe el estudiante con el ID ingresado")


        except psycopg2.Error as e:
                print("Error al modificar los datos del estudiante", e)

        finally:

            conn.close()
            cursor.close()


#Funcion Eliminar
def eliminar_estudiante():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            id = int(input("Ingrese el ID del estudiante a eliminar: "))

            query = "delete from estudiantes where id = %s"

            dato = (id,)

            cursor.execute(query, dato)
            conn.commit()

            if cursor.rowcount > 0:
                print("Se eliminó al estudiante de la lista")
            else:
                print("No existe el estudiante con el ID ingresado")


        except psycopg2.Error as e:
                print("Error al eliminar el estudiante", e)

        finally:
            conn.close()
            cursor.close()


#Menu de opciones
while True: #Este ciclo se ejecutara hasta que encuentre una sentencia  break
    print("\n******** Menú Principal ********")
    print("1. Crear un nuevo estudiante")
    print("2. Mostrar una lista de estudiante")
    print("3. Modificar datos de un estudiante")
    print("4. Eliminar un estudiante de la lista")
    print("5. Salir")

    num = input("Seleccione una opción: ") #Ingreso por teclado

    if num == '1':
        crear_registro()

    elif num == '2':
        mostrar_estudiantes()

    elif num == '3':
        modificar_estudiante()

    elif num == '4':
        eliminar_estudiante()

    elif num == '5':
        print("Ha salido del programa")
        break
    else:
        print("\nOpción inválida. Por favor, ingrese un número válido.")