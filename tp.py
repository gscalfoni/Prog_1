def main():
	#declaração de variáveis
	Tp1 = float(0.0)
	Tp2 = float(0.0)
	Tp3 = float(0.0)
	n = int(0)
	maior = float(0.0)
	t1 = float(0.0)
	t2 = float(0.0)
	t3 = float(0.0)
	delta1 = float(0.0)
	delta2 = float(0.0)
	delta3 = float(0.0)
	p1 = float(0.0)
	p2 = float(0.0)
	p3 = float(0.0)
	pt = float(0.0)
	nomeM = int(0)
	#início do programa

	Tp1 = float(input())
	Tp2 = float(input())
	Tp3 = float(input())
	n = int(input())
	maior = -1000

	if (n==9999):
		print("SEM EQUIPES CADASTRADAS")
	else:
		while (n!=9999): #loop
			t1 = float(input())
			t2 = float(input())
			t3 = float(input())
			delta1 = abs(Tp1 - t1)
			delta2 = abs(Tp2 - t2)
			delta3 = abs(Tp3 - t3)

			if (delta1 < 3): #condicionais para contagem de pontos
				p1 = 100
			else:
				if (delta1 >= 3 and delta1 <= 5):
					p1 = 80
				else:
					p1 = 80-((delta1 - 5) / 5)


			if (delta2 < 3):
				p2 = 100
			else:
				if (delta2 >= 3 and delta2 <= 5):
					p2 = 80
				else:
					p2 = 80-((delta2 - 5) / 5)


			if (delta3 < 3):
				p3 = 100
			else:
				if (delta3 >= 3 and delta3 <= 5):
					p3 = 80
				else:
					p3 = 80-((delta3 - 5) / 5)

			pt = p1 +p2 +p3
			if (maior < pt): #equipe vencedora 
				maior = pt
				nomeM = n

			print("EQUIPE=%d P1=%.2f P2=%.2f P3=%.2f PT=%.2f"%(n , p1 , p2 , p3 , pt)) #saída de dados
			n = int(input()) #loop

		print ("EQUIPE VENCEDORA=%d PONTUACAO TOTAL=%.2f" %(nomeM , maior)) #saída de dados


if __name__ == "__main__":
	main()
			
