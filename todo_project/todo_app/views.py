
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import AppUser as User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict

from .models import AppUser as User, ToDo


@csrf_exempt
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'todo_app/signup.html')

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            # User.objects.create_user(username=body['email'], email=body['email'], password=body['password'])
            return JsonResponse({'success':True})
        except Exception as e:
            print(str(e))
            return JsonResponse({'success':False})


@csrf_exempt
def log_in(request):
    if request.method == 'GET':
        return render(request, 'todo_app/login.html')
    
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body['email']
        password = body['password']
    
        # remember, we told django that our email field is serving as the 'username' 
        # this doesn't start a login session, it just tells us which user from the db belongs to these credentials
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                try:
                    # this method actually sets a cookie to start a session
                    login(request,user)
                    print('logged in!')
                    return JsonResponse({'Success': True})
                except Exception as e:
                    return JsonResponse({'Success': False, 'reason': 'login failed'})
            else:
                return JsonResponse({'Success': False, 'reason': 'account disabled'})
        else:
            return JsonResponse({'Success': False, 'reason': 'user does not exist'})

@csrf_exempt
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')

@csrf_exempt
def who_am_i(request):
    print(dir(request.user))
    if request.user.is_authenticated:
        return JsonResponse({
            'email': request.user.email
        })
    else:
        return JsonResponse({'user':None})

@csrf_exempt
def new_todo(request):
    if request.method == 'GET':
        return render(request, 'todo_app/new_todo.html')
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            todo = ToDo(title = body["title"], description = body["description"], user = request.user)
            todo.save()
            return JsonResponse({'success':True})
        except Exception as e:
            print(str(e))
            return JsonResponse({'success':False})

@csrf_exempt
def view_todos(request):
    todo_list = []
    todos = ToDo.objects.filter(user = request.user)
    for todo in todos.values():
        todo_list.append(todo)   
    return render(request, 'todo_app/view_todos.html', {"todo_dict":todo_list, "name":request.user.username})

@csrf_exempt
def todo_detail(request,id):
    todo = ToDo.objects.get(pk=id)
    return render(request, 'todo_app/todo_detail.html', {"todo":todo})

@csrf_exempt
def edit_todo(request, id):
    todo = ToDo.objects.get(pk=id) 
    if request.method == 'GET':
        return render(request, 'todo_app/edit_todo.html',{"todo":todo})
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            todo.title = body["title"]
            todo.description = body["description"]
            todo.save()
            return JsonResponse({'success':True})
        except Exception as e:
            print(str(e))
            return JsonResponse({'success':False})

@csrf_exempt
def delete_todo(request, id):
    todo = ToDo.objects.get(pk=id) 

    try:
        todo.delete()
        return HttpResponseRedirect('/todos')
    except Exception as e:
        print(str(e))
        return JsonResponse({'success':False})
