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
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0 :
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Seu saldo agora é R$ "+ str(saldo) )
        else:
            print("Erro ao depositar")
    
    if opcao == "s":
        sacar = float(input("Informe o valor de saque: "))
        
        excedeu_limite = limite < sacar
        excedeu_saldo = sacar > saldo
        excedeu_saques = numeros_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            
        elif sacar > 0  and sacar <= saldo:
            saldo -= sacar
            numeros_saque += 1
            extrato += f"Saque: R$ {sacar:.2f}\n"
            print ( "Seu saque de "+  str(sacar) +" foi efeituado com sucesso!  Seu saldo agora é R$" + str(saldo))
            
        else:
            print("Erro ao sacar")
    
    if opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    if opcao == "q":
        break
    