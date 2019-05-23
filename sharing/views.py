from django.shortcuts import render, redirect
from .models import UploadModel
from .forms import UploadForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from datetime import date, datetime


def log_in(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form_signup = UserCreationForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            return redirect('index')
    else:
        form_signup = UserCreationForm()
    return render(request, 'registration/signup.html', {'form_signup': form_signup})


@login_required()
def show_files(request):
    """ Function returns all files, which user uploaded. """

    file_posts = UploadModel.objects.filter(author=request.user)
    return render(request, 'sharing/my_uploading.html', {'file_posts': file_posts})


def file_page(request, pk):
    """ Function returns page with file by PrimaryKey. If time is expired returns error 404. """

    file = get_object_or_404(UploadModel, pk=pk)
    if not file.is_worked:
        return render(request, 'error/404.html', status=404)
    return render(request, 'sharing/file_page.html', {'file': file})


def handler404(request):
    """ Function returns error 404. """

    return render(request, 'error/404.html', status=404)


def add_new(request):
    """ Function which upload new file to UploadModel. """

    form_upload = UploadForm(request.POST, request.FILES, prefix='upload_form')
    if form_upload.is_valid() and request.is_ajax():
        new_file = form_upload.save(commit=False)
        new_file.author = request.user
        new_file.created_date = date.today()
        new_file.is_worked = True
        if new_file.ended_date <= date.today():
            print('Delete ' + new_file.title + ': ' + str(datetime.now()))
            new_file.is_worked = False
            new_file.delete()
        else:
            new_file.is_worked = True
        new_file.save()
        return redirect('index')
    form_upload = UploadForm()
    return render(request, 'sharing/index.html', {'form_upload': form_upload})
