menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saque = 0
LIMITE_SAQUE = 3


while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = input(float())
        if float(valor) > 0 :
            calculo = float(valor) + saldo
            saldo = "R$ {:,.2f}" + str(calculo)
            print("Seu saldo agora é R$ " + str(saldo))
        elif float(valor) < 0:
            print("Erro ao depositar")
    
    if opcao == "s":
        print("Saque")
    
    if opcao == "e":
        print("Extrato")
        
    if opcao == "q":
        break
    