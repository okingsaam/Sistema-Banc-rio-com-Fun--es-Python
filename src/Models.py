from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


def now_iso() -> str:
    return datetime.now().isoformat() + "Z"


@dataclass
class Transaction:
    tipo: str
    valor: float
    data: str = field(default_factory=now_iso)
    descricao: Optional[str] = None


@dataclass
class Account:
    id: str
    nome: str
    cpf: str
    email: str
    saldo: float = 0.0
    criado_em: str = field(default_factory=now_iso)
    transacoes: List[Transaction] = field(default_factory=list)

    def adicionar_transacao(self, transacao: Transaction):
        self.transacoes.append(transacao)
        if transacao.tipo == "deposito" or transacao.tipo == "transferencia_entrada":
            self.saldo += transacao.valor
        elif transacao.tipo == "saque" or transacao.tipo == "transferencia_saida":
            self.saldo -= transacao.valor