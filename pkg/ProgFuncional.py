__author__ = 'ddizoya'
'bhernandezsouto'

def saudar(ling):

  def saudar_es():
      print("hola")
  def saudar_gl():
      print("ola")
  def saudar_en():
      print("Hello")
  def saudar_fr():
      print("salut")

  ling_func = {
      'es':saudar_es,
      'gl':saudar_gl,
      'en':saudar_en,
      'fr':saudar_fr
  }
  return ling_func[ling]

print (saudar('en'))
f = saudar('es')
saudar('fr')()
f()

#Interacciones sobre listas de orden superior
lista = [2,4,6,8]

print("Cuadrados + mapeados: ")
def cuadrado(n):
    return n**2

lista2 = map (cuadrado,lista)

for elemento in lista2:
    print(elemento)




print("\nIncrementos + mapeado: ")

def incrementa(n):
    return n+1;

lista3 = map(incrementa,lista)

for elemento in lista3:
    print(elemento)





print("\nFiltrado cuando devuelve true:")

def e_par(n):
    return (n%2.0 ==0)

lista4 = filter(e_par,lista)

for elemento in lista4:
    print(elemento)




print("Lambda; funcion anonima e instantanea. + filtrado de true")

lista5 = filter (lambda n: n%2.0 ==0 , lista)

for elemento in lista5:
    print(elemento)