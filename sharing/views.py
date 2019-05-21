from django.shortcuts import render, redirect
from .models import UploadModel
from .forms import UploadForm
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from background_task import background
from django.utils import timezone


def signup(request):
    if request.method == 'POST':
        form_signup = UserCreationForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            return redirect('index')
    else:
        form_signup = UserCreationForm()
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'registration/signup.html', {'form_signup': form_signup})


@login_required()
def show_files(request):
    file_posts = UploadModel.objects.filter(author=request.user)
    return render(request, 'sharing/my_uploading.html', {'file_posts': file_posts})


def new_page(request, pk):
    file = get_object_or_404(UploadModel, pk=pk)
    return render(request, 'sharing/file_page.html', {'file': file})


def handler404(request):
    return render(request, 'error/404.html', status=404)


def add_new(request):
    form_upload = UploadForm(request.POST, request.FILES, prefix='upload_form')
    if form_upload.is_valid() and request.is_ajax():
        new_file = form_upload.save(commit=False)
        new_file.author = request.user
        new_file.created_date = timezone.now()
        print(new_file.ended_date, timezone.now())
        if new_file.ended_date > timezone.now():
            new_file.is_worked = True
        else:
            new_file.is_worked = False
        new_file.save()
        return redirect('index')
    form_upload = UploadForm()
    return render(request, 'sharing/index.html', {'form_upload': form_upload})


@background(schedule=timedelta(minutes=20))
def print_hello():
    print('hello')
