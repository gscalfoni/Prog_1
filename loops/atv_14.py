def main ():
    n = int(0)
    maior = int(0)
    menor = int(0)
    con_n = int(0)
    con_f = int(0)
    con_m = int(0)
    alturas = float(0.0)
    a = float(0.0)
    s = str("")
    media = (0.0)
    
    n = int(input())
    maior = -1
    menor = 1000
    con_n = 0
    con_f = 0
    con_m = 0
    alturas = 0
    while (con_n< n):
        a = float(input())
        s = str(input())
       
        if (a>maior):
            maior=a
        if (a<menor):
            menor=a
       
        if(s=="f" or s=="F"):
            alturas = alturas + a
            con_f += 1
        if(s=="m" or s=="M"):
            con_m += 1

        con_n +=1
    
    if (con_f == 0):
        media = 0
    else:
        media = (alturas/con_f)
    
    if (n > 0):
        print("MAIOR ALTURA = %.2f MENOR ALTURA = %.2f"%(maior, menor))
        print("MEDIA DE ALTURA FEMININA = %.2f"%(media))
        print("NUMERO DE HOMENS = %d"%(con_m))

if __name__ == "__main__":
    main()
    