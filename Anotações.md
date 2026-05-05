# Como subir o ambiente

1. Criar e ativar o .venv
```bash
python -m venv .venv
cd .venv/Scripts
activate
cd ../..
```

2. Baixar as bibliotecas com pip
```bash
pip install -r pips.txt
```

3. Copiar o .env.example
```bash
copy .env.example .env
```

4. Rodar a aplicação
```bash
python main.py
```

5. Acessar a /seed/ (se precisar) para testar a tabela de lançamento financeiro

# Detalhes

Toda vez que alterar algo no banco de dados (models.py), deve atualizar o banco com os comandos:
```bash
flask db migrate -m "<comentario>"
flask db upgrade
```

# Base para a criação do LancamentoFinanceiro 

Registro de Compras ou Despesas, isto é, aba "Pagamentos" na planilha
* usando de ref a planilha do cliente

1. produto: bebida
2. fornecedor(nome): Coca Cola
3. despesa/custo: "Variável" ou "Fixo"
4. origem(?): ele coloca campos como "Stone", "Itau", "Dinheiro" (obs: não sei se coloco)
5. pagamento: "Pix", "Boleto", "Débito Automático"
6. status: "Pago", "Pendente"
7. valor: R$ 803,53 (no caso da coca)
