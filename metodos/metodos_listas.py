lista = list ([1972,27,11,True]) #elimine hola y gustavo
#nos devuelve la longitud de la lista(cantidad de caracteres)
cadena = "hola"
resultado = len(lista)
#agregando un elemento a la lista
lista.append(4)
#agregando un elemento en una posicion especifica
lista.insert(2, False)
#agregando varios elementos a lista 
lista.extend([1972])
#eliminando un elemento de la lista 
print(len(lista))
lista.pop(0)
print(len(lista))
lista.pop(-1)
#eliminando un elemento de la lista por su valor
lista.sort()
#lista.remove("sagitario")
print(lista)
lista.sort(reverse=True)
#verificando si un elemento se encuentra en la lista 
elemento_encontrado = lista.index(4)


print(elemento_encontrado)
