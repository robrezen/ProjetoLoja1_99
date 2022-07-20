from django.db import models

# Create your models here.

class Vendedor(models.Model):
    cpf_vendedor = models.IntegerField(primary_key=True, default=0)
    nome_vendedor = models.CharField(max_length=30, null=False)
    data_admissao = models.DateField(auto_now=True)
    salario_bruto = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    salario_liquido = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    percentual_comissao = models.DecimalField(max_digits=3, decimal_places=2)
    quantidade_vendas = models.IntegerField(null=False)

class Cliente(models.Model):
    cpf_cliente = models.IntegerField(primary_key=True, default=0)
    nome_cliente = models.CharField(max_length=30, null=False)
    nivel = models.IntegerField(null=True) 
    email = models.CharField(max_length=30, null=False)
    telefone = models.IntegerField(null=True)

class Produto(models.Model):
    num_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=30, null=False)
    valor_produto = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    quantidade_produto = models.IntegerField(null=False)

class Venda(models.Model):
    num_venda = models.AutoField(primary_key=True)
    data_venda = models.DateField(auto_now=True, null=False)
    valor = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    percentual_desc = models.DecimalField(max_digits=3, decimal_places=2)
    cpf_vendedor = models.IntegerField(default=0)
    cpf_cliente = models.IntegerField(default=0)
    cod_produto =  models.IntegerField(default=0)
    quantidade = models.IntegerField(null=False, default = 1)

class Venda_Produto(models.Model):
    num_venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    cod_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False)

