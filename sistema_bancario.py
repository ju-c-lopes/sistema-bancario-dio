from os import system
import platform

if platform.system() == "Windows":
    system("cls")
else:
    system("clear")

header = f"""
    {"=" * 50}
    {"sistema bancário dio".upper().center(50, " ")}
    {"=" * 50}

"""
print(header)

nome_usuario = input("Nome do usuário: ")

print(f"Seja bem-vindo(a) {nome_usuario.title()} ao {'sistema bancário dio'.upper()}!!!")

# Variáveis

deposito = f"""
{"-" * 30}
"""
saque = f"""
{"-" * 30}
"""
extrato = f"""
{'extrato'.upper()}
{"-" * 30}
"""
saldo = 0
saque_acumulado = 0
limite_saque = 500
quantidade_saques = 0

while True:
    
    menu = """
    Qual operação deseja fazer?
    
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
    """

    print(menu)
    try:
        opcao = int(input("\tDigite sua opção: "))
        if opcao != 3 and extrato.find("movimentação") != -1:
            extrato = f"""
            \r{'extrato'.upper()}
            \r{"-" * 30}
            \r"""
    except ValueError:
        print(f"\nO valor digitado não é válido.\n")
        continue
    print()


    # Opção inválida
    if opcao not in range(1, 5):
        print("\nVocê digitou uma opção inválida!")
        continue

    # Opção de depósito
    elif opcao == 1:
        valor_depositado = float(input("Valor a ser depositado: "))
        if valor_depositado <= 0:
            print("Depósitos devem ser maiores que 0(zero)")
            continue
        saldo += valor_depositado
        entrada = f"""\rDepósito de R$ {valor_depositado:.2f}
        \r{"-" * 30}
        """
        deposito += entrada
        extrato += entrada

    # Opção de saque
    elif opcao == 2:
        if saldo <= 0:
            print("Você não tem saldo em conta para realizar operação de saque!")
            continue

        if quantidade_saques >= 3:
            print(f"{'-' * 30}\nVocê excedeu a quantidade diária permitida para realizar saques.\n{'-' * 30}")
            continue

        valor_a_sacar = float(input("Valor a ser sacado: "))

        if saque_acumulado + valor_a_sacar > limite_saque or valor_a_sacar > limite_saque:
            print(f"{'-' * 30}\nO limite diário para saque é de R$ {limite_saque:.2f}\n{'-' * 30}")
            continue

        if valor_a_sacar > saldo:
            print(f"O valor do saque de R$ {valor_a_sacar:.2f} excede seu saldo de R$ {saldo:.2f}")
            continue

        saldo -= valor_a_sacar
        saque_acumulado += valor_a_sacar
        quantidade_saques += 1
        saida = f"""\rSaque de R$ {valor_a_sacar:.2f}
        \r{"-" * 30}
        """
        saque += saida
        extrato += saida

    elif opcao == 3:

        if extrato.find("Depósito") == -1 and extrato.find("Saque") == -1:
            if extrato.find("movimentação") == -1:
                extrato += "Sem movimentação na conta"
        if platform.system() == "Windows":
            system("cls")
        else:
            system("clear")
        print(header)
        print(f"{'-' * 30}\nSaldo atual: R$ {saldo:.2f}\n{'-' * 30}")
        print(extrato)
        continue

    elif opcao == 4:
        print("\nObrigado por utilizar nossos serviços!!!")
        break

    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

    print(header)
    
    print(f"{'-' * 30}\nSaldo atual: R$ {saldo:.2f}\n{'-' * 30}")