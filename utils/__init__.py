def clear():
    from os import system, name
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def lerint(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except:
            clear()
            menu('ESTATÍSTICAS GERAIS')                  
            print(f"Partidas jogadas: {contjogadas}")
            print(f"Partidas que o jogador venceu: {contvitorias}")
            print(f"Partidas que o computador venceu: {contderrotas}")
            print(f"Partidas empatadas: {contempates}")
        else:
            return inteiro


def lermenu1(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except:
            clear()
            menu('JOKENPÔ', '-=', 10, 20)
        else:
            return inteiro


def lermenu2(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except:
            clear()
            menu('Vamos jogar JOKENPÔ!', '-=', 15, 30)
        else:
            return inteiro


def lermenu3(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except:
            clear()
            menu('ESTATÍSTICAS', '-', 20, 20)
        else:
            return inteiro


def menu(msg, linha='', tamanholinha=0, center=0):
    print(f'{linha}' * tamanholinha)
    print(f'{msg}'.center(center))
    print(f'{linha}' * tamanholinha)


def verificacao():
    global contjogadas, contvitorias, contderrotas, contempates
    contjogadas = contvitorias = contderrotas = contempates = 0
    from random import randint
    from time import sleep
    while True:
        computador = randint(1, 3)
        menu('Vamos jogar JOKENPÔ!', '-=', 15, 30)
        global jogador
        jogador = lermenu2(f"Suas opções\n[ 1 ]PEDRA\n[ 2 ]PAPEL\n[ 3 ]TESOURA\n[ 0 ]Voltar para o menu principal\nQual sua jogada? ")
        clear()
        if jogador == 0:
            break
        elif jogador == 1:
            contjogadas += 1
            print("Jogador jogou PEDRA")
            if computador == 1:
                print("Computador jogou PEDRA")
                print("EMPATE!")
                contempates += 1
                sleep(1.5)
            elif computador == 2:
                print("Computador jogou PAPEL")
                print("Jogador PERDEU!")
                contderrotas += 1
                sleep(1.5)
            else:
                print("Computador jogou TESOURA")
                print("Jogador VENCEU!")
                contvitorias += 1
                sleep(1.5)
        elif jogador == 2:
            contjogadas += 1
            print("Jogador jogou PAPEL")
            if computador == 1:
                print("Computador jogou PEDRA")
                print("Jogador VENCEU!")
                contvitorias += 1
                sleep(1.5)
            elif computador == 2:
                print("Computador jogou PAPEL")
                print("EMPATE!")
                contempates += 1
                sleep(1.5)
            else:
                print("Computador jogou TESOURA")
                print("Jogador PERDEU!")
                contderrotas += 1
                sleep(1.5)
        elif jogador == 3:
            contjogadas += 1
            print("Jogador jogou TESOURA")
            if computador == 1:
                print("Computador jogou PEDRA")
                print("Jogador PERDEU!")
                contderrotas += 1
                sleep(1.5)
            elif computador == 2:
                print("Computador jogou PAPEL")
                print("Jogador VENCEU!")
                contvitorias += 1
                sleep(1.5)
            else:
                print("Computador jogou TESOURA")
                print("EMPATE!")
                contempates += 1
                sleep(1.5)
        arquivoleitura()


def estatisticasgerais():
    global contjogadas, contvitorias, contderrotas, contempates
    while True:
        menu('ESTATÍSTICAS', '-', 20, 20)
        op = lermenu3("[ 1 ]ESTATÍSTICAS GERAIS\n[ 2 ]ESTATÍSTICAS DE TODO O TEMPO\n[ 3 ]LIMPAR DADOS\n[ 0 ]VOLTAR\nSua escolha: ")
        if op == 0:
            break
        elif op == 1:
            while True:
                clear()
                menu('ESTATÍSTICAS GERAIS')                  
                print(f"Partidas jogadas: {contjogadas}")
                print(f"Partidas que o jogador venceu: {contvitorias}")
                print(f"Partidas que o computador venceu: {contderrotas}")
                print(f"Partidas empatadas: {contempates}")
                op = lerint("\nDigite 0 para voltar: ")
                if op == 0:
                    clear()
                    break
                else:
                    continue
        elif op == 2:
            estatisticastodotempo()
        elif op == 3:
            clear()
            contjogadas = contvitorias = contderrotas = contempates = 0
            break
        else:
            clear()
            continue


def estatisticastodotempo():
    arquivoleitura()


def arquivoleitura():
    with open('stats.txt', 'w') as arquivo:
        arquivo.write(f'''Partidas jogadas: {contjogadas}
Partidas que o jogador venceu: {contvitorias}
Partidas que o computador venceu: {contderrotas}
Partidas empatadas: {contempates}''')



def programaprincipal():
    global contjogadas, contvitorias, contderrotas, contempates
    contjogadas = contvitorias = contderrotas = contempates = 0
    while True:
        clear()
        if contjogadas == 0:
            menu('JOKENPÔ', '-=', 10, 20)
            escolha = lermenu1("[ 1 ]NOVO JOGO\n[ 0 ]SAIR\nSua escolha: ")
            if escolha == 0:
                break
            elif escolha == 1:
                clear()
                verificacao()
        else:
            menu('JOKENPÔ', '-=', 10, 20)
            escolha = lermenu1("[ 1 ]NOVO JOGO\n[ 2 ]ESTATÍSTICAS\n[ 0 ]SAIR\nSua escolha: ")
            if escolha == 0:
                break
            elif escolha == 1:
                clear()
                verificacao()
            elif escolha == 2:
                clear()
                estatisticasgerais()
