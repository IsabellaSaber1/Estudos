def checaridade():
  nome = input ("Digite seu nome: ")
  idade = input ("Digite sua idade: ")

  idade = int(idade)
  if idade >= 18:
    print (f"{nome}, você é maior de idade.")
  else:
    print (f"{nome}, você é menor de idade.")

def maior_menor():
  numeros = [] #creating a list to store the numbers
  nummaior = 0
  nummenor = 1000
  for i in range(5): #repetir 5 vezes
    num = int(input("Digite um número: ")) #pedir um número ao usuário
    numeros.append(num) #adicionar o número à lista
  soma = sum(numeros) #calcular a soma dos números na lista
  print(f"A soma dos números é: {soma}") #mostrar a soma
  for i in range(5):
    if numeros[i] > nummaior:
        nummaior = numeros[i]
  print(f"O maior número é: {nummaior}")
  for i in range(5):
    if numeros[i] < nummenor:
        nummenor = numeros[i]
  print(f"O menor número é: {nummenor}")

if __name__ == "__main__":
  opcao = input ("Escolha a função de 1 a 2:")
  if opcao == "1":
        checaridade()
  elif opcao == "2":
        maior_menor()
    
                