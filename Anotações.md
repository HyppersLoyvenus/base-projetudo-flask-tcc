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

# Como contribuir com o projeto

### Fork do Repositório

1. Acesse o repositório original
2. No canto superior direito da página, clique no botão "Fork"

### Clone do Repositório

1. No seu fork, clique no botão verde "Code"
2. Copie a URL do repositório
3. Abra o terminal e execute:
```sh
git clone https://github.com/HyppersLoyvenus/base-projetudo-flask-tcc
```

### Fazendo as Alterações

1. Crie uma nova branch para suas alterações:
```sh
git checkout -b <nome-da-branch>
```
2. Faça as correções necessárias nos arquivos
3. Adicione as alterações:
```sh
git add .
```
4. Faça o commit das alterações:
```sh
git commit -m "Alteração de X coisa"
```
5. Envie as alterações para o seu fork:
```sh
git push origin <nome-da-branch>
```

### Criando o Pull Request

1. Acesse seu repositório no GitHub
2. Clique no botão "Compare & pull request" que aparecerá no topo
3. Clique em "Create pull request"

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
