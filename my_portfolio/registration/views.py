from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# views.py
from django.shortcuts import render
from .models import HomePage, JourneyHighlight, CarouselImage
from django.contrib.auth.decorators import login_required
from .forms import *
from django.forms.models import model_to_dict

def home(request):
    home_page = HomePage.objects.last() 
    highlights = JourneyHighlight.objects.all()
    context = {
        'home_page': model_to_dict(home_page), 
        'highlights': highlights,
        "carousel_images": CarouselImage.objects.all()
    }
    return render(request, 'registration/home.html', context)

# def home(request):
#     return render(request, 'registration/home.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
        else:
            # Handle invalid login (e.g., display error messages)
            print("Invalid login") 
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_home_page(request):
    if request.method == 'POST':
        form = HomePageForm(request.POST)
        if form.is_valid():
            home_page = form.save()
            return redirect('home') 
    else:
        form = HomePageForm()
    return render(request, 'registration/create_home_page.html', {'form': form})

@login_required
def update_home_page(request, pk):
    home_page = get_object_or_404(HomePage, pk=pk)
    if request.method == 'POST':
        form = HomePageForm(request.POST, instance=home_page)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomePageForm(instance=home_page)
    return render(request, 'registration/update_home_page.html', {'form': form})

@login_required
def delete_home_page(request, pk):
    home_page = get_object_or_404(HomePage, pk=pk)
    home_page.delete()
    return redirect('home')  # Redirect to the home page after deletion

@login_required
def create_carouseImage(request):
    if request.method == 'POST':
        form = CarouselImageForm(request.POST, request.FILES)
        print("===", form)
        if form.is_valid():
            carouseImage = form.save()
            return redirect('home')
    else:
        form = CarouselImageForm()
    return render(request, 'registration/create_carousel_image.html', {'form': form})

@login_required
def update_carouseImage(request, pk):
    carouseImage = get_object_or_404(CarouselImage, pk=pk)
    if request.method == 'POST':
        form = CarouselImageForm(request.POST, instance=carouseImage)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarouselImageForm(instance=carouseImage)
    return render(request, 'registration/update_carousel_image.html', {'form': form})

@login_required
def delete_carouseImage(request, pk):
    carouseImage = get_object_or_404(CarouselImage, pk=pk)
    carouseImage.delete()
    return redirect('carouseImage')  # Redirect to the home page after deletion

@login_required
def create_journeyHighlight(request):
    if request.method == 'POST':
        form = JourneyHighlightForm(request.POST)
        if form.is_valid():
            journeyHighlight = form.save()
            return redirect('home') 
    else:
        form = JourneyHighlightForm()
    return render(request, 'registration/create_journeyHighlight.html', {'form': form})

@login_required
def update_journeyHighlight(request, pk):
    journeyHighlight = get_object_or_404(JourneyHighlight, pk=pk)
    if request.method == 'POST':
        form = JourneyHighlightForm(request.POST, instance=journeyHighlight)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JourneyHighlightForm(instance=journeyHighlight)
    return render(request, 'registration/update_journeyHighlight.html', {'form': form})

@login_required
def delete_journeyHighlight(request, pk):
    journeyHighlight = get_object_or_404(JourneyHighlight, pk=pk)
    journeyHighlight.delete()
    return redirect('home')  # Redirect to the home page after deletion
