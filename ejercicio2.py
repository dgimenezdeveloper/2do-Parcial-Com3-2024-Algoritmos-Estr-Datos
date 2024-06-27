if __name__ == "__main__":
    nombres = ["Juan", "Pedro", "Maria", "Lucia", "Dario", "Jose", "Ana", "Laura"]
    carreras = ["Ingenieria", "Medicina", "Tec Univ en Programacion", "Arquitectura", "Economia", "Contabilidad"]
    
    lista = ListaDoblementeEnlazada()
    lista.lista_ejemplo(nombres, carreras, 10)

    print("Lista original:")
    for alumno in lista:
        print(alumno)

    lista_ordenada = lista.ordenar_lista()

    print("\nLista ordenada por fecha de ingreso:")
    for alumno in lista_ordenada:
        print(alumno)

    manejar_archivos_directorios(lista_ordenada)
