import bcrypt
from django.shortcuts import render, redirect
from store_app.models import User, Item
from django.contrib import messages
from django.db.models import Sum

def index(request):
    context = {
        "all_users" : User.objects.all()
    }
    return render (request, "index.html", context)

def register_user(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')
    password = request.POST['password']
    hashed_password = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
    print(hashed_password)
    new_user = User.objects.create(
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        email_address = request.POST['email'],
        password = hashed_password,
    )
    print(new_user.id, "THIS SHOULD BE A USER ID")
    request.session['user_id']  = new_user.id
    return redirect('/success')

def login(request):
    print('THIS IS BEFORE.......')
    # print(request.POST['email'], request.POST['password'])
    user_from_db = User.objects.filter(email_address=request.POST['email'])
    # print(user_from_db.email, "there should be an email", user_from_db.password, "there should be a password")
    if user_from_db:
        user_to_login = user_from_db[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user_to_login.password.encode()):
            request.session['user_id'] = user_to_login.id
            return redirect('/success')
        messages.error(request, "Wrong password, try again.")
    return redirect('/')

def log_out(request):
    request.session.flush()
    return redirect('/')

def success(request):
    context = {
        'logged_in_user' : User.objects.get(id=request.session['user_id'])
    }
    if not request.session['user_id']:
        return redirect('/')
    return render(request, 'success.html', context)

def account_information(request):
    return render(request, 'account_information.html')

def action(request):
    return render(request, 'action.html')

def comedy(request):
    return render(request, 'comedy.html')

def drama(request):
    return render(request, 'drama.html')

def electronics(request):
    context = {
         "electronic_list" : Item.objects.all()
    }
    return render(request, 'electronics.html', context)

def scifi(request):
    return render(request, 'scifi.html')

def cart(request, item_id):
    # get list of items the CURRENT user has added
    user = User.objects.get(id=request.session['user_id'])
    cart = Item.objects.get(id=item_id)
    context = {
        "cart" : user.items.all(),
    }
    return render(request, 'cart.html',  context)

def main_cart(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        "cart" : user.items.all(),
        'logged_in_user' : User.objects.get(id=request.session['user_id'])
    }
    if not request.session['user_id']:
        return redirect('/')
    return render(request, 'cart.html', context)

def add_to_cart(request, item_id):
        # ORM command to add item to user's cart
        current_item = Item.objects.get(id=item_id) 
        current_user = User.objects.get(id=request.session['user_id'])
        current_item.user.add(current_user)
        return redirect(f"/cart/{item_id}")

def delete(request, item_id):
        current_item = Item.objects.get(id=item_id)
        current_user = User.objects.get(id=request.session['user_id'])
        current_item.user.remove(current_user)
        return redirect(f'/cart/{item_id}')

def checkout(request):
    user = User.objects.get(id=request.session['user_id'])
    print("BEFORE SUM FUNCTION")

    # print(sum)
    context = {
        'total' : user.items.all().aggregate(Sum('price')),
        "cart" : user.items.all(),
    }
    return render(request, 'checkout.html', context)
    