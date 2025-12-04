
import json
from typing import Dict
from Models import Account, Transaction


class Storage:
    @staticmethod
    def save_json(path: str, accounts: Dict[str, Account]):
        data = {
            acc_id: {
                "id": acc.id,
                "nome": acc.nome,
                "cpf": acc.cpf,
                "email": acc.email,
                "saldo": acc.saldo,
                "criado_em": acc.criado_em,
                "transacoes": [
                    {
                        "tipo": t.tipo,
                        "valor": t.valor,
                        "data": t.data,
                        "descricao": t.descricao,
                    }
                    for t in acc.transacoes
                ],
            }
            for acc_id, acc in accounts.items()
        }

        # garante que a pasta exista
        import os
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def load_json(path: str) -> Dict[str, Account]:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return {}

        accounts: Dict[str, Account] = {}
        for acc_id, entry in data.items():
            acc = Account(
                id=entry["id"],
                nome=entry["nome"],
                cpf=entry["cpf"],
                email=entry["email"],
                saldo=entry.get("saldo", 0.0),
                criado_em=entry.get("criado_em"),
            )

            for t in entry.get("transacoes", []):
                trans = Transaction(
                    tipo=t.get("tipo"),
                    valor=t.get("valor"),
                    data=t.get("data"),
                    descricao=t.get("descricao"),
                )
                acc.transacoes.append(trans)

            accounts[acc_id] = acc

        return accounts
