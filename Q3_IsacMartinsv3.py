conf = "S"
def fun(): 
    t = 0
    salario1 = 0
    idade2 = 1500
    conf = "S"
    sexo1 = 0
    idade1 = 0
    nome2 = 0
    while conf == "S":
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        sexo = input("Digite o Sexo (M/F): ").upper()
        salario = input("Digite o salário: ")
        salario = float(salario)
        idade = int(idade)
        if sexo == "F" and salario < 2000:
            t = t + 1
        if salario > salario1:
            sexo1 = sexo
            idade1 = idade
            salario1 = salario
        if idade2 > idade:
            idade2 = idade
            nome2 = nome
        conf = input("Deseja continuar cadastrando?").upper()
    return [t, sexo1, idade1, nome2]
t, sexo1, idade1, nome2 = fun()
print("A quantidade de mulheres com salário menor que 2000 é: ", t)
print("O sexo e idade da pessoa com maior salário é:", "Sexo ", sexo1, "Idade ", idade1)
print("O nome do morador mais novo é: ", nome2)
