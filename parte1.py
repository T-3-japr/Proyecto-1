from funciones import mis_funciones as mf


archivo_parte_1 = 'Datos/articulo.txt'
archivo_stw = 'Datos/stopwords_español.txt'
patron = '[A-Z][a-z]+'
patron2 = '[A-Z][A-Z]+'
patron3 = '\W+'
patron4 = '[áéíóú]'
patron5 = '[0-9]+'

texto = mf.abrir_archivo(archivo_parte_1)
print(f'\nEl texto contiene {mf.contar_palabras(texto)} palabras')
print(f'\nLas palabras que empiezan por mayúscula son: \n{", ".join(mf.mayusculas(patron, texto))}')
print(f'\nLas palabras que empiezan por mayúscula son: \n{", ".join(mf.mayusculas(patron2, texto))}')
texto_min = mf.minusculas(texto)
print(f'\nEl texto en minúsculas queda: \n{texto_min}')
print(f'\nLos signos de puntuación son: \n{", ".join(mf.mayusculas(patron3, texto_min))}')
texto_s_punt = mf.e_punt(patron3, texto_min)
print(f'\nEl texto solo con espacios queda: \n{texto_s_punt}')
print(f'\nLas letras con acento que aparecen son: \n{", ".join(mf.mayusculas(patron4, texto_s_punt))}')
t_neutro = mf.elimina_acentos(texto_s_punt)
print(f'\nEl texto sin acentos queda: \n{t_neutro}')
t_neutro_total = mf.eliminar_numeros(patron5, t_neutro)
print(f'\nEl texto sin números queda: \n{t_neutro_total}')
texto_final = mf.eliminar_stepwords(t_neutro_total, archivo_stw)
print(f'\nUna vez eliminadas las StopWords, el texto queda: \n{" ".join(texto_final)}')
