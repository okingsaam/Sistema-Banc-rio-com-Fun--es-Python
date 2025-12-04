"""Script de demonstração não interativo para testar operações básicas do banco.

Cria contas, realiza depósitos, saques e transferências e salva o arquivo JSON em `data/banco_db.json`.
"""

import os
import sys

# garante que a pasta `src` esteja no sys.path para imports locais
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from Bank import Bank
from Storage import Storage


DB_PATH = os.path.join("data", "banco_db.json")


def main():
    # limpa DB para demonstração
    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
        except Exception:
            pass

    bank = Bank()

    # criar contas
    a1 = bank.create_account("Alice", "11122233344", "alice@example.com")
    a2 = bank.create_account("Bob", "22233344455", "bob@example.com")

    # operações
    bank.deposit(a1.id, 100.0, "Depósito inicial")
    bank.deposit(a2.id, 50.0)
    bank.withdraw(a1.id, 30.0, "Saque ATM")
    bank.transfer(a1.id, a2.id, 20.0, "Pagamento")

    # salvar
    Storage.save_json(DB_PATH, bank.accounts)

    # output resumo
    print("Demonstração concluída. Contas e transações:")
    for acc in bank.listar_contas():
        print(f"ID: {acc.id} | Nome: {acc.nome} | Saldo: R${acc.saldo:.2f}")
        for t in acc.transacoes:
            print(f"  - [{t.data}] {t.tipo} R${t.valor:.2f} ({t.descricao})")

    print(f"\nArquivo salvo em: {DB_PATH}")


if __name__ == "__main__":
    main()
