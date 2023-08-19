'''
César Alberto Bravo Pariente
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, 
no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

Trabalhe esse código em seu IDE, 
suba ele para sua conta no GitHub e 
compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

'''

anoCorreto = False

while (anoCorreto == False):
  print("Insira seu nome")
  nome = input()
  print("Insira seu ano de nascimento")
  ano = int(input())
  
  try:
     if ( (ano>=1922) and (ano<=2021) ):
         anoCorreto = True
         print("Seu nome é: ", nome)
         print("Sua idade é: ", (2022-ano) )
     else:
         print("Você digitou um ano menor que 1922 o maior que 2021")
  except:
    print("Ano inválido, por favor digite um ano entre 1921 e 2021!")
