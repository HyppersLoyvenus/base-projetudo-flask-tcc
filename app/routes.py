from app import app, BancoDeDados
from flask import render_template, url_for, request, redirect

from app.models import LancamentoFinanceiro, Produto, Fornecedor
from app.forms import LancamentoForm

@app.route('/')
def homepage():

    return render_template('index.html')

@app.route('/seed/')
def seed():
    from app.models import Produto, Fornecedor

    BancoDeDados.session.add(Produto(nome="Bebida"))
    BancoDeDados.session.add(Produto(nome="Cigarro"))
    BancoDeDados.session.add(Fornecedor(nome="Coca Cola"))
    BancoDeDados.session.add(Fornecedor(nome="Phillip Morris"))

    BancoDeDados.session.commit()

    return "Dados inseridos!"

# Criar Lançamentos Financeiros 
@app.route('/lancamento/novo', methods=['GET', 'POST'])
def novo_lancamento():
    form = LancamentoForm()

    form.produto.choices = [(p.id, p.nome) for p in Produto.query.all()]
    form.fornecedor.choices = [(f.id, f.nome) for f in Fornecedor.query.all()]

    if form.validate_on_submit():
        form.save()
        return redirect(url_for('listar_lancamento'))

    return render_template('lancamento_form.html', form=form)

# Listar
@app.route('/lancamentos')
def listar_lancamento():
    lancamentos = LancamentoFinanceiro.query.all()
    return render_template('lancamento_lista.html', lancamentos=lancamentos)

# Editar
@app.route('/lancamento/<int:id>/editar', methods=['GET', 'POST'])
def editar_lancamento(id):
    lancamento = LancamentoFinanceiro.query.get_or_404(id)
    form = LancamentoForm(obj=lancamento)

    form.produto.choices = [(p.id, p.nome) for p in Produto.query.all()]
    form.fornecedor.choices = [(f.id, f.nome) for f in Fornecedor.query.all()]

    if form.validate_on_submit():
        lancamento.produto_id = form.produto.data
        lancamento.fornecedor_id = form.fornecedor.data
        lancamento.tipo_custo = form.tipo_custo.data
        lancamento.conta_origem = form.conta_origem.data
        lancamento.forma_pagamento = form.forma_pagamento.data
        lancamento.status = form.status.data
        lancamento.valor = form.valor.data

        BancoDeDados.session.commit()
        return redirect(url_for('listar_lancamento'))

    return render_template('lancamento_form.html', form=form)

# Deletar
@app.route('/lancamento/<int:id>/deletar', methods=['POST'])
def deletar_lancamento(id):
    lancamento = LancamentoFinanceiro.query.get_or_404(id)

    BancoDeDados.session.delete(lancamento)
    BancoDeDados.session.commit()

    return redirect(url_for('listar_lancamento'))