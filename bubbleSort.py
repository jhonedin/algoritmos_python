"""
Descripción del algoritmo:

La Ordenación de burbuja (Bubble Sort en inglés) es un sencillo algoritmo de ordenamiento. 
Funciona revisando cada elemento de la lista que va a ser ordenada con el siguiente, 
intercambiándolos de posición si están en el orden equivocado. 
Es necesario revisar varias veces toda la lista hasta que no se necesiten más intercambios, 
lo cual significa que la lista está ordenada. 
Este algoritmo obtiene su nombre de la forma con la que suben por la lista los elementos durante los intercambios, 
como si fueran pequeñas "burbujas". 
También es conocido como el método del intercambio directo. 
Dado que solo usa comparaciones para operar elementos, 
se lo considera un algoritmo de comparación, 
siendo uno de los más sencillos de implementar.

Fuente: https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja

"""


def bubble_sort(a_list):
    # Ciclo que permite recorrer toda la lista
    for i in range(0,len(a_list)):
        # Ciclo que permite ir comparando cada elemento de la lista
        for j in range(0,len(a_list)-i-1):
            # Se compara dos elementos adyacentes
            if a_list[j] > a_list[j+1]:
                aux = a_list[j]
                # se intercambia los elementos si no estan en el orden esperado
                a_list[j] = a_list[j+1]
                a_list[j+1] = aux
    return a_list

unordered_list = [5,7,9,11,15,1,8]
print("unordered list: ",unordered_list)
ordered_list = bubble_sort(unordered_list)
print("ordered list: ", ordered_list)

"""
Prueba:
unordered list:  [5, 7, 9, 11, 15, 1, 8]
ordered list:  [1, 5, 7, 8, 9, 11, 15]

"""