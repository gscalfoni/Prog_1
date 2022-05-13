'''
Algoritmo
    Var
        n, maior, menor, con_n, con_f, con_m: inteiro
        a, alturas: racional
		s, media: literal
	
    Início
	    leia (n)
	    maior <- (-1)
	    menor <- 1000
	    con_n <- 0
	    con_f <- 0
	    con_m <- 0
	    alturasF <- 0
	
		enquanto (con_n < n) então
			leia(a)
			leia(s)

			se (a > maior) então
				maior <- a
			
            se (a < menor) então
				menor <- a
			
			se (s == “f” OU s == “F”) então
				alturasF <- alturasF + a
				con_f <- con_f + 1

			se (s == “m” OU s == “M”) então
				con_m <- con_m +1

			com_n <- con_n +1
        
		se (con_f == 0) então
			media <- "grupo sem mulheres"
		senão
			media <- literal (alturasF/con_f)
		
		se (n > 0) então
            escreva maior
		    escreva menor
            escreva media
            escreve con_m
fim_algoritmo

'''

def main ():
    n = int(0)
    maior = int(0)
    menor = int(0)
    con_n = int(0)
    con_f = int(0)
    con_m = int(0)
    alturasF = float(0.0)
    a = float(0.0)
    s = str("")
    media = str("")
    
    n = int(input())
    maior = -1
    menor = 1000
    con_n = 0
    con_f = 0
    con_m = 0
    alturasF = 0
    while (con_n< n):
        a = float(input())
        s = str(input())
       
        if (a>maior):
            maior=a
        if (a<menor):
            menor=a
       
        if(s=="f" or s=="F"):
            alturasF = alturasF + a
            con_f += 1
        if(s=="m" or s=="M"):
            con_m += 1

        con_n +=1
    
    if (con_f == 0):
        media = "grupo sem mulheres"
    else:
        media = str(alturasF/con_f)
    
    if (n > 0):
        print("MAIOR ALTURA = %.2f MENOR ALTURA = %.2f"%(maior, menor))
        print("MEDIA DE ALTURA FEMININA = %s"%(media))
        print("NUMERO DE HOMENS = %d"%(con_m))

if __name__ == "__main__":
    main()
    