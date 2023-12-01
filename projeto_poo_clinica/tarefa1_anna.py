#
# Tarefa 1
# Competências avaliadas:
# - Saber interpretar o que foi solicitado
# - Desenvolver uma solução viável para o problema
# - Saber utilizar classes e objetos

'''
Faça um algoritmo que controle o acesso de pessoas a
um estabelecimento comercial.

Para isso você deverá utilizar as seguintes classes:

Crie uma classe Profissional com os atributos:
        - nome
        - especialidade
        - sala
    Todos atributos devem ser privados e string.

crie uma classe Visitante com os atributos:
        - nome
        - documento
    Todos atributos devem ser privados e string.

crie a classe Visita com os atributos:
        - visitante
        - profissional
        - data_visita
    O atributo visitante deverá ser um objeto da
        classe Visitante escolhido de lista_visitantes.
    O atributo profissional deverá ser um objeto da
        classe Profissional escolhido de lista_profissionais.

Crie os métodos que forem necessários para acessar os
atributos das classes.


Desenvolva seu código a partir do menu abaixo:

======================
MENU
======================
1- Cadastrar Profissional
2- Localizar Profissional
3- Cadastrar Visitante
4- Registrar Visita
5- Relatório de Conferência
Escolha:


Na opção 1 do menu cadastre o nome, especialidade e sala
    onde o profissional atende. Armazene esses dados em
    lista_Profissionais (como objetos).

Na opção 2 do menu é possível localizar um profissional
    pelo nome ou pela profissão. Isso serve para o caso
    do visitante não saber a sala do profissional.
    (Apenas mostrar na tela o nome e a sala do profissional)

Na opção 3 do menu será cadastrado o visitante com nome,
    documento. Armazene esses dados em lista_visitantes
    (como objetos).

Na opção 4 do menu será registrado a visita.
    Escolha o visitante (da lista de visitantes) e o
    profissional (da lista_profissionais), entre com a
    data e armazene a visita em lista_visitas
    (como objeto).

Na opção 5 do menu apenas crie um relatório de conferência.
    Selecione o Profissional e mostre todos os visitantes
    e a data da visita.

Obs. Em todas as listas serão armazenados as instâncias
de suas classes.

'''

class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def get_nome(self):
        return self.__nome

    def get_especialidade(self):
        return self.__especialidade

    def get_sala(self):
        return self.__sala

class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def get_nome(self):
        return self.__nome

    def get_documento(self):
        return self.__documento

class Visita:
    def __init__(self, visitante, profissional, data):
        self.visitante = visitante
        self.profissional = profissional
        self.data = data

    def __str__(self):
        return f"Profissional: {self.profissional.get_nome()} Visitante: {self.visitante.get_nome()} Data: {self.data}"

def cadastrar_profissional():
    nome = input(f"\nNome: ")
    especialidade = input("Especialidade: ")
    sala = input("Sala: ")

    objProfissional = Profissional(nome, especialidade, sala)
    lista_profissional.append(objProfissional)

def localizar_profissional():
    print("\n")
    for pos, profissional in enumerate(lista_profissional):
        print(f"{pos+1}. {profissional.get_nome()} - {profissional.get_especialidade()}")
    dado = input(f"\nDigite o nome do profissional ou a especialidade: ")
    consta = False
    for profissional in lista_profissional:
        if dado == profissional.get_nome() or dado == profissional.get_especialidade():
            consta = True
            print(f"{profissional.get_nome()} - Sala: {profissional.get_sala()}")
            break
    if consta == False:
        print("Profissional não encontrado.")
    
def cadastrar_visitante():
    nome = input("\nNome: ")
    documento = input("Documento: ")

    objVisitante = Visitante(nome, documento)
    lista_visitante.append(objVisitante)

def registrar_visita():
    print(f"\nVisitantes Cadastrados: ")
    for pos, visitante in enumerate(lista_visitante):
        print(f"{pos+1}. {visitante.get_nome()}")
    escolha_visitante = input(f"\nDigite o nome do visitante cadastrado: ")
    consta_visitante = False
    for visitante in lista_visitante:
        if escolha_visitante == visitante.get_nome():
            consta_visitante = True
            print(f"\nProfissionais Cadastrados: ")
            for pos, profissional in enumerate(lista_profissional):
                print(f"{pos+1}. {profissional.get_nome()}")
            escolha_profissional = input("\nDigite o nome do profissional cadastrado: ")
            consta_profissional = False
            for profissional in lista_profissional:
                if escolha_profissional == profissional.get_nome():
                    consta_profissional = True
                    data = input("Digite a data da visita (dd/mm/aa): ")
                    lista_visita.append(Visita(visitante,profissional,data))
                    print("\nVisita cadastrada")
            if consta_profissional == False:
                print("\nProfissional não cadastrado")
    if consta_visitante == False:
        print("\nVisitante não cadastrado")

def relatorio_conferencia():
    print("\nEscolha um profissional: ")
    for pos, profissional in enumerate(lista_profissional):
            print(f"{pos+1}. {profissional.get_nome()}")
    escolha_profissional = input("\nDigite o nome do profissional cadastrado: ")
    for visitas in lista_visita:
        if escolha_profissional == profissional.get_nome():
            print(visitas)

def menu():
    while True:
        escolha = input(
            """
======================
MENU
======================
1- Cadastrar Profissional
2- Localizar Profissional
3- Cadastrar Visitante
4- Registrar Visita
5- Relatório de Conferência
Escolha: """)
        if escolha == "1": cadastrar_profissional()
        if escolha == "2": localizar_profissional()
        if escolha == "3": cadastrar_visitante()
        if escolha == "4": registrar_visita()
        if escolha == "5": relatorio_conferencia()

lista_profissional = []
lista_visitante = []
lista_visita = []

menu()
