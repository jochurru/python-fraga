#Diccionario con detalles de las peliculas separadas por genero.

# Terror
pesadilla_en_la_calle_elm = {
    "Descripcion": "Clásico del terror.",
    "Cantidad": 5,
    "Precio": 4000,
    "Categoria": "Terror",
    "Lanzamiento": 1984
}

halloween = {
    "Descripcion": "El inicio del género slasher.",
    "Cantidad": 6,
    "Precio": 3900,
    "Categoria": "Terror",
    "Lanzamiento": 1978
}

el_resplandor = {
    "Descripcion": "Obra maestra del horror psicológico.",
    "Cantidad": 7,
    "Precio": 4200,
    "Categoria": "Terror",
    "Lanzamiento": 1980
}

# Ciencia ficción
blade_runner = {
    "Descripcion": "Pionero del cyberpunk.",
    "Cantidad": 6,
    "Precio": 4500,
    "Categoria": "Ciencia Ficcion",
    "Lanzamiento": 1982
}

mad_max = {
    "Descripcion": "Distopía y acción en el desierto.",
    "Cantidad": 10,
    "Precio": 4000,
    "Categoria": "Ciencia Ficcion",
    "Lanzamiento": 1979
}

doce_monos = {
    "Descripcion": "Thriller de viajes en el tiempo.",
    "Cantidad": 4,
    "Precio": 3500,
    "Categoria": "Ciencia Ficcion",
    "Lanzamiento": 1995
}

# Drama
forrest_gump = {
    "Descripcion": "Un hombre con un corazón puro vive grandes aventuras.",
    "Cantidad": 9,
    "Precio": 3800,
    "Categoria": "Drama",
    "Lanzamiento": 1994
}

el_club_de_la_pelea = {
    "Descripcion": "Un hombre se enfrenta a su vacío existencial.",
    "Cantidad": 8,
    "Precio": 3600,
    "Categoria": "Drama",
    "Lanzamiento": 1999
}

milagros_inesperados = {
    "Descripcion": "Un drama conmovedor en el corredor de la muerte.",
    "Cantidad": 5,
    "Precio": 4000,
    "Categoria": "Drama",
    "Lanzamiento": 1999
}

# Fantasía
el_labertino_del_fauno = {
    "Descripcion": "Oscura fantasía ambientada en la posguerra española.",
    "Cantidad": 7,
    "Precio": 3900,
    "Categoria": "Fantasía",
    "Lanzamiento": 2006
}

harry_potter_y_la_piedra_filosofal = {
    "Descripcion": "Un joven descubre que es un mago.",
    "Cantidad": 12,
    "Precio": 4500,
    "Categoria": "Fantasía",
    "Lanzamiento": 2001
}

narnia_el_leon_la_bruja_y_el_ropero = {
    "Descripcion": "Cuatro hermanos descubren un mundo mágico.",
    "Cantidad": 10,
    "Precio": 4000,
    "Categoria": "Fantasía",
    "Lanzamiento": 2005
}

# Animación
shrek = {
    "Descripcion": "Un ogro y un burro emprenden una divertida misión.",
    "Cantidad": 15,
    "Precio": 3400,
    "Categoria": "Animacion",
    "Lanzamiento": 2001
}

intensamente = {
    "Descripcion": "Las emociones cobran vida dentro de una niña.",
    "Cantidad": 12,
    "Precio": 3800,
    "Categoria": "Animacion",
    "Lanzamiento": 2015
}

up = {
    "Descripcion": "Un anciano y un niño se embarcan en una aventura aérea.",
    "Cantidad": 10,
    "Precio": 3700,
    "Categoria": "Animacion",
    "Lanzamiento": 2009
}

# Acción
rapidos_y_furiosos = {
    "Descripcion": "Carreras clandestinas y acción trepidante.",
    "Cantidad": 8,
    "Precio": 3500,
    "Categoria": "Acción",
    "Lanzamiento": 2001
}

terminator_2 = {
    "Descripcion": "Un cyborg intenta salvar a la humanidad.",
    "Cantidad": 6,
    "Precio": 4000,
    "Categoria": "Acción",
    "Lanzamiento": 1991
}

john_wick = {
    "Descripcion": "Un asesino letal en busca de venganza.",
    "Cantidad": 10,
    "Precio": 4200,
    "Categoria": "Acción",
    "Lanzamiento": 2014
}

#Diccionario que contiene todo el "Stock" de las peliculas.
stock={
    "pesadilla en la calle elm": pesadilla_en_la_calle_elm,
    "halloween": halloween,
    "el resplandor": el_resplandor,
    "blade runner": blade_runner,
    "mad max": mad_max,
    "doce monos": doce_monos,
    "forrest gump": forrest_gump,
    "el club de la pelea": el_club_de_la_pelea,
    "milagros inesperados": milagros_inesperados,
    "el labertino del fauno":el_labertino_del_fauno,
    "harry potter y la piedra filosofal":harry_potter_y_la_piedra_filosofal,
    "narnia el leon la bruja y el ropero":narnia_el_leon_la_bruja_y_el_ropero,
    "shrek":shrek,
    "intensamente":intensamente,
    "up":up,
    "rapidos y furiosos":rapidos_y_furiosos,
    "terminator 2":terminator_2,
    "john wick":john_wick
}
#Funciones complementarias para consulta de datos de productos.
#Funcion "Buscar por cantidad minima"
def buscar_por_cantidad():
    titulo="***BUSCAR POR CANTIDAD***"
    print(titulo.center(60))
    print("-"*60)
    try:
        cantidad_minima=int(input("Ingrese la cantidad minima de stock a buscar: "))
        resultados={clave:valor for clave, valor in stock.items() if valor["Cantidad"]>= cantidad_minima}
        if resultados:
            print("\nPeliculas con cantidad mayor o igual a ",cantidad_minima,":\n")
            for nombre, datos in resultados.items():
                print(f"Nombre:{nombre.title()} | Cantidad: {datos['Cantidad']}")
        else:
            print(f"No se encontraron productos con cantidad mayor o igual a {cantidad_minima}.\n")
    except ValueError:
        print("Error:Debe ingresar un valor numerico!\n")
#Funcion "Buscar por precio"
def buscar_por_precio():
    titulo="***BUSCAR POR PRECIO***"
    print(titulo.center(60))
    print("-"*60)
    try:
        precio_maximo=int(input("Ingrese el precio maximo a buscar: "))
        resultados={clave:valor for clave, valor in stock.items() if valor['Precio']>=precio_maximo}

        if resultados:
            print("\nPeliculas con precio mayor o igual a", precio_maximo,":\n")
            for nombre, datos in resultados.items():
                print(f"Nombre: {nombre.title()} | Precio: $ {datos['Precio']}")
        else:
            print(f"No se encotraron productos con precio mayor o igual a ${precio_maximo}.\n")
    except ValueError:
        print("Error: Debe ingresar un valor numerico!\n")
#Funcion "Buscar por categoria"
def buscar_por_categoria():
    titulo="***BUSCAR POR CATEGORIA***" 
    print(titulo.center(60))
    print("-"*60)
    categoria=input("Ingrese la categoria a buscar: ").strip().lower()
    resultados={clave:valor for clave,valor in stock.items() if valor ['Categoria'].lower()==categoria}
    if resultados:
        print(f"\n Peliculas en la categoria '{categoria.title()}':\n")
        for nombre, datos in resultados.items():
            print(f"Nombre: {nombre.title()} | Categoria: {datos['Categoria']}")
    else:
        print(f"No se encotraron peliculas en la categoria '{categoria.title()}'.\n")
#Funcion "Buscar por año de lanzamiento"
def buscar_por_lanzamiento():
    titulo="***BUSCAR POR AÑO DE LANZAMIENTO***" 
    print(titulo.center(60))
    print("-"*60)
    try:
        anio_lanzamiento=int(input("Ingrese el año de lanzamiento a buscar: "))
        resultados={clave:valor for clave,valor in stock.items() if valor['Lanzamiento']==anio_lanzamiento}
        if resultados:
            print(f"\n Productos lanzados en el año {anio_lanzamiento}: \n")

        for nombre, datos in resultados.items():
            print(f"Nombre: {nombre.title()} | Lanzamiento: {datos['Lanzamiento']}")
        else:
            print(f"No se encontraron peliculas lanzadas en el año {anio_lanzamiento}.\n")
    except ValueError:
        print("Error: Debe ingresar un valor numerico!\n")
#Se define submenu de busqueda avanzada para funcion 1.
def menu_busqueda():
    while True:
        print("-"*60)
        print("MENU DE BUSQUEDA".center(60))
        print("-"*60)
        print("1- Buscar por cantidad")
        print("2- Buscar por precio")
        print("3- Buscar por categoria")
        print("4- Buscar por año de lanzamiento")
        print("5- Volver al menu principal")
        try:
            opcion=int(input("Seleccione una opcion (1-5): "))
            if opcion ==1:
                buscar_por_cantidad()
            elif opcion==2:
                buscar_por_precio()
            elif opcion==3:
                buscar_por_categoria()
            elif opcion==4:
                buscar_por_lanzamiento()
            elif opcion==5:
                print("Regresando al menu principal...")
                break
            else:
                print("Opcion no valida, por favor ingrese un numero de 1 a 5")
        except ValueError:
            print("Error: Debe ingresar un valor numerico!\n")           
# Se define la función 1 - "Alta de productos nuevos"
def alta_producto():
    titulo = "***AGREGAR PRODUCTOS AL CATALOGO***"
    print(titulo.center(60))
    print("-" * 60)

    # Bucle principal para ingresar productos
    while True:
        nombre_pelicula = input("Ingrese el nombre de la película o 'salir' para regresar al menú principal: ").strip().lower()
        if nombre_pelicula == "salir":
            print("Regresando al menú principal...")
            break

        if nombre_pelicula in stock:
            print("EL PRODUCTO QUE INGRESÓ, YA SE ENCUENTRA EN EL STOCK.")
            actualizar = input("¿Desea actualizar la información? (s/n): ").strip().lower()
            if actualizar == "s":
                descripcion = input("Ingrese una nueva descripción: ").strip()
                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad: "))
                        break
                    except ValueError:
                        print("Error: Debe ingresar un número.")
                while True:
                    try:
                        precio = int(input("Ingrese el precio: "))
                        break
                    except ValueError:
                        print("Error: Debe ingresar un número.")
                categoria = input("Ingrese la categoría de la película: ").strip()
                while True:
                    try:
                        lanzamiento = int(input("Ingrese el año de lanzamiento: "))
                        break
                    except ValueError:
                        print("Error: Debe ingresar un número.")

                # Se actualiza el producto existente en el diccionario
                stock[nombre_pelicula] = {
                    "Descripcion": descripcion,
                    "Cantidad": cantidad,
                    "Precio": precio,
                    "Categoria": categoria,
                    "Lanzamiento": lanzamiento
                }
                print(f"El producto '{nombre_pelicula}' se modificó correctamente.")
                break  # Termina la iteración para este producto

        else:
            descripcion = input("Ingrese una breve descripción: ").strip()
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número.")
            while True:
                try:
                    precio = int(input("Ingrese el precio: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número.")
            categoria = input("Ingrese la categoría de la película: ").strip()
            while True:
                try:
                    lanzamiento = int(input("Ingrese el año de lanzamiento: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número.")

            # Se agrega el nuevo producto al diccionario
            stock[nombre_pelicula] = {
                "Descripcion": descripcion,
                "Cantidad": cantidad,
                "Precio": precio,
                "Categoria": categoria,
                "Lanzamiento": lanzamiento
            }
            print(f"Producto '{nombre_pelicula}' fue agregado correctamente.")
            break  # Termina la iteración para este producto


#Se define la funcion 2- "Consulta de datos de productos"
def consulta_productos():
    titulo="***CONSULTA DE DATOS DE PRODUCTOS***"
    print(titulo.center(60))
    print("-"*60)

    while True:
        nombre_pelicula=input("Ingrese el nombre de la pelicula o 'salir' si quiere regresar al menu de opciones: ").strip().lower()
        if nombre_pelicula=="salir":
            print("Regresando al menu de opciones...")
            break
        if nombre_pelicula in stock:
            producto=stock[nombre_pelicula]
            print("\nInformacion del producto:")
            print(f"Nombre: {nombre_pelicula.title()}")
            print(f"Descripcion: {producto['Descripcion']}")
            print(f"Cantidad disponible: {producto['Cantidad']}")
            print(f"Precio: ${producto['Precio']}")
            print(f"Categoria: {producto['Categoria']}")
            print(f"Año de lanzamiento: {producto['Lanzamiento']}")
        else:
            print(f"No se encontro el producto '{nombre_pelicula}' en el catalogo\n")
            #Se le da opcion de cargar el producto que no existe.
            carga_nueva=input("Desea cargar la pelicula al stock? (s/n)").strip().lower()
            if carga_nueva=="s":
                alta_producto()
            elif carga_nueva=="n":
                print("Regresando al menu de opciones...")
                break
        
#Se define la funcion 3- "Modificar la cantidad de stock de un producto."            
def modificar_stock():
    titulo="***MODIFICAR CANTIDAD DE STOCK***"
    print(titulo.center(60))
    print("-"*60)
    nombre_pelicula= input("Ingrese el nombre de la pelicula de la que quiera modificar el stock o 'salir' para salir al menu principal: ").strip().lower()

    if nombre_pelicula=="salir":
        print("Regresando al menu principal...")
        return

    if nombre_pelicula in stock:
        print(f"La informacion actual del producto es '{nombre_pelicula.title()}: ")
        print(f"Cantidad actual en stock: {stock[nombre_pelicula]['Cantidad']}")

        while True:
            try:
                nueva_cantidad=int(input("Ingrese la nueva cantidad de stock: "))
                if nueva_cantidad<0:
                    print("Error, la cantidad ingresada no debe ser negativa.")
                else:
                    break
            except ValueError:
                print("Error: Debe ingresar un valor numerico!\n")
        
        #Actualizar stock.
        stock[nombre_pelicula]['Cantidad'] = nueva_cantidad
        print(f"La cantidad del producto '{nombre_pelicula.title()}' ha sido actualizada a {nueva_cantidad}.\n")
    else:
        print(f"El producto '{nombre_pelicula.title()}', no se encuentra en el catalogo\n")

#Se define la funcion 4-"Dar de baja productos"
def dar_baja_producto():
    titulo="***ELIMINAR PRODUCTOS***"
    print(titulo.center(60))
    print("-"*60)
    
    while True:
        #se solicita nombre de producto o "salir"
        nombre_pelicula=input("Ingrese el nombre de la pelicula a eliminar o 'salir' para regresar al menu principal:").strip().lower()

        if nombre_pelicula == "salir":
            print("Regresando al menu principal...")
            break
        
        if nombre_pelicula in stock:
            print(f"Producto encontrado:{nombre_pelicula}")
            confirmacion= input("Esta seguro que quiere eliminar ese producto? (s/n): ")
            if confirmacion=="s":
                del stock[nombre_pelicula] #elimina el producto solicitado
                print(f"El producto '{nombre_pelicula}' ha sido eliminado correctamente.")
            else:
                print("Operacion cancelada. El producto no se elimino.")
        else:
            print(f"El producto '{nombre_pelicula}' no se encuentra en el catalogo")

#Se define la funcion 5- "Listado completo de los productos.
def listar_productos():
    titulo="***LISTADO COMPLETO DE PRODUCTOS***"
    print(titulo.center(60))
    print("-"*60)
    #Primero se verifica si hay productos en el stock
    if not stock:
        print("El stock esta vacio, No hay productos para listar.")
    else:
        #Se recorre y muestra el stock de los productos.       
        for nombre, detalles in stock.items():
            print(f"Producto: {nombre.capitalize()}")
            print(f"Descripcion: {detalles.get('Descripcion', 'Sin descripcion')}")
            print(f"Cantidad: {detalles.get('Cantidad', 0)}")
            print(f"Precio $:{detalles.get('Precio', 0)}")
            print(f"Categoria: {detalles.get('Categoria', 'No especificado')}")
            print(f"Lanzamiento: {detalles.get('Lanzamiento', "No especificado")}")
            print("-"*60)
    print("Fin del listado\n")

#Se define la funcion 6- "listado con stock bajo minimo"
def listar_bajo_minimo():
    titulo="***LISTAR STOCK CON BAJO MINIMO***"
    print(titulo.center(60))
    print("-"*60)
    #definimos con el usuario el stock bajo minimo.
    while True:
        try: 
            stock_minimo=int(input("Ingrese el stock minimo a buscar: "))
            break
        except ValueError:
            print("Error, Debe ingresar un numero valido.")
    productos_bajo_minimo=[]

    #Buscar productos con stock bajo minimo ingresado.
    for nombre, detalles in stock.items():
        if detalles.get('Cantidad', 0)<stock_minimo:
            productos_bajo_minimo.append((nombre, detalles))
    #Mostramos Resultados.
    if not productos_bajo_minimo:
        print(f"Todos los productos tienen stock igual o superior a {stock_minimo}.")
    else:
        print(f"Productos con stock bajo minimo menor a {stock_minimo}:")
        for nombre, detalles in productos_bajo_minimo:
            print(f"Producto: {nombre.capitalize()}")
            print(f"Descripcion: {detalles.get('Descripcion', 'Sin descripcion')}")
            print(f"Cantidad: {detalles.get('Cantidad', 0)}")
            print(f"Categoria: {detalles.get('Categoria', 'No especificada')}")
            print(f"Lanzamiento: {detalles.get('Lanzamiento', 'No especificado')}")
            print("-"*60)
    print("Fin del listado. \n")

    


#Definimos el menu con un bucle.
def menu():
    while True:
        #Encabezado
        print("-" * 70)
        print("MENU PRINCIPAL".center(70))
        print("-" * 70)
        #Menu de opciones
        print("Menu gestion de productos\n")
        print("1. Alta de productos nuevos")
        print("2. Consulta de datos de productos")
        print("3. Modificar la cantidad en stock de un producto")
        print("4. Dar de baja productos")
        print("5. Listado completo de los productos")
        print("6. Lista de productos con cantidad bajo mínimo")
        print("7. Salir")
          
        try:
            #solicitamos al usuario que ingrese una opcion valida.
            opcion=int(input("Ingrese una opcion del menu '(1/7)': "))

            #procesamos la opcion que solicito el usuario
            if   opcion==1:
                print("Has seleccionado, 1-'Alta de productos nuevos'")
                alta_producto()
            elif opcion==2:
                print("Has seleccionado, 2-'Consulta de productos'")
                while True:
                    try:
                        print("-"*60)
                        print("***Menu de opciones***".center(60))
                        print("-"*60)
                        print("Opcion 1: busqueda por nombre")
                        print("Opcion 2: busqueda avanzada")
                        print("Opcion 3: Salir al menu principal")
                        opcion=int(input("Ingrese opcion a buscar: (de 1 a 3): "))
                    except ValueError:
                         print("Error: Debe ingresar un valor numerico!\n")
                    if opcion==1:
                        consulta_productos()
                    elif opcion==2:
                        print("***MENU DE BUSQUEDA AVANZADA".center(60))
                        print("-"*60)
                        menu_busqueda()
                    elif opcion==3:
                        break
                    else:
                            print("Ingrese la opcion 1 o 3 solamente, vuelva a ingresar opcion.")
                   
            elif opcion==3:
                 print("Has seleccionado, 3-'Modificar la cantidad en stock de un producto'")
                 modificar_stock()
            elif opcion==4:
                print("Has seleccionado, 4-'Dar de baja productos'") 
                dar_baja_producto()
            elif opcion==5:
                print("Has seleccionado, 5-'Listado completo de los productos'") 
                listar_productos()
            elif opcion==6:
                print("Has seleccionado, 6-'Lista de productos con cantidad bajo mínimo'")
                listar_bajo_minimo()
            elif opcion==7:
                print("Finalizando el programa.")
                break
            else:
                print("Opcion no válida, Ingrese nuevamente una opcion (1/7)")
        except ValueError:
            print("Error debe ingresar un numero entero, vuelva a ingresar opcion.")

menu()