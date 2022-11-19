def operacion(a,b):
  try:
    op = a/b #definimos la operación a realizar
  except ZeroDivisionError:#Usamos ZeroDivisionError para que nos salte un mensaje cuando se divida entre cero ya que no se puede.
    print("No se puede dividir un número entre cero")
  else:
    print("El resultado de dividir",{a},"y",{b},"es:",op.format)#Si no se divide entre cero imprimimos el resultado de la operación propuesta
  return
#Damos varios valores a "a" y "b" para hacer varias pruebas  
operacion(7,0)
operacion(8,2)