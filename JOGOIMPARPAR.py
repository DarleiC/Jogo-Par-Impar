from random import randint, choice
from time import sleep
computer = c = 0
command = p = 0
while True:
    print('\033[7m+\033[m' * 40)
    print('Score: MÁQUINA= {} \n        HUMANO= {}'.format(c,p))
    print('\033[7m+\033[m' * 40)
    quer = int(input('\n \033[31;43m- Quer jogar PAR ou IMPAR?\033[m \033[4;7m1=SIM 2=Não\033[m \n='))
    if quer == 1:
        pc = randint(0, 100)
        #print(pc)
        qual = (['PAR', 'IMPAR'])
        d = choice(qual)
        print(' ')
        print('Eu decido e escolho:\n {}\n'.format(d))
        humano = int(input('Humano, Informe um valor: '))
        print('Escolho o número: {}'.format(pc))
        print(' ')
        print(' Vamos ver quem ganhou. Contando..')
        sleep(3)
        print(' ')
        soma = humano + pc
        resto = soma % 2
        if resto == 1 and d == 'IMPAR':
            print('=== MÁQUINA GANHOU PORQUE {} É IMPAR\n'.format(soma))
            c += 1
        elif resto == 0 and d == 'PAR':
            print('=== MÁQUINA GANHOU PORQUE {} É PAR\n'.format(soma))
            c += 1
        elif resto == 0 and d == 'IMPAR':
            print('>>> HUMANO GANHOU PORQUE {} É PAR\n'.format(soma))
            p += 1
        elif resto == 1 and d == 'PAR':
            print('>>> HUMANO GANHOU PORQUE {} É IMPAR\n'.format(soma))
            p += 1
    elif quer == 2:
        if c > p:
            print('>>>>>+++++ E o campeão foi a MÁQUINA com {} pontos!'.format(c))
        elif c == p:
            print('>>>>>> Isso foi um Empate!')
        else:
            print('>>>>>+++++ E o campeão foi o HUMANO com {} pontos!'.format(p))
        break    
    else:
        print('Score: MÁQUINA= {} HUMANO= {}'.format(c,p))
        #print('Score: MÁQUINA= ' + str(c) + ' HUMANO= ' + str(p))
        print(' ')  
print(' ')
