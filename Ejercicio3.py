paises = {"España":"Español", "EEUU":"Inglés","Italia":"Italiano"}
def encontrar(pais):
  try:
    paises[pais]
  except KeyError:#Este salta cuando intentamos acceder a un valor que no se encuentra en el diccionario.
    print("El país no se encuentra dentro del diccionario")
  else:
    print("El país se encuentra dentro del diccionario")#Si el país no pertenece al diccionario 
  return
if __name__ == "__main__":
  #Buscamos dos valores en el diccinario
  print(encontrar("Alemania"))
  print(encontrar("Italia"))
  
