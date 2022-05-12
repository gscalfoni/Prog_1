def main ():
	#Declaração de variáveis
	a = int(0) 
	soma = ("")
	b = int(0)
	b16 = str("")

	a = int(input()) #Entrada de dados
	soma = ""

	while (a>=0): #Processamento
		b = a
		while (b>0):
			b16 = str(b%16)
			if(b16 == "10"):
				b16 = "A"
			else:
				if (b16 == "11"):
					b16 = "B"
				else:
					if(b16 == "12"):
						b16 = "C"
					else:
						if(b16 == "13"):
							b16 = "D"
						else:
							if(b16 == "14"):
								b16 = "E"
							else:
								if(b16 == "15"):
									b16 = "F"
			soma = b16 + soma 
			b = b // 16
		if (a==0):
			soma = "0"
		if(a>=0):
			print("BASE10=%d BASE16=%s" %(a, soma)) #Saída de dados
		soma = ""
		a = int(input()) #Entrada de dados
if __name__ == "__main__":
    main()
