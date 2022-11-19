paises = {"España":"Español", "EEUU":"Inglés","Italia":"Italiano"}
def encontrar(pais):
  try:
    paises[pais]
  except KeyError:
    print("El país no se encuentra dentro del diccionario")
  else:
    print("El país se encuentra dentro del diccionario")
  return
if __name__ == "__main__":
  print(encontrar("Alemania"))
  print(encontrar("Italia"))
  
