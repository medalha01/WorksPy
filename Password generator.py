import random


def gerador(op):
    password = ""
    for i in range(op):
        s = "abcdefghijmnopqerstuvxzkwyABCDEFGHIJMNOPQRSTUVXZYKZ@&*#!*#@($#)$@)!*#@!U&*@$&#$Y#&SD123456789**12"
        j = random.sample(s, 1)
        for x in j:
            password += x

    print(password)


def seguranca():
    try:
        op = input("Digite o tamanho da senha.")
        no = int(op)
        return no
    except:
        print("Apenas números serão aceitos")
        no = ""
    if no is not int:
        seguranca()


T = seguranca()

gerador(T)
