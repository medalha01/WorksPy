def fun(): 
    n, m = input("Digite N e M: ").split()
    m = float(m)
    n = float(n)
    t = 0
    p1 = 0
    p2 = 0
    gamma = 0
    delta = 0
    omnicrom = 0
    divisible = "a"
    n1 = 0
    while p1 < n:
        while n >= (2+t):
            divisible = (n % (2+t))
            if divisible == 0:
                t = t + 1
                gamma = gamma + 1
            else:
                t = t + 1
        n = n - 1
        t = 0
        if gamma == 0:
            p1 = n
            t = 0
            break
        gamma = 0

    while p2 < m:
        while m >= (2+t):
            divisible = (m % (2+t))
            if divisible == 0:
                t = t + 1
                omnicrom = omnicrom + 1
            else:
                t = t + 1
        m = m - 1
        t = 0
        if omnicrom == 0:
            p2 = m
            print(p2)
            break
        omnicrom = 0
    print(p1*p2)
    print("Programa encerrado")
fun()