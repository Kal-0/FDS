from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Category, Item, Profile
from .forms import SignupForm, ItemForm

def home(request):
    return render(request,"home.html")

def feed(request):
    items = Item.objects.filter(check_sold=False)
    categories = Category.objects.all()

    return render(request, 'feed_db.html', {
        'cats' : categories,
        'pub': items,
    })

def page_categoria(request, foto_id):
    categories = get_object_or_404(Category, pk=foto_id)
    items = Item.objects.filter(check_sold=False).filter(category=categories.id)
    return render(request, 'categoria.html', {
        'categories' : categories,
        'pub': items,       
    })

def produto_detalhes(request, foto_id):
    items = get_object_or_404(Item, pk=foto_id)
    return render(request, 'interno_publicacao.html', {
        'items': items,
    })

def test(request):
    number = 0
    namels=["bebel","caio","diogo"]
    return render(request, "test.html", {"namels":namels, "number": number})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {'username': username}
            return render(request, "home.html", context)
        else:
            messages.success(request, ("There Was An Error Loggin In, Try Again..."))
            return redirect('login')
    else:
        context = {'username': ''}
        return render(request, "login.html", context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignupForm()
        
    return render(request, 'cadastro.html', {
        'form': form
    })

def publicacao_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = SignupForm()
        
    return render(request, 'cadastro.html', {
        'form': form
    })

def perfil(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, "perfil.html", {'user_profile': user_profile})

def buscar(request):
    return render(request, "buscar.html")

def create_item(request):
    print(f"GET: {request.GET}")
    print(f"POST: {request.POST}")
    
    if request.method == 'POST':
        user = request.user
        print(user)
        
        if request.POST.get("productName") != "":
            inProductName = request.POST.get("productName")
            print(inProductName)
            
           
        if request.POST.get("productPrice") != None:
            inProductPrice = request.POST.get("productPrice")
            print(inProductPrice)
            
            
        inProductDescription = request.POST.get("productDescription")
        print(inProductDescription)
        
        
        inProductCategory = Category.objects.get(name = request.POST.get("productCategory"))
        print(inProductCategory)
        
        print(Category.objects.get(name = "dede"))
        
        
        inProductImage = request.POST.get("productImage")
        print(inProductImage)
        
        
        Item.objects.create(name=inProductName, price=inProductPrice, description=inProductDescription, category=inProductCategory, image=inProductImage, created_by = user)
        
        
    return render(request, 'base_publicacao.html', {})
