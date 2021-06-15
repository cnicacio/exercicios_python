''' 
01 -Escreva um programa que pede a 
senha do usuário e só sai do looping 
quando digitarem corretamente a senha
'''

usuario = str(input('Digite seu usuário: '))
senha = str(input('Digite sua senha: '))

while senha != 'carlitos1994':
    senha = str(input('Senha incorreta. Digite novamente: '))

print('Login efetuado com sucesso')

''' 
02 - Faça um programa que leia o sexo biológico 
de uma pessoa, mas só aceite os valores 'M' ou
'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto
'''

nome = str(input('Digite seu nome: '))
sexo_bio = str(input('Informe seu sexo biológico [F/M]: ').strip().upper()[0])

while sexo_bio != 'F' and sexo_bio != 'M':
    sexo_bio = input('Valor inválido! Informe seu sexo biológico: ').strip().upper()[0]
    if sexo_bio == 'F':
        print(f'Olá, {nome}, seu sexo biológico é feminino')
    elif sexo_bio == 'M':
        print(f'Olá, {nome}, seu sexo biológico é masculino')

'''
03- Crie um jogo onde o computador vai "pensar"
em um número entre o 0 e 10. O jogador vai
tentar adivinhar qual número foi escolhido até
acertar, entre os palpites diga ao jogador
se o número do computador é maior ou menor do
que ele digitou e no final mostre os palpítes
necessários para vencer o jogo
'''

from random import randint

n1 = randint(1, 10)
n2 = int(input('Digite um número de 1 a 10: '))
palpites = 0

while n2 > 10 or n2 <= 0:
    n2 = int(input('Valor inválido! Digite um número de 1 a 10: '))

while n2 != n1:
    if n2 < n1:
        n1 = randint(1, 10)
        palpites += 1
        n2 = int(input('Número incorreto! Tente um número maior: '))
    elif n2 > n1:
        n1 = randint(1, 10)
        palpites += 1
        n2 = int(input('Número incorreto! Tente um número menor: '))

palpites += 1
print(f'Parabéns! Você acertou após {palpites} tentativas.')
'''
04 - Faça um programa que jogue par ou
ímpar com o computador. O jogo só será interrompido
quando o jogador perder, postrando o total de vitórias
consecutivas que ele conquistou até o final do jogo
'''

from random import randint

vitorias = 0

while True:
    jogador = int(input('Diga um número de 0 a 10: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: ').strip().upper()[0])
    print(f'Você jogou {jogador} e o computador jogou {computador}, o total foi {total}')
    
    if escolha == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break

    if escolha == 'I':
        if total % 2 != 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')

print(f'GAME OVER... Você venceu {vitorias} vezes!')
