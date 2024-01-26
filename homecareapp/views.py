from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from .forms import *
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseBadRequest

# Create your views here.
def index(request):
    return render(request, "homecareapp/index.html")

def about(request):
    return render(request, "homecareapp/about.html")

def faq(request):
    template = 'homecareapp/faq.html'     
    faq_results = FAQ.objects.all;
     
    context = {
        'faq_results' : faq_results
    }    
    return render(request, template, context)            

def dashboard(request):
    return render(request, "homecareapp/dashboard.html")

def search(request):
    return render(request, "homecareapp/search.html")

def searchResults(request):
    return render(request, "homecareapp/searchResults.html")

# authentication
def register(request):
    '''
    user registration view
    '''
    registered = False
    
    if request.method == 'POST':        
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
           
            if 'first_name' in user_form.cleaned_data:
                profile.first_name = request.DATA['first_name']
            if 'last_name' in user_form.cleaned_data:
                profile.last_name = request.DATA['last_name']   
            if 'mobile' in user_form.cleaned_data:
                profile.mobile = request.DATA['mobile']  
            if 'status' in user_form.cleaned_data:
                profile.status = request.DATA['status']                                                   
                                                                      
            profile.save()            
            registered = True
            return redirect('/login/') 
            
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # build the page context
        user_form = UserForm()
        user_form.password = ""
        
        template = 'homecareapp/register.html'
        context = { 
                    'user_form': user_form, 
                    'profile_form': UserProfileForm(), 
                    'registered': registered 
                    }
        
        # render the page with context
        return render(request, template, context)


def user_login(request):
    '''
    user login view
    '''
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(username=username, password=password)

        if not user:
            # invalid credentails. return.
            template = 'homecareapp/login.html'            
            context = {
                        'user_form': UserForm(), 
                        'error': "Invalid login details supplied." 
                    }            
            return render(request, template, context)                
        
        if user.is_active:
            login(request, user)
            return redirect('/home/{}'.format(request.user.id))  
        else:
            return HttpResponseForbidden("Your account is disabled.")
                
    else:
        # get request
        template = 'homecareapp/login.html'  
        context = { 'user_form': UserForm() }              
        return render(request, template, context)                                