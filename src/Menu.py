from Bank import Bank
from Storage import Storage
import os

# Caminho padrão do arquivo JSON
DB_PATH = os.path.join("data", "banco_db.json")


def carregar_banco() -> Bank:
    bank = Bank()
    bank.accounts = Storage.load_json(DB_PATH) or {}
    return bank


def salvar_banco(bank: Bank):
    Storage.save_json(DB_PATH, bank.accounts)


def menu():
    bank = carregar_banco()

    while True:
        print("\n=== SISTEMA BANCÁRIO ===")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Listar contas")
        print("6 - Ver extrato")
        print("0 - Sair")

        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            try:
                acc = bank.create_account(nome, cpf, email)
                salvar_banco(bank)
                print(f"Conta criada! ID: {acc.id}")
            except Exception as e:
                print("Erro:", e)

        elif opc == "2":
            acc_id = input("ID da conta: ")
            valor = float(input("Valor: "))
            try:
                bank.deposit(acc_id, valor)
                salvar_banco(bank)
                print("Depósito realizado!")
            except Exception as e:
                print("Erro:", e)

        elif opc == "3":
            acc_id = input("ID da conta: ")
            valor = float(input("Valor: "))
            try:
                bank.withdraw(acc_id, valor)
                salvar_banco(bank)
                print("Saque realizado!")
            except Exception as e:
                print("Erro:", e)

        elif opc == "4":
            o = input("Conta origem: ")
            d = input("Conta destino: ")
            v = float(input("Valor: "))
            try:
                bank.transfer(o, d, v)
                salvar_banco(bank)
                print("Transferência concluída!")
            except Exception as e:
                print("Erro:", e)

        elif opc == "5":
            contas = bank.listar_contas()
            if not contas:
                print("Nenhuma conta cadastrada.")
            for c in contas:
                print(f"ID: {c.id} | Nome: {c.nome} | CPF: {c.cpf} | Saldo: R${c.saldo:.2f}")

        elif opc == "6":
            acc_id = input("ID da conta: ")
            try:
                acc = bank.get_account(acc_id)
                print(f"\nExtrato de {acc.nome} (Saldo: R${acc.saldo:.2f})")
                for t in acc.transacoes:
                    print(f"[{t.data}] {t.tipo.upper()} - R${t.valor:.2f} ({t.descricao})")
            except Exception as e:
                print("Erro:", e)

        elif opc == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")
