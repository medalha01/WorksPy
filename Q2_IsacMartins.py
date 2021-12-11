w = "S"
while w == "S":
    alice, beto, clara = input("Digite os valores de Alice, Beto e Clara").split()
    alice = int(alice)
    beto = int(beto)
    clara = int(clara)
    if alice != beto and  alice != clara:
        print("A")
    elif beto != alice and beto != clara:
        print("B")
    elif clara != alice and clara != beto:
        print("C")
    else:
        print('*')
    w = input("Deseja continuar jogando? (S/N)").upper() 
