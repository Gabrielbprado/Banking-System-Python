import textwrap

print(textwrap.dedent("""\
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [q]\tSair
    => """))

deposit = 0
withdraw = 0
withdraw_limit = 3
accounts = []
withdraw_number = 0

while True:
    option = input("Enter the option: ")

    if option == "1":
        print("Insert how much you want to deposit:")
        valor = float(input())
        deposit += valor

    elif option == "2":
        print("How much do you want to withdraw?")
        valor = float(input())
        if valor > deposit:
            print("You don't have enough money")
        else:
            withdraw += valor
            deposit -= valor
            withdraw_limit -= 1
            if withdraw_limit < 0:
                print("You have reached the withdraw limit")
            else:
                print("You have withdrawn", valor)
                withdraw_number += 1

    elif option == "3":
        print("Your balance is:", deposit)

    elif option == "4":
        print("New account created")
        name = input("Insert the name of the account: ")
        accounts.append(name)

    elif option == "5":
        print("Account list")
        for account in accounts:
            print(account)

    elif option == "6":
        print("New user created")

    elif option == "q":
        break

    else:
        print("Invalid option")
