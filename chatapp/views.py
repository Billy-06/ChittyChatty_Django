from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Message

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('chat')
    else:
        form = UserRegisterForm()
    return render(request, 'chatapp/register.html', {'form': form})

@login_required
def chat_view(request):
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Message.objects.create(user=request.user, content=content)
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'chatapp/chat.html', {'messages': messages})
