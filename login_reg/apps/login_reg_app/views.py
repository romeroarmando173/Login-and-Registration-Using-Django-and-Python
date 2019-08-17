from django.shortcuts import render, redirect
from .models import *
import bcrypt, re
from django.contrib import messages
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
def index(request):
    return render(request, "login_reg_app/index.html")

def registration(request):
    errors = {}
    if len(request.POST['first_name']) < 2:
        errors['fn'] = "first name need to be at least more than 2 characters"
    if len(request.POST['last_name']) < 2:
        errors['ln'] = "last name need to be at least more than 2 characters"
    if len(request.POST['password']) < 8:
        errors['pw'] = "your passwrd need to b longer than 8 char"
    if request.POST['password'] != request.POST['c_password']:
        errors['cpw'] = "niggah u trippin, make sure passwords match"
    if not EMAIL_REGEX.match(request.POST['email']):
        errors['emailregex'] = "!!!!!____BAD EMAIL BAD CREDENTIALS_____!!!!!!"

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = bcrypt.hashpw(request.POST['password'].encode('utf8'), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], 
        email = request.POST['email'], password = password)
        request.session['user_id']=user.id
        return redirect("/success")

def success(request):
    context = {
       "user": User.objects.get(id = request.session['user_id']),  #if you get a key error, is because you tried loggin in someone whom does not exist in db
       "quoteAll": Quote.objects.all(),   # this variable will be used in jinja
                                          #    "AuthorWhoWroteTheQuote": User.objects.all(),
     }
    return render(request, "login_reg_app/success.html", context)

def login(request):
    errors = {}
    if not EMAIL_REGEX.match(request.POST['email']):
        errors['emailregex'] = "!!!BAD EMAIL BAD CREDENTIALS_____!!!!!!"

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        match_user = User.objects.filter(email= request.POST['email']) # [ {"id": 1, ...} ], get {}
        if len(match_user) > 0:
            user = match_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):     # you did not need .encode() here
                request.session['user_id'] = user.id
                return redirect("/success")
            else:
                messages.error(request, "!!!!!____BAD EMAIL BAD CREDENTIALS___!!!!!!")
                return redirect('/')
        else:
            messages.error(request, "!!!!___BAD EMAIL BAD CREDENTIALS___!!!!!!")
            return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def addquote(request):
    errors = {}
    if len(request.POST['author']) < 3:
        errors['au'] = "author need to be at least more than 2 character"
    if len(request.POST['content']) < 10:
        errors['co'] = "quote need to be at least more than 2 characters"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect("/success")
    else:
        user=User.objects.get(id=request.session['user_id'])   
        Quote.objects.create(author= request.POST['author'], content= request.POST['content'], userQuote = user)   # userQuote here was used from models.py and also in jinja
        return redirect("/success")
        
def posterPage(request,user_id):  # pay attention how the user_id got passed here # the user_id here actually gets passed down to the next line wehre you see id=user_id BUT its original createion is in the success.html here at bottom of jenja page :{{quote.userQuote.id}}"
    user = User.objects.get(id=user_id)    # this is reflecting the user with pertaining id
    context = {                            #if you get a key error, is because you tried loggin in someone whom does not exist in db
        "quoteAll": Quote.objects.filter(userQuote=user), 
        'user': user                                                          # "AuthorWhoWroteTheQuote": User.objects.all(),
     }
    return render(request, "login_reg_app/posterPage.html", context)

def myAccount(request, user_id):    # user_id is written here in this syntax-manner because its similar to the way views does their syntax
    return render(request, "login_reg_app/myAccount.html")

def UpdateDB1(request, user_id):
    user= User.objects.get(id=user_id)  # auto increment id and url id 
    user.first_name=request.POST['first']
    user.first_name=request.POST['first']
    user.save()
    return redirect('/success')

def delete(request, quote_id): #always pass id when you are deleting , this would be your quote id since its specific
    Quote.objects.get(id=quote_id).delete()
    return redirect("/success")
# def add_like(request, quote_id):
#     User.objects.get(id = request.sessions['user_id'])
#     quote = Quote.objects.get(id=)