from __future__ import annotations
import uuid
from typing import Dict, Optional

from Models import Account, Transaction


class Bank:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def create_account(self, nome: str, cpf: str, email: str) -> Account:
        account_id = uuid.uuid4().hex[:10]

        for acc in self.accounts.values():
            if acc.cpf == cpf:
                raise ValueError("Já existe uma conta com esse CPF.")

        acc = Account(id=account_id, nome=nome, cpf=cpf, email=email)
        self.accounts[account_id] = acc
        return acc

    def get_account(self, account_id: str) -> Account:
        if account_id not in self.accounts:
            raise KeyError("Conta não encontrada.")
        return self.accounts[account_id]

    def find_by_cpf(self, cpf: str) -> Optional[Account]:
        for acc in self.accounts.values():
            if acc.cpf == cpf:
                return acc
        return None

    def deposit(self, account_id: str, valor: float, descricao: Optional[str] = None) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")

        conta = self.get_account(account_id)
        trans = Transaction(tipo="deposito", valor=valor, descricao=descricao)
        conta.adicionar_transacao(trans)

    def withdraw(self, account_id: str, valor: float, descricao: Optional[str] = None) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")

        conta = self.get_account(account_id)

        if valor > conta.saldo:
            raise ValueError("Saldo insuficiente para saque.")

        trans = Transaction(tipo="saque", valor=valor, descricao=descricao)
        conta.adicionar_transacao(trans)

    def transfer(self, origem_id: str, destino_id: str, valor: float, descricao: Optional[str] = None) -> None:
        if origem_id == destino_id:
            raise ValueError("Não é possível transferir para a mesma conta.")

        conta_origem = self.get_account(origem_id)
        conta_destino = self.get_account(destino_id)

        if valor <= 0:
            raise ValueError("O valor da transferência deve ser maior que zero.")

        trans_out = Transaction(tipo="transferencia_saida", valor=valor, descricao=descricao)
        conta_origem.adicionar_transacao(trans_out)

        trans_in = Transaction(tipo="transferencia_entrada", valor=valor, descricao=descricao)
        conta_destino.adicionar_transacao(trans_in)

    def listar_contas(self):
        return list(self.accounts.values())