import os
import re


def abrir_archivo(nombre):
    """
    Función creada para abrir el archvo.
    :param nombre: es el nombre del archivo
    :return: Devuelve el contenido del archivo
    """
    path = os.getcwd()
    print(path)            # Cada vez que utilizemos esta función, mostrara el directorio de trabajo
#    if os.path.isdir(nombre):
#        pass
#    else:
#        print(os.chdir(nombre))
    archivo = open(nombre, encoding="utf8")
    articulo = archivo.read(100000)
    return articulo


def contar_palabras(texto):
    """
    Esta función cuenta las palabras almacenadas en la variable "texto"
    :param texto: es el return de la función "abrir_archivo"
    :return: Devuelve el resultado del conteo
    """
    return len(texto.split())


def mayusculas(patron, texto):
    """
    Esta función sevirá para varios puntos, cambiando el nombre de la variable de salida
    :param patron: define el patrón de busqueda
    :param texto: indica el archivo de texto
    :return: devolverá o las siglas, las palabras en mayúsculas o los signos de puntuación, según el patrón
    """
    lista = re.findall(patron, texto)
    return lista


def minusculas(texto):
    """
    Función para poner el texto en minúsculas
    :param texto: indica el archivo
    :return: devolverá el texto en minúculas
    """
    return texto.lower()


def e_punt(patron, texto):
    """
    Elininamos los signos de puntuación. Se cmabian por espacios en blanco. Ojo!!! parametro texto
    :param patron: define patron de busqueda
    :param texto: define el texto a analizar ---> ojo, a lo largo de las funciones debenos ir cambiando los
    textos por los modificados previamente.
    :return: Devuelve el texto sin signos.
    """
    return re.sub(patron, " ", texto)


def elimina_acentos(texto):
    """
    Se buscan las letras con acento y se cambian por las que no tienen
    :param texto: archivo de texto
    :return: devuelve el archivo modificado
    """
    t1 = None

    for i in texto:
        if i == 'á':
            t1 = re.sub(i, "a", texto)
        elif i == 'é':
            t1 = re.sub(i, "e", t1)
        elif i == 'í':
            t1 = re.sub(i, "i", t1)
        elif i == 'ó':
            t1 = re.sub(i, "o", t1)
        elif i == 'ú':
            t1 = re.sub(i, "u", t1)
    return t1


def eliminar_numeros(patron, texto):
    """
    Mostramos números y se borran
    :param patron: correspondiente a la búsqueda de números
    :param texto: el archivo
    :return: devuelve el archivo sin números, previamente, la función muestra los números que ha encontrado
    """
    numeros = re.findall(patron, texto)
    print(f'\nLos numeros encontrados han sido: \n\n{"-".join(numeros)}')
    sin_numero = re.sub(patron, '', texto)
    return sin_numero


def eliminar_stepwords(t_neutro_total, nombre):
    """
    Elimina las StopWords una vez aplicados los filtros anteriores
    :param t_neutro_total: archivo texto
    :param nombre: Archivo sobre el que actúa
    :return: Devuelve el archivo filtrado
    """
    stw = abrir_archivo(nombre).split()
    text = t_neutro_total.split()
    for p in stw:
        for w in text:
            if p == w:
                text.remove(w)
    return text


def mostrar_eliminar_stopwords(texto, nombre):
    """
    Muestra y elimina las StopWords una vez aplicados los filtros anteriores
    :param texto: archivo texto
    :param nombre: Archivo sobre el que actúa
    :return: Devuelve el archivo filtrado
    """
    stw_encontrada = []
    stw = abrir_archivo(nombre).split()
    text = texto.split()
    for p in stw:
        for w in text:
            if p == w:
                text.remove(w)
                if w not in stw_encontrada:
                    stw_encontrada.append(w)
    print(f'\nLas stopwords encontradas en el texto son: \n\n{"-".join(stw_encontrada)}')
    return text


def numero_palabras(texto):
    """
    Cuenta el número de veces que sale cada palabra
    :param texto: Texto a analizar
    :return: Lista de tuplas con la palabra y el número de veces que se repite
    """
    lista = []
    for palabra in texto:
        cuenta = palabra, texto.count(palabra)
        lista.append(cuenta)
    return lista


def analisis(archivo_negativas, archivo_positivas, texto):
    """
    Esta función realizará el cálculo de las sumas palabras positiva mas la negativas. Para ello, llamará a
    2 funciones
    :param archivo_negativas: parametro que indica la ubicación del archivo de las palabras negativas
    :param archivo_positivas: parametro que indica la ubicación del archivo de las palabras positivas
    :param texto: Parametro con el archivo de trabajo
    :return: Devolverá el resultado de la suma de la dos funciones interiores
    """

    def negativo(archivo_neg, text):
        """
        Calcula el valor de las palabras negativas, para ello, carga el archivo con las estas palabras y las compara
        el texto neutro pasado en el parámetro texto
        :param archivo_neg: Parámetro con el nombre del archivo de la palabras negativas
        :param text: Parametro con el archivo de trabajo
        :return: Devolverá el resultado de la suma de las palabras con valor negativo
        """
        archivo_sw = open(archivo_neg, encoding="utf8")
        p_negativas = archivo_sw.read()
        p_negativas = p_negativas.split()
        result_negativo = 0
        for p in range(len(p_negativas)):
            for t in range(len(text)):
                if p % 2 == 0 and text[t][0] == p_negativas[p]:
                    result_negativo += float(text[t][1] * float(p_negativas[p + 1]))
        return result_negativo

    def positivo(archivo_pos, text):
        """
        Calcula el valor de las palabras positivas, para ello, carga el archivo con las estas palabras y las compara
        el texto neutro pasado en el parámetro texto
        :param archivo_pos: Parámetro con el nombre del archivo de las palabras positivas
        :param text: Parametro con el archivo de trabajo
        :return: Devolverá el resultado de la suma de las palabras con valor positivo
        """
        archivo_sw = open(archivo_pos, encoding="utf8")
        p_positivas = archivo_sw.read()
        p_positivas = p_positivas.split()
        result_positivas = 0
        for p in range(len(p_positivas)):
            for t in range(len(text)):
                if p % 2 == 0 and texto[t][0] == p_positivas[p]:
                    result_positivas += float(texto[t][1] * float(p_positivas[p + 1]))
        return result_positivas

    puntuacion_negativa = negativo(archivo_negativas, texto)    # Llamamos a la función y devuelve el resultado
    puntuacion_positiva = positivo(archivo_positivas, texto)    # Llamamos a la función y devuelve el resultado
    return puntuacion_positiva + puntuacion_negativa
