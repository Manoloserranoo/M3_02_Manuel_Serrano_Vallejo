def operacion(num):
  try:
    resultado = num +10
  except TypeError:#En caso de que el valor introducido no sea un número imprimimos un error.
    print("No es correcto ")
  else:
    print("El resultado de la operacción es:", resultado)
  return
#Damos dos valores, un valor numerico y un string.
if __name__=="__main__":
  operacion("2")
  operacion(2)