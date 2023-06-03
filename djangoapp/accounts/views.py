from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def renderiza(request):
    return render(request, 'accounts/accounts.html')


def login(request):
    if request.method != 'POST':
        return redirect('accounts:renderiza')

    usuario = request.POST.get('username')
    senha = request.POST.get('password')

    if not usuario or not senha:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return redirect('accounts:renderiza')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return redirect('accounts:renderiza')

    auth.login(request, user)
    messages.success(request, 'Logado com sucesso!')
    return redirect('produto:produtos')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuário deslogado.')
    return redirect('produto:produtos')


def register(request):
    if request.method != 'POST':
        return redirect('accounts:renderiza')

    nome = request.POST.get('nome')
    sobrenomenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenomenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return redirect('accounts:renderiza')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return redirect('accounts:renderiza')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return redirect('accounts:renderiza')
    if len(usuario) < 6:
        messages.error(request, 'Usuario precisa ter 6 caracteres ou mais.')
        return redirect('accounts:renderiza')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return redirect('accounts:renderiza')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return redirect('accounts:renderiza')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe.')
        return redirect('accounts:renderiza')

    messages.success(request, 'Registrado com sucesso! Agora faça login.')

    user = User.objects.create_user(username=usuario, email=email, password=senha,
                                    first_name=nome, last_name=sobrenomenome)
    user.save()

    return redirect('accounts:renderiza')
