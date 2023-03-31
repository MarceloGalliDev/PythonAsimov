#----------------------
# Funções decorativas
def somaUm(numero):
  return numero + 1

f1 = somaUm
f1(1)

#-----------------------
# Funções decorativas dentro de outra função decorativa
def somaDois(numero):
  def adicionar(numero):
    return numero + 2
  return adicionar(numero)

somaDois(4)

#-----------------------
# Passando funções comom argumentos em outras funções
def somaUm(numero):
  return numero + 1

def functionCall(function):
  numeroToAdd = 5
  return function(numeroToAdd)

#------------------------
# Retornando funções em funções
def diga_ola():
  def diga_oi():
    return "Hi"
  return diga_oi
hello = diga_ola()
hello()

#------------------------
#Exemplos
def decorador_functions(function):
  def wrapper():
    func = function()
    cria_maisculo = func.upper()
    return cria_maisculo
  return wrapper

def diga_ola():
  return "hello there"

funcao_decorada = decorador_functions(diga_ola)
funcao_decorada()

#é a mesma coisa que:

@decorador_functions
def diga_ola():
  return "hello there"
diga_ola()