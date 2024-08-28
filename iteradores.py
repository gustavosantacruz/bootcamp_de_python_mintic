# ejemplo de como funcionan los iteradores
#crear una lista con algunos numeros 
my_list = [1,2,3,4]
#obtener el iterador de la lista
#uni iterador es un objeto que nos permite rrecorrer una coleccion(como una lista9uno por uno)
my_iter = iter(my_list)
#usar el iterador para acceder a los elementos de la lista 
#la funcion next () nos da el sguiente elemento en la coleccion cada vez que se llama
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))
#iterar cadenas de texto usando un iterador 
#crear cadena de texto
text = "hola mundo"
#crear un iterador para la cadena
#un iterador nos permite recorrer cada caracter de la cadena uno por uno 
iter_text = iter(text)
#iterar sobre cada caracter de la cadena usando bucle for
for char in iter_text:
    print(char)
#crear un itirador que genere numeros impares desde 1 hasta el limite
#range(1, limit+1, 2)genera numeros comenzando en 1,  con saltos de 2, hasta llegar a 9 (el limite no se incluye)
odd_iter = iter(range(1,10,2))
#mostrar el iterador para recorrer y mostrar cada numero impar generado
for num in odd_iter:
    print(num)
#definir una funcion generadora
def my_generator():
    #la palabra clave yield no permite devolver un valor y pausar la funcion en ese punto
    yield 1 #primer valor que se devuelve cunado se llama la funcion  
    yield 2 #primer valor que se devuelve cunado se llama la funcion 
    yield 3 #primer valor que se devuelve cunado se llama la funcion 
#usar un bucle for para iterar sobre los valores generados 
for value in my_generator():
    print(value)
#fibonacci
#la serie de fibonacci hace referencia a que vamios a obtener un valor sumando los dos anteriores
#los dos anteriores [0 1 1 2 3 5 8 13... ]
def fibonacci(limit):
    #inicializar los dos primeros numeros de la secuencia fibonacci
    a, b = 0, 1.
    #continuar generano numeros mientras "a" sea menor ue el limite
    while a < limit:
        yield a #devolver el valor actual de a y pausar la ejecucion de la funcion
        a,b, = b, a + b
    for num in fibonacci(10):
        print(num)
        

    