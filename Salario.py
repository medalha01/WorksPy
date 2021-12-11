def salario(salarioun):
    salario2 = float(salarioun)
    salario2 = round(salario2, 2)
    if salario2 <= 400 and salario2 >= 0:
        novosalario = salario2 * 1.15
        reajuste = salario2 * 0.15
        Percentual = "15%"
    elif salario2 <= 800 and salario2 >= 400.01:
        novosalario = salario2 * 1.12
        reajuste = salario2 * 0.12
        Percentual = "12%"     
    elif salario2 <= 1200 and salario2 >= 800.01:
        novosalario = salario2 * 1.10
        reajuste = salario2 * 0.10
        Percentual = "10%" 
    elif salario2 <= 2000 and salario2 >= 1200.01:
        novosalario = salario2 * 1.07
        reajuste = salario2 * 0.07
        Percentual = "7%"  
    elif salario2 >= 2000.01:
        novosalario = salario2 * 1.04
        reajuste = salario2 * 0.04
        Percentual = "4%"    
    print(novosalario)
    print(reajuste) 
    print(Percentual)         
input1 = input('Digite o salário: ')
salario(input1)
