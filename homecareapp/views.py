from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

def index(request):
    '''
    Home Page
    '''
    template = "homecareapp/index.html"         
    context = {
        'page_content' : PageContent.objects.filter(category='home').first()
    }    
    
    return render(request, template, context)

def about(request):
    '''
    About Page
    '''
    template = "homecareapp/about.html"         
    context = {
        'page_content' : PageContent.objects.filter(category='about').first()
    }    
    
    return render(request, template, context)    

def faq(request):
    '''
    FAQ Page
    '''
    template = 'homecareapp/faq.html'     
    faq_results = FAQ.objects.all;
     
    context = {
        'faq_results' : faq_results
    }    
    return render(request, template, context)            

@login_required
def dashboard(request, id):
    return render(request, "homecareapp/dashboard.html")

@login_required
def search(request):
    
    template = 'homecareapp/search.html'     
    care_services = CareService.objects.all;
     
    context = {
        'care_services' : care_services
    }    
    return render(request, template, context)     

@login_required
def searchResults(request):
    return render(request, "homecareapp/searchResults.html")

# authentication
@require_http_methods(["GET", "POST"])
def register(request):
    '''
    user registration view
    '''
    registered = False
    
    if request.method == 'POST':        
        user_form = UserForm(data=request.POST)        

        if user_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            # profile = profile_form.save(commit=False)
            # profile.user = user
           
            # if 'first_name' in user_form.cleaned_data:
            #     profile.first_name = request.DATA['first_name']
            # if 'last_name' in user_form.cleaned_data:
            #     profile.last_name = request.DATA['last_name']   
            # if 'mobile' in user_form.cleaned_data:
            #     profile.mobile = request.DATA['mobile']  
            # if 'date_of_birth' in user_form.cleaned_data:
            #     profile.date_of_birth = request.DATA['date_of_birth']     
            # if 'user_type' in user_form.cleaned_data:
            #     profile.date_of_birth = request.DATA['user_type']                                                                                                                                       
            # profile.save()            
            registered = True
            return redirect('login') 
            
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

@require_http_methods(["GET", "POST"])
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
            return redirect('/dashboard/{}'.format(request.user.id))  
        else:
            return HttpResponseForbidden("Your account is disabled.")
                
    else:
        # get request
        template = 'homecareapp/login.html'  
        context = { 'user_form': UserForm() }              
        return render(request, template, context)                                