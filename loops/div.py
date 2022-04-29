def main():
    quo = int(0)
    a = int(0)
    b = int(0)
    
    quo = 0
    a = int (input())
    b = int (input())
    
    if (a<=0 or b<=0):
       print("ENTRADA INVALIDA")
    else:
        while (a>b):
            a = a - b
            quo = quo + 1 
    
        print("QUOCIENTE=%d" %(quo))

if __name__ == "__main__":
    main()