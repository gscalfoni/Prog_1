a = float(input())
b = float(input())
c = float(input())

maior = -1
periE = 0
periI = 0
periESC = 0
con_nt = 0
con_eq = 0
con_iso = 0
con_esc = 0
con_t = 0
con_total = 0

if (a==0 or b==0 or c==0):
    print("NAO HA DADOS PARA PROCESSAR")
else:
    while(a!=0 or b!=0 or c!=0):
        tipo = ""
        if(c<a+b and a<b+c and b<c+a):
            peri = a + b + c
            area = ((peri/2)*(peri/2 - a)*(peri/2 - b)*(peri/2 - c))**(1/2)
            if (a==b and b==c):
                tipo= "EQUILATERO"
                periE = periE + peri
                con_eq += 1
            else:
                if (a!=b and b!=c and c!=a):
                    tipo = "ESCALENO"
                    periESC = periESC + peri
                    con_esc += 1
                else:
                    tipo = "ISOCELES"
                    periI = periI + peri
                    con_iso +=1
            con_t += 1
            if (maior<area):
                maior = area
                l1 = a
                l2 = b
                l3 = c
            print("AREA = %.2f PERIMETRO = %.2f TIPO = %s" %(area , peri , tipo))
        
        else:
            print("NAO TRIANGULO")
            con_nt += 1

        con_total += 1
        a = float(input())
        b = float(input())
        c = float(input())

if (con_t == 0):
    perc_t = 0
else:
    perc_t = (con_t/ con_total)*100

if (con_nt == 0):
    perc_nt = 0
else:
    perc_nt = (con_nt/ con_total)*100

if (perc_t>0):
    if (con_eq == 0):
        periM_eq = 0
    else:
        periM_eq = (periE/con_eq)
    if(con_esc == 0):
        periM_esc = 0
    else:
        periM_esc = (periESC/con_esc)
    if(con_iso == 0):
        periM_iso = 0
    else:
        periM_iso = (periI/con_iso)
    
    print("%.2f eh o perimetro medio dos triangulos equilateros" %(periM_eq))
    print("%.2f eh o perimetro medio dos triangulos isoceles" %(periM_iso))
    print("%.2f eh o perimetro medio dos triangulos escaleno" %(periM_esc))


print("A maior area = %.2f eh do triangulo: lado1 = %.2f, lado2 = %.2f e lado3 = %.2f" %(maior , l1, l2, l3))
print("Percentual de triangulos = %.2f" %(perc_t))
print("Percentual de nao triangulos = %.2f)" %(perc_nt))



