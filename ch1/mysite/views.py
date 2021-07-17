from django.contrib.auth.decorators import login_required
from hint.models import Theme
from accounts.models import Profile
from .forms import HintForm
from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404, HttpResponse, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import (logout as django_logout)
from django.contrib import auth

def signin(request):
    if request.COOKIES.get('username') is not None:
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        method = request.COOKIES.get('method')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if method == "pc":
                return HttpResponseRedirect(reverse('theme_list', args=[user.username]))
            else:
                return HttpResponseRedirect(reverse('theme_list', args=[user.username]))
        else:
            return render(request, 'accounts/login_fail.html')

    elif request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        method = request.POST['method']
        print(method)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            if method == "pc":
                response = HttpResponseRedirect(reverse('theme_list', args=[user.username]))
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                response.set_cookie('method', method)
                return response

            else:
                response = HttpResponseRedirect(reverse('theme_list', args=[user.username]))
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                response.set_cookie('method', method)
                return response
        else:
            return render(request, 'accounts/login_fail.html')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {
            'form': form
        })


def logout(request):
    # django_logout(request)
    response = HttpResponseRedirect(reverse('login'))
    response.delete_cookie('username')
    response.delete_cookie('password')
    response.delete_cookie('method')
    return response




@login_required
def theme_list(request, user_id):
    profile = get_object_or_404(Profile, user=request.user)
    themes = Theme.objects.all()
    themes = themes.filter(roomEscape=profile)
    escape_room = profile.escape_room
    return render(request, 'theme/theme_list.html', {
        'themes': themes,
        'escape_room': escape_room,
        'user_id': user_id
    })


@login_required
def theme_edit(request, user_id, theme):
    profile = get_object_or_404(Profile, user=request.user)
    nation = profile.nation
    escape_room = profile.escape_room
    theme = get_object_or_404(Theme, name=theme, roomEscape=profile)
    textHint = profile.textHint
    manyHint = theme.manyHint
    timer = profile.timer

    if request.method == 'POST':
        form = HintForm(request.POST, request.FILES, instance=theme)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.roomEscape = profile
            theme.save()
            return HttpResponseRedirect(reverse('theme_list', args=[request.user.username]))
        else:
            print(form.errors)
    else:
        form = HintForm(instance=theme)
    return render(request, 'theme/theme_edit.html', {
        'form': form,
        'theme': theme,
        'escape_room': escape_room,
        'user_id': user_id,
        'nation': nation,
        'textHint': textHint,
        'manyHint': manyHint,
        'timer': timer,
    })

def ajax(request, user_id, theme):
    theme = get_object_or_404(Theme, name=theme, roomEscape=request.user)
    print(theme)
    data = request.GET['msg']
    if data == '1':
        theme.sub_hint1.delete()
    elif data == '2':
        theme.sub_hint2.delete()
    elif data == '3':
        theme.sub_hint3.delete()
    elif data == '4':
        theme.sub_hint4.delete()
    elif data == '5':
        theme.sub_hint5.delete()
    elif data == '6':
        theme.sub_hint6.delete()
    elif data == '7':
        theme.sub_hint7.delete()
    elif data == '8':
        theme.sub_hint8.delete()
    elif data == '9':
        theme.sub_hint9.delete()
    elif data == '10':
        theme.sub_hint10.delete()
    elif data == '11':
        theme.sub_hint11.delete()
    elif data == '12':
        theme.sub_hint12.delete()
    elif data == '13':
        theme.sub_hint13.delete()
    elif data == '14':
        theme.sub_hint14.delete()
    elif data == '15':
        theme.sub_hint15.delete()
    elif data == '16':
        theme.sub_hint16.delete()
    elif data == '17':
        theme.sub_hint17.delete()
    elif data == '18':
        theme.sub_hint18.delete()
    elif data == '19':
        theme.sub_hint19.delete()
    elif data == '20':
        theme.sub_hint20.delete()

    return HttpResponse(data)
