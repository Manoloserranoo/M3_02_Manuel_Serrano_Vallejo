lista = [4, 7, 30, 23, 5]
def numero_lista(numero):
  try:
    lista[numero]#
  except IndexError:#Usamos IndexError para saber si la posición que solicitamos existe en la lista.
    print("El número está en el intervalo de la lista")
  else:
    print("El número no está en el intervalo de la lista")#Si se pide imprimir una posición de la cual no dispinemos en la lista imprimiremos el mensaje.
    return
#Damos dos valores para buscar
numero_lista(10)
numero_lista(40)