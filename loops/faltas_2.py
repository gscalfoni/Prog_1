def main(): 
    
    turma = str("")
    cont_faltas = int(0)
    maior = float(0.0)
    menor = float(0.0)
    matri = str("")
    freq = str("")
    porcent = float (0.0)
    maior_turma = str("")
    menor_turma = str("")
    cont_percent = float(0.0)
    
    cont_percent = 0
    maior = -1
    menor= 101
    turma = str(input())

    
    while (turma != "TFIM"):
        matri = str(input())
        cont_faltas = 0
        cont_freq = 0
        
        while (matri != "MFIM"):
            freq = str(input())
            cont_freq = cont_freq +1
            if (freq == "A"): 
                cont_faltas = cont_faltas + 1
            matri = str(input())
                 
        porcent = (cont_faltas/ cont_freq)*100 
            
        if (porcent > maior):
            maior = porcent
            maior_turma = turma
        if (porcent < menor):
            menor = porcent
            menor_turma = turma
        if (porcent > 20.00):
            cont_percent = cont_percent + 1
    
        print("TURMA=%s AUSENCIA=%.2f%%" %(turma, porcent))
        turma = str(input())
        
    print("TURMA COM MAIOR PORCENTAGEM DE AUSENCIA=%s AUSENCIA=%.2f%%" %(maior_turma , maior))
    print("TURMA COM MENOR PORCENTAGEM DE AUSENCIA=%s AUSENCIA=%.2f%%" %(menor_turma , menor))
    print("%.d TURMAS COM PORCENTAGEM DE AUSENCIA SUPERIOR A 20%%" %(cont_percent))
    
if __name__ == "__main__":
    main()