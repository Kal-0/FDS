from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Category, Item, Profile, Carrinho, Historico
from .forms import SignupForm, ItemForm, ProfileForm




def home(request):
    
    #print(request.session["username"])
    
    context = {"username"}
    return render(request,"home/home.html")

def feed(request):
    items = Item.objects.filter(check_sold=False)
    categories = Category.objects.all()

    return render(request, 'home/feed.html', {
        'cats' : categories,
        'pub': items,
    })

def page_categoria(request, foto_id):
    categories = get_object_or_404(Category, pk=foto_id)
    items = Item.objects.filter(check_sold=False).filter(category=categories.id)
    return render(request, 'home/categoria.html', {
        'categories' : categories,
        'pub': items,       
    })

def produto_detalhes(request, foto_id):
    items = get_object_or_404(Item, pk=foto_id)
    categories = Category.objects.filter(id=items.category.id)
    context = {
        'items': items,
        'cat': categories,
    }
    return render(request, 'home/interno_publicacao.html', context)

def test(request):
    number = 0
    namels=["bebel","caio","diogo"]
    return render(request, "home/test.html", {"namels":namels, "number": number})

def login_user(request):
    
    request.user = None
    #request.session["user"] = None
    #print(request.session["user"])
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #print(f"user: {user}")
        if user is not None:
            login(request, user)
            
            #cria perfil
            print(f"user: {request.user}")
            #print(Profile.objects.filter(user=request.user))
            if not Profile.objects.filter(user=request.user):
                
                #print("criou")
                Profile.objects.create(user=request.user, name=username)
            
            #request.session["username"] = username
            return redirect("home")
        else:
            messages.success(request, ("There Was An Error Loggin In, Try Again..."))
            return redirect('login')
    else:
        context = {'username': ''}
        return render(request, "home/login.html", context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
    
            return redirect('login')
    else:
        form = SignupForm()
        
    return render(request, 'home/cadastro.html', {
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
        
    return render(request, 'home/cadastro.html', {
        'form': form
    })

def perfil(request):
    items = Item.objects.filter(check_sold=False)
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Handle the case where the user does not have a profile
        return redirect('login')
    return render(request, "home/perfil.html", {
        'user_profile': user_profile,
        'pub': items,
        })

def create_item(request):
    #print(f"GET: {request.GET}")
    #print(f"POST: {request.POST}")
    
    if request.method == 'POST':
        user = request.user
        print(user)
        
        if request.POST.get("productName") != "" and request.POST.get("productName") != None:
            inProductName = request.POST.get("productName")
            print(inProductName)
        else:
            return render(request, 'home/criando_publicacao.html', {})
           
        if request.POST.get("productPrice") != None:
            inProductPrice = request.POST.get("productPrice")
            print(inProductPrice)
        else:
            return render(request, 'home/criando_publicacao.html', {})    
            
        inProductDescription = request.POST.get("productDescription")
        print(inProductDescription)
        
        inProductCategory=None
        if Category.objects.filter(name=request.POST.get("productCategory")):
            inProductCategory = Category.objects.get(name = request.POST.get("productCategory"))
            print(inProductCategory)
        
            #print(Category.objects.get(name= request.POST.get("productCategory")))
            
        else:
            Category.objects.create(name= request.POST.get("productCategory"))
            inProductCategory = Category.objects.get(name = request.POST.get("productCategory"))
        
        
        inProductImage = request.POST.get("productImage")
        print(inProductImage)
        
        
        Item.objects.create(name=inProductName, price=inProductPrice, description=inProductDescription, category=inProductCategory, image=inProductImage, created_by = user)
        
        
    return render(request, 'home/criando_publicacao.html', {})

def carrinho(request):
    user_profile = Profile.objects.get(user=request.user)
    user_car = Carrinho.objects.filter(user=user_profile.id, status=True)
    items = Item.objects.filter(check_sold=False)

    valor_total = 0
    itens_quant = 0

    for carrinho in user_car:
        for item in items:
            if carrinho.itens_carrinho == item:
                valor_total += item.price
                itens_quant += 1

    return render(request, "home/carrinho.html", {
        'user_carrinho': user_car,
        'pub': items,
        'valor_total': valor_total,
        'itens_quant': itens_quant,
    })

def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=user_profile)
    if  request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
           form.save()
           print("SALVEI")
           return redirect('perfil')
    context={'form': form}

    return render(request, "home/edit_profile.html", context) 

from django.shortcuts import get_object_or_404, redirect
from .models import Item, Carrinho

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    Carrinho.objects.create(
        user=request.user.profile,
        itens_carrinho=item
    )

    return redirect('carrinho')

def remove_cart(request, car_id):
    cart = get_object_or_404(Carrinho, id = car_id)
    cart.delete()

    return redirect('carrinho')

def finalizar_cart(request, car_id):
    cart = get_object_or_404(Carrinho, id = car_id)

    cart.status = False
    cart.save()

    return redirect('carrinho')

def add_to_compra(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    Carrinho.objects.create(
        user=request.user.profile,
        itens_carrinho=item,
        status = False
    )

    return redirect('feed')

def painel_de_vendas_negociações(request):
    user = request.user
    user_car = Carrinho.objects.filter(status=False)
    items = Item.objects.filter(created_by=user, check_sold=False)

    context={
        'user_carrinho': user_car,
        'pub': items,
    }
    return render(request, 'home/panel_de_vendas_negociações.html', context)

def confimar_venda(request, car_id):
    cart = get_object_or_404(Carrinho, id = car_id)

    Historico.objects.create(
        user_client = cart.user,
        user_vendodor = request.user.profile,
        item_id = cart.itens_carrinho,
    )

    cart.delete()

    return redirect('painel_de_vendas_negociações')

def painel_de_vendas_vendas(request):
    return render(request, 'home/panel_de_vendas_vendas.html')

def painel_de_vendas_estoque(request):
    return render(request, 'home/panel_de_vendas_estoque.html')

def config(request):
    return render(request, 'home/configs.html')

def busca(request):
    return render(request, 'home/busca.html')