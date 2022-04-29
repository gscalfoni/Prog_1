def main():  
    a = int(0)
    b = int(0)
    c = int(0)
    x = int(0)

    a = int(input())
    b = int(input())
    c = int(input())

    while (a!=0 or b!=0 or c!=0): 
        if (a>=b and a>=c):
            x=a
        else:
            if (b>=a and b>=c):
                x=b
            else:
                x=c
        print("MAIOR ( %d , %d , %d ) = %d" %(a, b, c, x))
        a = int(input())
        b = int(input())
        c = int(input())
if __name__ == "__main__":
    main()