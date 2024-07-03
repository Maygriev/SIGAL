from django.shortcuts import render, redirect

from apps.usuario.forms import LoginForms, CadastroForms

from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nomeLogin = form["nome_login"].value()
            senhaLogin = form["senha"].value()

            usuario = auth.authenticate(
                request,
                username=nomeLogin,
                password=senhaLogin
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nomeLogin} logado com sucesso!")
                return redirect("index")
            else:
                messages.error(request, "Usuário ou senha incorretos.")
                return redirect("login")
                
    return render(request, "usuario/login.html", {"form": form})
    
def cadastro(request):
    pass

def logout_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    messages.success(request, f"{request.user} deslogado com sucesso!")
    logout(request)
    return redirect('login')
    