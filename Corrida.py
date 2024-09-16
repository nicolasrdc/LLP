m = float(input("Digite o número de metros que Leonardo pretende correr:"))
c = float(input("Digite o comprimento da pista: "))

if m>=1 and m<= pow(10, 8) and c>=1 and c<=10000:
    
    t = m % c 

    print("{:.2f}".format(t))

else: 
    Exception("Erro, tente novamente!")