cadena1 = "Hola,soy,gustavo,santacruz"
cadena2 = "gracias por aprender python con nosotros"
#print(dir(cadena1))

resultado = cadena1.lower() #convierte el texto en miniculas
print(resultado)

primera_letra_mayus = cadena1.capitalize()
print(primera_letra_mayus)

busqueda_find = cadena1.find("z")
print(busqueda_find)

#busqueda_index = cadena1.index("a")
#print(busqueda_index)

es_numerico = cadena1.isnumeric()
print(es_numerico)

es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

contar_coincidencias = cadena1.count("a")
print(contar_coincidencias)

contar_caracteres = len(cadena1)
print(contar_caracteres)

empieza_con = cadena1.startswith("H")
print(empieza_con)
termina_con = cadena1.endswith("o")
print(termina_con)

cadena_nueva = cadena1.replace("soy", "yo me llamo")
print(cadena_nueva)

cadena_separada = cadena1.split(",")
print(cadena_separada)
print(type(cadena_separada))
print(cadena_separada[0])
