alunosFut = set()
alunosBasq = set()
alunosNat = set()
alunosVol = set()

def cadastro():
    print("Qual modalidade o aluno dever ser adicionado?")
    print(" 1 - Futebol    3 - Basqueste \n 2 - Natação    4 - Volêi")
    userInput0 = int(input("--"))
    ## O código ficaria melhor com o uso de dicionário.
    while userInput0 < 1 or userinput0 > 4:
        print("Resposta inválida")
        userInput0 = input("--")
    if userInput0 == 1:
        print("Digite o nome do aluno a ser adicionado a classe de Futebol:")
        userInput0 = input("=>")
        alunosFut.add(userinput0)
    if userInput0 == 2:
        print("Digite o nome do aluno a ser adicionado a classe de Natação:")
        userInput0 = input("=>")
        alunosNat.add(userinput0)
    if userInput0 == 3:
        print("Digite o nome do aluno a ser adicionado a classe de Basquete:")
        userInput0 = input("=>")
        alunosBasq.add(userinput0)
    if userInput0 == 4:
        print("Digite o nome do aluno a ser adicionado a classe de Volêi:")
        userInput0 = input("=>")
        alunosVol.add(userinput0)
    userInput1 = input("Deseja adicionar mais algum aluno?")
    if userInput1.lower() in {"yes", "sim", "s", "y"}:
        Cadastro()


def alunos():
    print(*alunosFut, sep=", ")
    print(*alunosNat, sep=", ")
    print(*alunosBasq, sep=", ")
    print(*alunosVol, sep=", ")


def verificacao():
    print(alunosFut.intersection(alunosnat))
    print(alunosFut.intersection(alunosbasq))
    print(alunosFut.intersection(alunosvol))
    print(alunosNat.intersection(alunosbasq))
    print(alunosNat.intersection(alunosvol))
    print(alunosBasq.intersection(alunosvol))


def somaGeral():
    print("O numero de aluno matriculados no futebol é: ", len(alunosFut))
    print("O numero de aluno matriculados na natação é: ", len(alunosNat))
    print("O numero de aluno matriculados no basquete é: ", len(alunosBasq))
    print("O numero de aluno matriculados no volêi é: ", len(alunosVol))
    total = (
        int(len(alunosFut))
        + int(len(alunosNat))
        + int(len(alunosBasq))
        + int(len(alunosVol))
    )
    print(total)


cadastro()
verificacao()
alunos()
somaGeral()
