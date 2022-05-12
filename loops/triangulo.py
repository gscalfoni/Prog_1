def main ():
	#Declaração de variáveis
	a = float(0.0)
	b = float(0.0)
	c = float(0.0)
	maior = int(0)
	periE = float(0.0)
	periI = float(0.0)
	periESC = float(0.0)
	con_nt = int(0)
	con_eq = int(0)
	con_iso = int(0)
	con_esc = int(0)
	con_t = int(0)
	con_total = int(0)
	tipo = ("")
	l1 = float(0.0)
	l2 = float(0.0)
	l3 = float(0.0)
	area = float(0.0)
	peri = float(0.0)
	perc_t = float(0.0)
	perc_nt = float(0.0)
	periM_eq = float(0.0)
	periM_esc = float(0.0)
	periM_iso = float(0.0)

#Entrada de dados
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

#Processamento
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
						tipo = "ISOSCELES"
						periI = periI + peri
						con_iso +=1
				con_t += 1
				if (maior<area):
					maior = area
					l1 = a
					l2 = b
					l3 = c
				print("AREA = %.2f PERIMETRO = %.2f TIPO = %s" %(area , peri , tipo)) #Saída de dados
			
			else:
				print("NAO TRIANGULO") #Saída de dados
				con_nt += 1

			con_total += 1
			a = float(input())
			b = float(input())
			c = float(input())

		if (con_t == 0):
			perc_t = 0
		else:
			perc_t = (con_t/ con_total)*100
			print("A maior area = %.2f eh do triangulo: lado1 = %.2f, lado2 = %.2f e lado3 = %.2f" %(maior , l1, l2, l3)) #Saída de dados
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
			
			print("%.2f eh o perimetro medio dos triangulos equilateros" %(periM_eq)) #Saída de dados
			print("%.2f eh o perimetro medio dos triangulos isosceles" %(periM_iso)) #Saída de dados
			print("%.2f eh o perimetro medio dos triangulos escalenos" %(periM_esc)) #Saída de dados


		print("Percentual de triangulos = %.2f" %(perc_t)) #Saída de dados
		print("Percentual de nao triangulos = %.2f" %(perc_nt)) #Saída de dados

if __name__ == "__main__":
	main()
