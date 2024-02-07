from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from tasks.forms import TaskForm, UpdateForm, NewUserForm, ProfileUpdateForm
from tasks.models import Tasks

def home(req):
    return render(req, "home.html")

def signup(req):
    if req.method == "POST":
        f = NewUserForm(req.POST)
        if f.is_valid():
            user = f.save()
            if user is not None:
                return redirect('login')
        else:
            return render(req, "signup.html", {'form':f})
    f = NewUserForm()
    return render(req, "signup.html", {'form':f})

def loginUser(req):
    if req.method == "POST":
        f = AuthenticationForm(data = req.POST)
        if f.is_valid():
            u = f.cleaned_data.get('username')
            p = f.cleaned_data.get('password')
            user = authenticate(username = u, password = p)
            if user is not None:
                login(req, user)
                return redirect('home')
        else:
            f = AuthenticationForm(data = req.POST)
            return render(req, "login.html", {'form':f})
    f = AuthenticationForm()
    return render(req, "login.html", {'form':f})

def contact(req):
    return render(req, "contact.html")

@login_required(login_url="login")
def neohome(req):
    if req.user.is_authenticated:
        user = req.user
        form = TaskForm()
        alltasks = Tasks.objects.filter(user = user).order_by('-status', 'due_date')
        return render(req, "neohome.html", {'form': form, 'tasks':alltasks})

@login_required(login_url="login")
def createTask(req):
    if req.user.is_authenticated:
        user = req.user
        form = TaskForm(req.POST)
        task = form.save(commit = False)
        task.user = user
        form.save()
        return redirect("neohome")

@login_required(login_url="login")
def logoutUser(req):
    logout(req)
    return redirect("home")

@login_required(login_url="login")
def deleteTask(req, id):
    Tasks.objects.get(pk = id).delete()
    return redirect('neohome')

@login_required(login_url="login")
def changeStatus(req, id):
    task = Tasks.objects.get(pk = id)
    if task.status == 'p':
        task.status = 'c'
    else:
        task.status = 'p'
    task.save()
    return redirect('neohome')

@login_required(login_url="login")
def update(req, id):
    task = Tasks.objects.get(pk = id)
    if req.method == "POST":
        task.title = req.POST.get('nt')
        task.due_date = req.POST.get('nd')
        task.save()
        return redirect('neohome')
    if req.user != task.user:
        return redirect('neohome')
    f = UpdateForm(initial={'nt':task.title, 'nd': task.due_date})
    f.base_fields['nd'].label = "New Due Date"
    return render(req, 'update.html', {'form':f})

@login_required(login_url="login")
def profileUpdate(req):
    ouser = User.objects.get(username = req.user)
    
    f = ProfileUpdateForm(initial={'first_name':req.user.first_name, 'last_name': req.user.last_name, 'email': req.user.email, 'user':req.user.username})
    
    if req.method == "POST":
        try:
            u = req.POST.get('user')
            if not str(u).isalnum():
                return render(req,"proupdate.html", {'form': f,'mes':"Error: Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters."} )
            if User.objects.filter(username = u).exists():
                render(req,"proupdate.html", {'form': f,'mes':"Error: User Name Already Exists, Choose another."} )
            ouser.username = u
            ouser.first_name = req.POST.get('first_name')
            ouser.last_name = req.POST.get('last_name')
            ouser.email = req.POST.get('email')
            ouser.save()
            return redirect('home')
        except:
            return render(req,"proupdate.html", {'form': f,'mes':"Error: User Name Already Exists"} )
        
    return render(req, "proupdate.html", {'form': f,})

@login_required(login_url="login")
def deleteProfile(req):
    User.objects.get(username = req.user).delete()
    return redirect('home')