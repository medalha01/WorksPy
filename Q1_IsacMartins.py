a, c, x, y = input().split()
a = int(a)
c = int(c)
x = int(x)
y = int(y)
t = c - y - x - 1 
if a > 0 and c <= 1000 and a <= 1000 and x <= c and y <= c and x <= 100: 
    if a > t:
        if x > y/2:
            print("Caio, a culpa é sua")
        else:
            print("Igor Bolado!")
    else:
        print("Igor Feliz!")
else:
    print("Erro: Input Inválido")

