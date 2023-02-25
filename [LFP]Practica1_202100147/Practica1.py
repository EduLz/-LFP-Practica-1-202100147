import msvcrt
import csv
import os
import graphviz

from informacion import informacion
people = []
peliculas=[]
print("LENGUAJES FORMALES Y DE PROGRAMACION")
print("SECCION: A-")
print("CARNE:202100147")
print("NOMBRE: EDUARDO MISAEL LOPEZ AVILA")
print("Presione cualquier tecla para continuar...")
msvcrt.getch()

while(True):
    print("--------MENU PRINCIPAL--------")
    print("1.CARGAR ARCHIVO DE ENTRADA")
    print("2.GESTIONAR PELICULAS")
    print("3.FILTRADO")
    print("4.CREAR GRAFICA")
    print("5.SALIR")
    print("------------------------------")
    lang = input("Seleccione una opcion: ")
    match lang:
        case "1":
            print("INGRESE LA DIRECCION DEl ARCHIVO")
            directorioA= input()
            if os.path.exists(directorioA):
                csvfile = open(directorioA, 'r',encoding='utf-8')
                reader = csv.reader(csvfile, delimiter=';')     

                for row in reader:
                    nombrePelicula = row[0].strip()
                    nombreActor = row[1].strip()
                    anio=row[2].strip()
                    genero=row[3].strip()
                    actores=nombreActor.split(',')
                    limpio=[]
                    for i in actores:
                        limpio.append(i.strip())
                    for n in people:
                        if nombrePelicula==n.nombrePelicula and limpio==n.actores and anio==n.anio and genero==n.genero:
                            print("La película ",nombrePelicula," ya se encuentra en el registro.")
                            break
                    else:
                        newInfo = informacion(nombrePelicula, limpio, anio, genero)
                        people.append(newInfo)     
                print("-------------------------")
                print("-----ARCHIVO CARGADO-----")  
                print("-------------------------")    
                #for person in people:
                 #   person.print_nombrePelicula(),person.print_actores(),person.print_anio(),person.print_genero()
            else:
                print("El archivo no existe en la ruta especificada.")

        case "2":
            while(True):
                print("------------------------")
                print("1.     MOSTRAR PELICULAS")
                print("2.       MOSTRAR ACTORES")
                print("3.    SALIR DE ESTE MENU")
                print("------------------------")
                peliOpcion=input("Seleccione una opcion: ")
                match peliOpcion:
                    case "1":
                        print("----------------------------------------------")
                        print("ESTAS SON LAS PELICULA REGISTRADAS ACTUALMENTE")
                        print("----------------------------------------------")
                        for person in people:
                            person.print_nombrePelicula()
                        print("----------------------------------------------")
                        print("Presione cualquier tecla para continuar...")
                        msvcrt.getch()
                    case "2":
                        print("--------------------------------------------")
                        print("SELECCIONE UNA PELICULA PARA VER LOS ACTORES")
                        print("--------------------------------------------")
                        # Mostrar la lista de películas registradas
                        contador=0
                        for person in people:
                            peliculas.append(person)
                            print(contador,".",person.nombrePelicula)
                            contador +=1
                        peliculaSeleccionada = int(input("Seleccione una pelicula: "))# Preguntar al usuario de qué película quiere ver los actores
                        if int(peliculaSeleccionada)>=contador:
                            print("SELECCIONE UNA OPCION VALIDA")
                            peliculas.clear()
                            contador=0
                            break
                        else:
                            actoresMostrar = peliculas[peliculaSeleccionada].actores# Obtener la lista de actores de la película seleccionada
                            print("Actores de la película", peliculas[peliculaSeleccionada].nombrePelicula)# Imprimir la lista de actores
                            for actor in actoresMostrar:
                                print(actor)
                            print("--------------------------------------------")
                            peliculas.clear()
                            contador=0
                            print("Presione cualquier tecla para continuar...")
                        msvcrt.getch()
                    case "3":
                        print("REGRESANDO A MENÚ PRINCIPAL")  
                        break           
                    case _:
                        print("INGRESE UNA OPCION VALIDA")
        case "3":
            print("OPCION PARA FILTRAR")
            while(True):
                print("--------FILTRADO--------")
                print("1. FILTRADO POR ACTOR")
                print("2. FILTRADO POR AÑO")
                print("3. FILTRADO POR GÉNERO")
                print("4. REGRESAR A MENÚ PRINCIPAL")
                print("------------------------")
                filtroOpcion = input("Seleccione una opción: ")
                if filtroOpcion == "1":
                    print("FILTRADO POR ACTOR")
                    print("------------------------")
                    # Mostrar la lista de actores registrados
                    actores_registrados = set()
                    for person in people:
                        actores_registrados.update(person.actores)
                    print("ACTORES REGISTRADOS:")
                    for actor in actores_registrados:
                        print(actor)
                    print("------------------------")
                    # Preguntar al usuario qué actor quiere filtrar
                    actor_filtro = input("Seleccione un actor: ")
                    # Buscar las películas en las que participa el actor
                    peliculas_filtradas = []
                    for person in people:
                        if actor_filtro in person.actores:
                            peliculas_filtradas.append(person)
                    # Imprimir el resultado del filtrado
                    print("---------------------------")
                    print("RESULTADO DEL FILTRADO:")
                    contadorActores=1
                    if len(peliculas_filtradas) == 0:
                        print("No se encontraron películas con el actor seleccionado.")
                    else:
                        for pelicula in peliculas_filtradas:
                            print("--------","Pelicula:",contadorActores,"--------")
                            pelicula.print_nombrePelicula(), pelicula.print_genero(), pelicula.print_anio()
                            print("---------------------------")
                            contadorActores +=1
                    print("Presione cualquier tecla para continuar...")
                    msvcrt.getch()
                elif filtroOpcion == "2":
                    print("FILTRADO POR AÑO")
                    print("------------------------")
                    # Mostrar la lista de actores registrados
                    anios_registrados = set()
                    for person in people:
                        anios_registrados.update([person.anio])
                    print("AÑOS REGISTRADOS:")
                    for anioos in anios_registrados:
                        print(anioos)
                    print("------------------------")
                    # Preguntar al usuario el año a filtrar
                    anio_filtro = input("Ingrese el año a filtrar: ")
                    # Buscar las películas del año seleccionado
                    peliculas_filtradas = []
                    for person in people:
                        if person.anio == anio_filtro:
                            peliculas_filtradas.append(person)
                    # Imprimir el resultado del filtrado
                    print("---------------------------")
                    print("RESULTADO DEL FILTRADO:")
                    contadorAños=1
                    if len(peliculas_filtradas) == 0:
                        print("No se encontraron películas para el año seleccionado.")
                    else:
                        for pelicula in peliculas_filtradas:
                            print("--------","Pelicula:",contadorAños,"--------")
                            pelicula.print_nombrePelicula(), pelicula.print_genero()
                            print("---------------------------")
                            contadorAños+=1
                    print("Presione cualquier tecla para continuar...")
                    msvcrt.getch()
                elif filtroOpcion == "3":
                    print("FILTRADO POR GENERO")
                    print("------------------------")
                    # Mostrar la lista de genero registrados
                    generos_registrados = set()
                    for person in people:
                        generos_registrados.update([person.genero])
                    print("GENEROS REGISTRADOS:")
                    for genre in generos_registrados:
                        print(genre)
                    print("------------------------")
                    # Preguntar al usuario qué genero quiere filtrar
                    genero_filtro = input("Seleccione un genero: ")
                    # Buscar las películas en las que participa el genero
                    genero_filtradas = []
                    for person in people:
                        if genero_filtro in person.genero:
                            genero_filtradas.append(person)
                    # Imprimir el resultado del filtrado
                    print("---------------------------")
                    print("RESULTADO DEL FILTRADO:")
                    contadorGeneros=1
                    if len(genero_filtradas) == 0:
                        print("No se encontraron películas con el genero seleccionado.")
                    else:
                        for pelicula in genero_filtradas:
                            print("--------","Pelicula:",contadorGeneros,"--------")
                            pelicula.print_nombrePelicula(), pelicula.print_anio()
                            print("---------------------------")
                            contadorGeneros +=1
                    print("Presione cualquier tecla para continuar...")
                    msvcrt.getch()
                elif filtroOpcion == "4":
                    print("REGRESANDO AL MENU PRINCIPAL")
                    break
        case "4":
            def graphRelations(people):
                grafo = graphviz.Digraph('ejemplo', filename="D:\\USAC\\2023\\Primer Semestre\\LFP\\LAB-LFP\\Practica 1\\[LFP]Practica1_202100147\\grafo")
                grafo.attr(rankdir="LR", ranksep="3", nodestep="1")
                
                # Creamos los nodos para las películas y los actores
                for person in people:
                    grafo.node(str(person.nombrePelicula).replace(':',''), f'''<
                        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                            <TR>
                                <TD COLSPAN="2" bgcolor="#507bef"><FONT COLOR="black">{person.nombrePelicula}</FONT></TD>
                            </TR>
                            <TR>
                                <TD><FONT COLOR="black">{person.anio}</FONT></TD>
                                <TD><FONT COLOR="black">{person.genero}</FONT></TD>
                            </TR>
                        </TABLE>>''', shape="none")
                    for actor in person.actores:
                        grafo.node(str(actor), shape="box", style="filled", color="#36d6b2", fontcolor="black")

                        # Agregamos una conexión desde el actor hacia la película
                        grafo.edge(str(person.nombrePelicula).replace(':','')+":e",str(actor))

                grafo.view()
            print("--------------------------")    
            print("GRAFICA GENERADA CON EXITO")
            print("--------------------------")
            graphRelations(people)

        case "5":
            print("---------------------------")
            print("SALIENDO, TE TENGA BUEN DIA")
            print("---------------------------")
            break
        case _:
            print("INGRESE UN VALOR VALIDO")
            
