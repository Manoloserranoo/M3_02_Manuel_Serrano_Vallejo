lista = [4, 7, 30, 23, 5]
def numero_lista(numero):
  try:
    lista[numero]
  except IndexError:
    print("No se encuentra en el rango de la lista")
  else:
    print("Se encuentra en el rango de la lista")
    return
numero_lista(10)
numero_lista(3)