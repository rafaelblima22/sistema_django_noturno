from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Paciente

# Create your views here.
@login_required
def index(request):
    pacientes = Paciente.objects.all()
    return render(request, "index.html",{'pacientes':pacientes})

@login_required
def novoPaciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        Paciente.objects.create( 
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento
        )
        return redirect("/novoPacienteSucesso")
    return render(request, "novo-paciente.html")

@login_required
def novo_paciente_sucesso(request):
    return render(request, "novo-paciente-sucesso.html")

@login_required
def alterar_paciente(request, codigo_paciente):
    paciente = Paciente.objects.get(codigo_paciente=codigo_paciente)
    if request.method == 'POST':
        paciente.nome = request.POST.get('nome')
        paciente.cpf = request.POST.get('cpf')
        paciente.email = request.POST.get('email')
        paciente.telefone = request.POST.get('telefone')
        paciente.data_nascimento = request.POST.get('data_nascimento')

        paciente.save()

        return redirect('index')
    return render(request, "alterar_dados.html", {'paciente':paciente})