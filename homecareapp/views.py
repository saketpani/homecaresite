from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
import logging

def index(request):
    '''
    Home Page
    '''
    template = "homecareapp/index.html"
    context = {
        'page_content': PageContent.objects.filter(category='home').first()
    }

    return render(request, template, context)


def about(request):
    '''
    About Page
    '''
    template = "homecareapp/about.html"
    context = {
        'page_content': PageContent.objects.filter(category='about').first()
    }

    return render(request, template, context)


def faq(request):
    '''
    FAQ Page
    '''
    template = 'homecareapp/faq.html'
    faq_results = FAQ.objects.all()

    context = {
        'faq_results': faq_results
    }
    return render(request, template, context)


@login_required
def dashboard(request, id):
    return render(request, "homecareapp/dashboard.html")


@login_required
@require_http_methods(["GET", "POST"])
def search(request):

    if request.method == 'POST':
        search_input = request.POST.get('search_input')
        if search_input is None or search_input == '':
            return HttpResponseBadRequest('Invalid serach_input value.')

        option = request.POST.get('services')
        if option == None or option == 'all':
            search_results = (ServiceProvider.objects.filter(title__contains=search_input)
                              | ServiceProvider.objects.filter(pin__contains=search_input))

        else:
            search_results = ((ServiceProvider.objects.filter(title__contains=search_input)
                               | ServiceProvider.objects.filter(pin__contains=search_input))
                              & ServiceProvider.objects.filter(services__contains=option)
                              )

        template = 'homecareapp/searchResults.html'

        context = {
            'search_results': search_results,
            'care_services': CareService.objects.all()
        }

        return render(request, template, context)
    else:
        template = 'homecareapp/search.html'
        care_services = CareService.objects.all()

        context = {
            'care_services': care_services
        }
    return render(request, template, context)


@login_required
@require_http_methods(["GET"])
def service_provider_details(request, id):

    try:

        provider = ServiceProvider.objects.get(id=id)

        favourite = ''
        favourites = ServiceProvider_Favourite.objects.filter(
            user__id=request.user.id)
        for item in favourites:
            if item.service_provider.id == id:
                favourite = 'Yes'

        template = 'homecareapp/serviceProviderDetails.html'

        context = {
            'service_provider': provider,
            "favourite": favourite
        }

        return render(request, template, context)

    except ServiceProvider.DoesNotExist:
        return HttpResponseNotFound("The service provider is not found.")


@login_required
@require_http_methods(["GET"])
def saved_provider_details(request):
    try:

        favourites = ServiceProvider_Favourite.objects.filter(
            user__id=request.user.id)
        ids = [item.service_provider.id for item in favourites]

        search_results = ServiceProvider.objects.filter(pk__in=ids)
        template = 'homecareapp/savedserviceprovidercontacts.html'

        context = {
            'results': search_results,
        }

        return render(request, template, context)

    except ServiceProvider.DoesNotExist:
        return HttpResponseNotFound("The service provider is not found.")


@require_http_methods(["GET", "POST"])
def register(request):
    '''
    user registration view
    '''
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid():

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
            if 'date_of_birth' in user_form.cleaned_data:
                profile.date_of_birth = request.DATA['date_of_birth']
            profile.save()
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


# authentication
@require_http_methods(["GET", "POST"])
def register(request):
    '''
    user registration view
    '''
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid():

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
            if 'date_of_birth' in user_form.cleaned_data:
                profile.date_of_birth = request.DATA['date_of_birth']
            profile.save()
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


@login_required
@require_http_methods(["GET", "POST"])
def profile_edit(request, id):

    # validate that the user is updating their own profile only
    if request.user.id != id:
        logging.logger.error("you cannot update other user profile.")
        return redirect('/login/')

    if request.method == 'POST':
        profile = AppUser.objects.filter(user__id=request.user.id).first()
        profile_form = UserProfileEditForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/dashboard/{}'.format(request.user.id))
        else:
            print(profile_form.errors)
    else:
        profile = AppUser.objects.filter(user__id=request.user.id).first()
        profile_edit_form = UserProfileEditForm(instance=profile)        

        template = 'homecareapp/profile.html'
        context = {'profile_edit_form': profile_edit_form, 'user_id': id}
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
        context = {'user_form': UserForm()}
        return render(request, template, context)


@login_required
@require_http_methods(["GET"])
def user_logout(request):
    logout(request)
    return redirect('/login')
