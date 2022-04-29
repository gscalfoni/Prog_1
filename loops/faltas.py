def main(): 
    
    N = int(0)
    cont_N = int(0)
    turma = str("")
    quant = int(0)
    cont_Q = int(0)
    cont_faltas = int(0)
    maior = float(0.0)
    menor = float(0.0)
    matri = str("")
    freq = str("")
    porcent = float (0.0)
    maior_turma = str("")
    menor_turma = str("")
    cont_percent = float(0.0)
    
    N = int(input())
    contN = 0 
    cont_percent = 0
    maior = -1
    menor= 101
    
    while (cont_N < N):
        turma = str(input())
        quant = int(input())
        cont_Q = 0 
        cont_faltas = 0 
        
        while (cont_Q < quant):
            matri = str(input())
            freq = str(input())
            
            if (freq == "A"): 
                cont_faltas = cont_faltas + 1 
            cont_Q = cont_Q + 1 
            
        porcent = (cont_faltas/ quant)*100 
            
        if (porcent > maior):
            maior = porcent
            maior_turma = turma
        if (porcent < menor):
            menor = porcent
            menor_turma = turma
        if (porcent > 20.00):
            cont_percent = cont_percent + 1
    
        print("TURMA=%s AUSENCIA=%.2f%%" %(turma, porcent)) 
        
        cont_N = cont_N + 1 

    print("TURMA COM MAIOR PORCENTAGEM DE AUSENCIA=%s AUSENCIA=%.2f%%" %(maior_turma , maior))
    print("TURMA COM MENOR PORCENTAGEM DE AUSENCIA=%s AUSENCIA=%.2f%%" %(menor_turma , menor))
    print("%.d TURMAS COM PORCENTAGEM DE AUSENCIA SUPERIOR A 20%%" %(cont_percent))
    
if __name__ == "__main__":
    main()