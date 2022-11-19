def operacion(a,b):
  try:
    resultado = a/b
  except ZeroDivisionError:
    print("No se puede dividir por cero")
  else:
    print(resultado)
  return
operacion(7,0)
operacion(7,1)