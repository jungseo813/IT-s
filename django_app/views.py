from django.shortcuts import render


def join_view(request):
    return render(request, 'join.html')

def login_view(request):
    return render(request, 'login.html')
