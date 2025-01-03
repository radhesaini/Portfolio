from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            from django.contrib.auth import login
            login(request, user)
            return redirect('portfolio')

    else:
        form = UserCreationForm()
    return render(request, 'portfolio/register.html', {'form': form})

def portfolio_view(request):
    project = Project.objects.all()
    context = {'projects': project}
    print(project)
    return render(request, 'portfolio/portfolio.html', context)

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect('portfolio')
        else:
            return render(request, 'portfolio/create_project.html', {'form': form})
    else:
        form = ProjectForm()
    return render(request, 'portfolio/create_project.html', {'form': form})