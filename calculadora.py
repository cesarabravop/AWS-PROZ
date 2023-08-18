'''
César Alberto Bravo Pariente
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. 
Depois precisa executar a operação e mostrar o resultado na tela. 
Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

Trabalhe esse código em seu IDE, 
suba ele para sua conta no GitHub e 
compartilhe o link desse projeto no campo ao lado 
para que outros desenvolvedores possam analisá-lo.

'''
opcao = '9'
while (opcao != "0"):
    print ('1: Soma')
    print ('2: Subtração')
    print ('3: Multiplicação')
    print ('4: Divisão')
    print ('0: Sair')
    print ('')
    opcao = input('Digite o número para a operação correspondente: ')
    if (opcao == '0'): 
        break
    elif (opcao == '1'): 
        num1 = float(input('inserir o primeiro valor: '))
        num2 = float(input('inserir o segundo valor:: '))
        res = num1 + num2
        print ('O resultado da soma de ', num1, ' com ', num2, ' é :', res)
        print ('')
    elif (opcao == '2'): 
        num1 = float(input('inserir o primeiro valor: '))
        num2 = float(input('inserir o segundo valor:: '))
        res = num1 - num2
        print ('O resultado da subtração de ', num1, ' com ', num2, ' é :', res)
        print ('')
    elif (opcao == '3'): 
        num1 = float(input('inserir o primeiro valor: '))
        num2 = float(input('inserir o segundo valor:: '))
        res = num1 * num2
        print ('O resultado da multiplicação de ', num1, ' com ', num2, ' é :', res)
        print ('')
    elif (opcao == '4'): 
        num1 = float(input('inserir o primeiro valor: '))
        num2 = float(input('inserir o segundo valor:: '))
        if (num2 == 0.0):
            print ('Não é possível dividir por zero')
        else:
            res = num1 / num2
            print ('O resultado da divisão de ', num1, ' com ', num2, ' é :', res)
            print ('')
    else:
        print ('Essa opção não existe')
        print ('')
