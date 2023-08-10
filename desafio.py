menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor de deposito: "))


        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Deposito falhou: O valor informado foi invalido.")    

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE 

        if excedeu_saldo:
            print("Operção invalida, você não tem saldo suficinte")
        elif excedeu_limite:
            print("Operação invalida. O valor do saque excede o limite.")
        elif excedeu_saque:
            print("Operação invalida> Numero maximo de saques excedidos.")   

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou: o valor informado é invalido:")   

    elif opcao == "e":
        print("\n******************** EXTRATO ********************")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*************************************************")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, porfavor selecione a operação desejada")     