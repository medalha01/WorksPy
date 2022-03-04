from Conta import Conta
import re

dicContas = {}


def criar(dicContas):
    cod = input("Qual o codigo da conta?").strip()
    cpf = input("Qual o cpf do dono da conta?").strip()
    nome = input("Qual o nome do dono da conta?").strip()
    senha = input("Qual a senha da conta?").strip()
    saldo = input("Qual o saldo inicial da conta?").strip()
    hold2 = Conta(cpf, nome, senha, saldo)
    dicContas.update({cod: hold2})
    return dicContas


def sacar(dicContas):
    valor = input()
    while valor is not int:
        input("Digite um valor válido")
    cod = input().strip
    conta = dicContas.get(cod)
    conta.saque(valor)


def depositar(dicContas):
    valor = input()
    while valor is not int:
        input("Digite um valor válido")
    cod = input().strip
    conta = dicContas.get(cod)
    conta.deposito(valor)


def transfere(dicContas):
    valor = input()
    while valor is not int:
        input("Digite um valor válido")
    cod = input().strip
    conta = dicContas.get(cod)
    cod2 = input().strip
    conta2 = dicContas.get(cod2)
    conta.transfer(conta2, valor)

def extrato()
    cod = input().strip
    conta = dicContas.get(cod)
    conta.extrato
    

def operation(hold):
    oper = {
        1: criar(),
        2: sacar(),
        3: depositar(),
        4: transfere(),
        5: extrato(),
        6: break,
    }
    return oper.get(hold)


while True:
    print(
        "Bem vindo ao sistema! \nPara que eu possa ajudar digite qual serviço você procura:"
    )
    print(
        " 1 - Criação de Conta\n 2 - Saque\n 3 - Depósito\n 4 - Transferência\n 5 - Extrato\n 6 - Sair"
    )
    hold = input().strip()
    while hold not in ["1", "2", "3", "4", "5", "6"]:
        hold = input("Digite um input válido").strip()
    hold = int(hold)

    operation(hold)
