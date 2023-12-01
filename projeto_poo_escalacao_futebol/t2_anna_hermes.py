# ANNA CAROLINA HERMES - TRABALHO FINAL

class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False # ou True

    def get_numero(self):
        return self.__numero

    def set_numero(self, x):
        self.__numero = x

    def get_nome(self):
        return self.__nome_jogador

    def set_nome(self, x):
        self.__nome_jogador = x

    def get_posicao(self):
        return self.__posicao

    def set_posicao(self, x):
        self.__posicao = x
    
    def get_situacao(self):
        return self.__situacao

    def set_situacao(self, x):
        self.__situacao = x
    
    def get_participacao(self):
        return self.__participou_partida

    def set_participacao(self, x):
        self.__participou_partida = x


def ler_arquivo():
    try:
        arquivo = open("convocados.txt", "r",  encoding='utf-8')
    except:
        print("Arquivo inexistente")
        return

    for linha in arquivo:
        numero, nome, posicao = linha.strip().split(':')
        convocado = Jogador(nome, numero, posicao)
        lista_jogadores.append(convocado)

    arquivo.close()


def ler_jogadores():
    print("""\nJOGADORES CONVOCADOS
********************""")
    for jogador in lista_jogadores:
        print(f"{jogador.get_numero()}. {jogador.get_nome()} - {jogador.get_posicao()}")


def escalar_goleiro():
    print("""\nGOLEIROS CONVOCADOS
********************""")
    for pos, jogador in enumerate(lista_jogadores):
        if jogador.get_posicao() == 'GOLEIRO':
            print(f"{jogador.get_numero()}. {jogador.get_nome()} - {jogador.get_posicao()}")


    escolha_goleiro = input("\nDigite o número do goleiro escolhido: ")
    for pos, jogador in enumerate(lista_jogadores):
        if escolha_goleiro == jogador.get_numero() and jogador.get_posicao() == 'GOLEIRO':
            lista_escalados.append(jogador)
            jogador.set_participacao(True)
            lista_jogadores[pos] = jogador

def escalar_jogadores():
    for cont in range(10):
        print("""\nJOGADORES CONVOCADOS
********************""")
        for pos, jogador in enumerate(lista_jogadores):
            if jogador.get_posicao() != 'GOLEIRO' and jogador.get_participacao() == False:
                print(f"{jogador.get_numero()}. {jogador.get_nome()} - {jogador.get_posicao()}")

        escolha_jogador = input("\nDigite o número do jogador escolhido: ")
        for pos, jogador in enumerate(lista_jogadores):
            if escolha_jogador == jogador.get_numero():
                if jogador.get_posicao() != 'GOLEIRO':
                    lista_escalados.append(jogador)
                    jogador.set_participacao(True)
                    lista_jogadores[pos] = jogador


def reserva():
    for jogador in lista_jogadores:
        escalado = False
        for jogador_escalado in lista_escalados:
            if jogador.get_numero() == jogador_escalado.get_numero():
                escalado = True
                break
        if not escalado:
            lista_reserva.append(jogador)


def substituicao():
    print("""\nSUBSTITUIÇÃO
********************
Disponíveis para substituição:""")
    for jogador in lista_reserva:
        print(f"{jogador.get_numero()}. {jogador.get_nome()} - {jogador.get_posicao()}")

    quem_entra = input("Digite o número do jogador que entrará em campo: ")
    for pos, jogador in enumerate(lista_reserva):
        if quem_entra == jogador.get_numero():
            lista_reserva.remove(jogador)
            lista_escalados.append(jogador)
            jogador.set_participacao(True)
            print(f"{jogador.get_nome()} entra em campo")

    print("""\nSUBSTITUIÇÃO
********************
Jogadores em campo:""")
    for jogador in lista_escalados:
        print(f"{jogador.get_numero()}. {jogador.get_nome()} - {jogador.get_posicao()}")

    quem_sai = input("Digite o número do jogador que sairá de campo: ")
    for jogador in lista_escalados:
        if quem_sai == jogador.get_numero():
            lista_escalados.remove(jogador)
            lista_reserva.append(jogador)
            jogador.set_participacao(True)
            print(f"{jogador.get_nome()} sai de campo")


def expulsao():
    print("""\nEXPULSÃO
********************""")

    for jogador in lista_escalados:
        print(f"{jogador.get_numero()}. {jogador.get_nome()} - {jogador.get_posicao()}")

    expulso = input("Digite o número do jogador expulso: ")
    for pos, jogador in enumerate(lista_jogadores):
        if expulso == jogador.get_numero():
            for escalado in lista_escalados:
                if expulso == escalado.get_numero:
                    lista_escalados.remove(jogador)
                    lista_reserva.append(jogador)
                    jogador.set_participacao(True)
                    jogador.set_situacao("EXPULSO")
                    lista_jogadores[pos] = jogador


def escalacao():
    print("""\nESCALAÇÃO DA PARTIDA
********************""")

    for jogador in lista_jogadores:
        if jogador.get_participacao():
            grava_escalacao(jogador.get_numero(), jogador.get_nome(), jogador.get_posicao())
            print(f"{jogador.get_numero()}. {jogador.get_nome()} - {jogador.get_posicao()}")


def grava_escalacao(numero, nome, posicao):
    try:
        arquivo = open("todosjogadores.txt", "a")
    except:
        arquivo = open("todosjogadores.txt", "w")

    arquivo.write(str(numero) + ":" + nome + ":" + posicao + "\n")
    arquivo.close()


def main():
    while True:
        escolha = input("""
MENU
======
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir Escalação
Escolha: 
""")
        if escolha == '1': 
            ler_arquivo()
            ler_jogadores()
        if escolha == '2':
            escalar_goleiro()
            escalar_jogadores()
            reserva()
        if escolha == '3':
            substituicao()
        if escolha == '4':
            expulsao()
        if escolha == '5':
            escalacao()
        if escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4" and escolha != "5":
            print("Comando Inválido!")


lista_jogadores = []
lista_escalados = []
lista_reserva = []

main()
