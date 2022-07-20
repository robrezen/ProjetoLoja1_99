from django.shortcuts import render, redirect
from core.models import Vendedor, Venda, Produto, Venda_Produto, Cliente
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def render_index(request):
    return render(request, 'index.html')

def render_nothing(request):
    return redirect('/index/')

# Login e Logout

def render_login(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            messages.add_message(request, messages.INFO, 'Login realizado')
            return redirect('/index')
        else:
            messages.add_message(request, messages.ERROR, 'Usuário ou senha incorretos!')
            return redirect('/login')
    else:
        return redirect('/index')

def submit_logout(request):
    logout(request)
    return redirect('/logout_successful/')

def render_logout(request):
    return render(request, 'logout_successful.html')

# Venda

def render_administrar_venda(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'administrar-venda.html')

def render_registrar_venda(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'registrar-venda.html')

def submit_registrar_venda(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')
    if request.POST:
        cpf_vendedor = request.POST.get('cpf_vendedor')
        cod_produto = request.POST.get('codProduto')
        cpf_cliente = request.POST.get('cpf_cliente')
        quantidade = int(request.POST.get('quantidade'))
        ProdutoAtual = Produto.objects.get(num_produto=cod_produto)
        ClienteAtual = Cliente.objects.get(cpf_cliente=cpf_cliente)

        Venda.objects.create(valor = quantidade*ProdutoAtual.valor_produto,
                                percentual_desc = ClienteAtual.nivel*0.1,
                                cpf_vendedor = cpf_vendedor,
                                cpf_cliente = cpf_cliente,
                                cod_produto = cod_produto,
                                quantidade = quantidade)
        messages.add_message(request, messages.INFO, 'Venda registrada com sucesso!')
    return redirect('/administrar-venda')

def render_consultar_venda(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'consultar-venda.html')

def submit_consultar_venda(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        num_venda = request.POST.get('num_venda')
        vendas = Venda.objects.filter(num_venda=num_venda)
        dados = {'vendas':vendas}

        return render(request, 'consultar-venda-exibir.html', dados)
    
    else:
        return redirect('/index')

def render_alterar_venda(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'alterar-venda.html')
    
def render_excluir_venda(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'excluir-venda.html')

# Produto


def render_administrar_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'administrar-produto.html')


def render_registrar_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'registrar-produto.html')

def submit_registrar_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')
    if request.POST:
        nome_produto = request.POST.get('nome_produto')
        valor_produto = request.POST.get('valor_produto')
        quantidade_produto = request.POST.get('quantidade_produto')
        Produto.objects.create(nome_produto = nome_produto,
                                valor_produto = valor_produto,
                                quantidade_produto = quantidade_produto)

        produto_criado = Produto.objects.get(nome_produto=nome_produto)
        messages.add_message(request, messages.INFO, 'Produto registrado com sucesso com código ' + str(produto_criado.num_produto) + '!')

    return redirect('/administrar-produto')


def render_consultar_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'consultar-produto.html')

def submit_consultar_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        num_produto = request.POST.get('num_produto')
        nome_produto = request.POST.get('nome_produto')
        tipo_ident = request.POST.get('tipo_ident')
        
        if tipo_ident == 'num':
            produtos = Produto.objects.filter(num_produto=num_produto)
        else:
            produtos = Produto.objects.filter(nome_produto=nome_produto)
        
        dados = {'produtos':produtos}

        return render(request, 'consultar-produto-exibir.html', dados)
    
    else:
        return redirect('/index')


def render_alterar_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'alterar-produto.html')

def submit_alterar_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        num_produto = request.POST.get('num_produto')
        nome_produto = request.POST.get('nome_produto')
        tipo_ident = request.POST.get('tipo_ident')

        if tipo_ident == 'num':
            return redirect('/alterar-produto-confirma/?id=' + num_produto + '&tipo_ident=' + tipo_ident)
        else:
            return redirect('/alterar-produto-confirma/?id=' + nome_produto + '&tipo_ident=' + tipo_ident)
    
    else:
        return redirect('/index')

def render_alterar_produto_confirma(request):
    tipo_ident = request.GET.get('tipo_ident')

    if tipo_ident == 'num':
        num_produto = request.GET.get('id')
        produtos = Produto.objects.filter(num_produto=num_produto)
    else:
        nome_produto = request.GET.get('id')
        produtos = Produto.objects.filter(nome_produto=nome_produto)

    dados = {'produtos':produtos}
    return render(request, 'alterar-produto-confirma.html', dados)

def submit_alterar_produto_confirma(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        num_produto = request.POST.get('num_produto')
        nome_produto = request.POST.get('nome_produto')
        valor_produto = request.POST.get('valor_produto')
        quantidade_produto = request.POST.get('quantidade_produto')
        
        Produto.objects.filter(num_produto=num_produto).update( nome_produto=nome_produto, 
                                                                valor_produto=valor_produto, 
                                                                quantidade_produto=quantidade_produto)

        messages.add_message(request, messages.INFO, 'Produto alterado com sucesso!')
        return redirect('/administrar-produto')
    
    else:
        return redirect('/index')
    

def render_excluir_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    exibir_produto = request.GET.get('exibir_produto')
    num_produto = request.GET.get('id')
    produtos = Produto.objects.filter(num_produto=num_produto)
    
    dados = {'produtos':produtos,'exibir_produto':exibir_produto,'id':num_produto}
    
    return render(request, 'excluir-produto.html', dados)

def submit_excluir_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        num_produto = request.POST.get('num_produto')
        return redirect('/excluir-produto/?id=' + num_produto + '&exibir_produto=true')

    else:
        return redirect('/index')

def confirm_excluir_produto(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        num_produto = request.POST.get('num_produto')
        produto_a_deletar = Produto.objects.get(num_produto=num_produto)
        produto_a_deletar.delete()

        messages.add_message(request, messages.INFO, 'Produto excluído com sucesso!')
        return redirect('/administrar-produto')

    else:
        return redirect('/index')


# Vendedor

def render_administrar_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'administrar-vendedor.html')


def render_registrar_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'registrar-vendedor.html')

def submit_registrar_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')
    if request.POST:
        cpf_vendedor = request.POST.get('cpf_vendedor')
        nome_vendedor = request.POST.get('nome_vendedor')
        salario_bruto = request.POST.get('salario_bruto')
        salario_liquido = request.POST.get('salario_liquido')
        percentual_comissao = request.POST.get('percentual_comissao')
        Vendedor.objects.create(cpf_vendedor = cpf_vendedor,
                                nome_vendedor = nome_vendedor,
                                salario_bruto = salario_bruto,
                                salario_liquido = salario_liquido,
                                percentual_comissao = percentual_comissao,
                                quantidade_vendas = 0)

    messages.add_message(request, messages.INFO, 'Vendedor registrado com sucesso!')
    return redirect('/administrar-vendedor')


def render_consultar_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'consultar-vendedor.html')

def submit_consultar_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_vendedor = request.POST.get('cpf_vendedor')
        vendedores = Vendedor.objects.filter(cpf_vendedor=cpf_vendedor)
        dados = {'vendedores':vendedores}

        return render(request, 'consultar-vendedor-exibir.html', dados)
    
    else:
        return redirect('/index')


def render_alterar_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'alterar-vendedor.html')

def submit_alterar_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_vendedor = request.POST.get('cpf_vendedor')
        return redirect('/alterar-vendedor-confirma/?id=' + cpf_vendedor)
    
    else:
        return redirect('/index')

def render_alterar_vendedor_confirma(request):
    cpf_vendedor = request.GET.get('id')
    vendedores = Vendedor.objects.filter(cpf_vendedor=cpf_vendedor)
    dados = {'vendedores':vendedores}
    return render(request, 'alterar-vendedor-confirma.html', dados)

def submit_alterar_vendedor_confirma(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_vendedor = request.POST.get('cpf_vendedor')
        nome_vendedor = request.POST.get('nome_vendedor')
        salario_bruto = request.POST.get('salario_bruto')
        salario_liquido = request.POST.get('salario_liquido')
        percentual_comissao = request.POST.get('percentual_comissao')
        quantidade_vendas = request.POST.get('quantidade_vendas')
        Vendedor.objects.filter(cpf_vendedor=cpf_vendedor).update(nome_vendedor = nome_vendedor, 
                                salario_bruto=salario_bruto, 
                                salario_liquido=salario_liquido, 
                                percentual_comissao=percentual_comissao, 
                                quantidade_vendas=quantidade_vendas)

        messages.add_message(request, messages.INFO, 'Vendedor alterado com sucesso!')
        return redirect('/administrar-vendedor')
    
    else:
        return redirect('/index')
    

def render_excluir_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    exibir_vendedor = request.GET.get('exibir_vendedor')
    cpf_vendedor = request.GET.get('id')
    vendedores = Vendedor.objects.filter(cpf_vendedor=cpf_vendedor)
    
    dados = {'vendedores':vendedores,'exibir_vendedor':exibir_vendedor,'id':cpf_vendedor}
    
    return render(request, 'excluir-vendedor.html', dados)

def submit_excluir_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_vendedor = request.POST.get('cpf_vendedor')
        return redirect('/excluir-vendedor/?id=' + cpf_vendedor + '&exibir_vendedor=true')

    else:
        return redirect('/index')

def confirm_excluir_vendedor(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_vendedor = request.POST.get('cpf_vendedor')
        vendedor_a_deletar = Vendedor.objects.get(cpf_vendedor=cpf_vendedor)
        vendedor_a_deletar.delete()

        messages.add_message(request, messages.INFO, 'Vendedor excluído com sucesso!')
        return redirect('/administrar-vendedor')

    else:
        return redirect('/index')

# cliente


def render_administrar_cliente(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'administrar-cliente.html')


def render_registrar_cliente(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')
    if request.POST:
        cpf_vendedor = request.POST.get('cpf_vendedor')
        nome_vendedor = request.POST.get('nome_vendedor')
        salario_bruto = request.POST.get('salario_bruto')
        salario_liquido = request.POST.get('salario_liquido')
        percentual_comissao = request.POST.get('percentual_comissao')
        Vendedor.objects.create(cpf_vendedor = cpf_vendedor,
                                nome_vendedor = nome_vendedor,
                                salario_bruto = salario_bruto,
                                salario_liquido = salario_liquido,
                                percentual_comissao = percentual_comissao,
                                quantidade_vendas = 0)

    return render(request, 'registrar-cliente.html')

def submit_registrar_cliente(request):
    if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
            return redirect('/login')
    if request.POST:
        nome_cliente = request.POST.get('nome_cliente')
        cpf_cliente = request.POST.get('cpf_cliente')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        Cliente.objects.create(nome_cliente = nome_cliente,
                                cpf_cliente = cpf_cliente,
                                nivel = 0,
                                email = email,
                                telefone = telefone)
    
    messages.add_message(request, messages.INFO, 'Cliente registrado com sucesso!')
    return redirect('/administrar-cliente')


def render_consultar_cliente(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'consultar-cliente.html')

def submit_consultar_cliente(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_cliente = request.POST.get('cpf_cliente')
        clientes = Cliente.objects.filter(cpf_cliente=cpf_cliente)
        dados = {'clientes':clientes}

        return render(request, 'consultar-cliente-exibir.html', dados)
    
    else:
        return redirect('/index')


def render_alterar_cliente(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    return render(request, 'alterar-cliente.html')

def submit_alterar_cliente(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_cliente = request.POST.get('cpf_cliente')
        return redirect('/alterar-cliente-confirma/?id=' + cpf_cliente)
    
    else:
        return redirect('/index')

def render_alterar_cliente_confirma(request):
    cpf_cliente = request.GET.get('id')
    clientes = Cliente.objects.filter(cpf_cliente=cpf_cliente)
    dados = {'clientes':clientes}
    return render(request, 'alterar-cliente-confirma.html', dados)

def submit_alterar_cliente_confirma(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_cliente = request.POST.get('cpf_cliente')
        nome_cliente = request.POST.get('nome_cliente')
        nivel = request.POST.get('nivel')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        
        Cliente.objects.filter(cpf_cliente=cpf_cliente).update( nome_cliente=nome_cliente, 
                                                                nivel=nivel, 
                                                                email=email,
                                                                telefone=telefone)

        messages.add_message(request, messages.INFO, 'Cliente alterado com sucesso!')
        return redirect('/administrar-cliente')
    
    else:
        return redirect('/index')

def render_excluir_cliente(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    exibir_cliente = request.GET.get('exibir_cliente')
    cpf_cliente = request.GET.get('id')
    clientes = Cliente.objects.filter(cpf_cliente=cpf_cliente)
    
    dados = {'clientes':clientes,'exibir_cliente':exibir_cliente,'id':cpf_cliente}
    
    return render(request, 'excluir-cliente.html', dados)

def submit_excluir_cliente(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_cliente = request.POST.get('cpf_cliente')
        return redirect('/excluir-cliente/?id=' + cpf_cliente + '&exibir_cliente=true')

    else:
        return redirect('/index')

def confirm_excluir_cliente(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Para acessar esta página é necessário estar autenticado!')
        return redirect('/login')

    if request.POST:
        cpf_cliente = request.POST.get('cpf_cliente')
        cliente_a_deletar = Cliente.objects.get(cpf_cliente=cpf_cliente)
        cliente_a_deletar.delete()

        messages.add_message(request, messages.INFO, 'Cliente excluído com sucesso!')
        return redirect('/administrar-cliente')

    else:
        return redirect('/index') 
    

def render_lista_vendas(request):
    lista_vendas = Venda.objects.all().order_by('-num_venda')
    return render(request, 'lista-vendas.html', {'lista_vendas':lista_vendas})

def render_lista_vendedores(request):
    lista_vendedores = Vendedor.objects.all().order_by('-nome_vendedor')
    return render(request, 'lista-vendedores.html', {'lista_vendedores':lista_vendedores})

def render_lista_produtos(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'lista-produtos.html', {'lista_produtos':lista_produtos})

def render_lista_clientes(request):
    lista_clientes = Cliente.objects.all().order_by('-nome_cliente')
    return render(request, 'lista-clientes.html', {'lista_clientes':lista_clientes})


