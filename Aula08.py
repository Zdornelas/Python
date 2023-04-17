#Aula 08 - Lista,Tuplas e Dicionários

#Identificador de nome e uma lista de nomes
nomes = ["Messias", "Emanuel", "Miguel", "João"]
print (nomes)

# Verificar o tipo de dado
print (type (nomes))

#Acessando  um elemento da lista
nomes [0]

#Tamnho da lista
print(len(nomes))

#Imprimindo cada item da lista
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])

#Lista de frutas
frutas = ["pêras", "uva", "maça", "kiwi"]
print(frutas)

#Alternado o elemento que está na posição 1
frutas[1] = "abacate"
print (frutas)

#insert
frutas.insert (2, "morango")
print(frutas)

#del (delete)
frutas.insert (5, "chuchu") #Não é fruta
print(frutas)
del frutas[5]
print(frutas)

#index
frutas.insert (5, "chuchu") #Não é fruta
print(frutas)
indice_fruta = frutas.index ("chuchu")
del frutas[indice_fruta]
print (frutas)


