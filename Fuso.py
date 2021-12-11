def a(s,t,f):
    s = float(s)
    t = float(t)
    f = float(f)
    if s <= 23 and s >= 0 and t <= 12 and t >= 1 and f <= 5 and f >= -5:
        tempo = s + t + f 
        while tempo >= 24:
            tempo = tempo - 24
    print(tempo)      
input1, input2, input3 = input().split()
a(input1, input2, input3)
