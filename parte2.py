from funciones import mis_funciones as mf

archivo_parte_2 = 'Datos/sentweets_esp.txt'
archivo_stw = 'Datos/stopwords_español.txt'
archivo_negativas = 'Datos/negative_lex.txt'
archivo_positivas = 'Datos/positive_lex.txt'
patron_url = 'http[s]?://[a-z]+.[a-z]+/[a-zA-Z0-9]+'
patron_usuario = '@[a-zA-Z0-9]+|#[a-zA-Z0-9]+'
patron_s_puntuacion = '\W+|[_]+'
patron_mayuscula = '[A-Z][a-z]+'
patron_siglas = '[A-Z][A-Z]+'
patron_acentos = '[áéíóú]'
patron5 = '[0-9]+'

texto_parte_2 = mf.abrir_archivo(archivo_parte_2)
print(f'\nEl texto con el que vamos ha hacer la segunda parte del proyecto es: \n\n{texto_parte_2}')
texto_sin_url = mf.e_punt(patron_url, texto_parte_2)
print(f'\nEl texto sin las url queda de la siguiente forma: \n\n{texto_sin_url}')
texto_sin_usuario = mf.e_punt(patron_usuario, texto_sin_url)
print(f'\nEl texto sin las referencias a usuario queda de la siguiente forma: \n\n{texto_sin_usuario}')
texto_sin_puntuacion = mf.e_punt(patron_s_puntuacion, texto_sin_usuario)
print(f'\nEl texto sin signos de puntuación, queda: \n\n{texto_sin_puntuacion}')
texto_sin_numero = mf.eliminar_numeros(patron5, texto_sin_puntuacion)
print(f'\nEl texto sin números queda: \n\n{texto_sin_numero}')
texto_mayuscula = mf.mayusculas(patron_mayuscula, texto_sin_numero)
print(f'\nLas palabras del texto que empiezan por mayúsculas son: \n\n{", ".join(texto_mayuscula)}')
print(f'\nLas siglas que aparecen en el texto son: \n\n{"-". join(mf.mayusculas(patron_siglas, texto_sin_numero))}')
print(f'\nLas texto sin siglas queda: \n\n{mf.e_punt(patron_siglas, texto_sin_numero)}')
texto_minusculas = mf.minusculas(texto_sin_numero)
print(f'\nEl texto con todas las letras en minúscula queda: \n\n{texto_minusculas}')
acentos_texto = mf.mayusculas(patron_acentos, texto_minusculas)
print(f'\nLas letras acentuadas son: \n\n{acentos_texto}')
texto_sin_stw = mf.mostrar_eliminar_stopwords(texto_minusculas, archivo_stw)
print(f'\nEl texto sin Stopwords queda: \n\n{" ".join(texto_sin_stw)}')
parejas = mf.numero_palabras(texto_sin_stw)
print(f'\nEl número de veces que aparece cada palabra es de: \n\n{parejas}')
r = mf.analisis(archivo_negativas, archivo_positivas, parejas)
if r > 0:
    print(f'\nEl valor del texto con una puntuación de {round(r, 2)}, es positivo')
elif r < 0:
    print(f'\nEl valor del texto con una puntuación de {round(r, 2)}, es negativo')
else:
    print(f'\nEl valor del texto con una puntuación de {r}, es neutro')
