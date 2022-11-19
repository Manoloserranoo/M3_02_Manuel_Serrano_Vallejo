def operacion(num):
  try:
    resultado = num +10
  except TypeError:
    print("No es correcto ")
  else:
    print("El nuevo resultado es:", resultado)
  return
operacion("Hola")
operacion(7)
operacion(2)