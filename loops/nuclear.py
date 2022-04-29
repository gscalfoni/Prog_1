def main():  
    massa_ini = float(0.0)
    massa_fim = float(0.0)
    quo = float(0.0)
    segundos = int(0)
    minutos = int(0)
    horas = int(0)

    massa_ini = float(input())
    
    while (massa_ini >= 0):
        quo = 0
        massa_fim = massa_ini
        
        while (massa_fim >= 0.5):
            massa_fim = massa_fim/2
            quo = quo + 1
            
        segundos = quo * 50
            
        horas = segundos // 3600
        minutos = (segundos % 3600)//60
        segundos = (segundos % 3600)%60
        
        print("MASSA INICIAL = %.3f MASSA FINAL = %.3f TEMPO DECORRIDO = %d:%d:%d" %(massa_ini, massa_fim, horas, minutos, segundos))
        massa_ini = float(input())
    
    print ("FIM")
if __name__ == "__main__":
    main()
    