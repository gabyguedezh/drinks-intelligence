from accounts.forms import (UserForm, UserLoginForm,
                            UserRegistrationForm)
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.views import generic
from tasks.views import has_piece


####################################################################################
#       Define class based view for index page, both POST and GET requests         #
####################################################################################

class IndexView(generic.DetailView):
    template_name = 'index.html'

    def get(self, request):
        piece_check = has_piece(request)
        return render(request, self.template_name, {'piece_check': piece_check})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

####################################################################################
#       Define class based view for logout page, both POST and GET requests         #
####################################################################################

@login_required
def logout(request):
    """ log the user out """
    auth.logout(request)
    return redirect(reverse('index'))

####################################################################################
#       Define class based view for index page, both POST and GET requests         #
####################################################################################

def login(request):
    """ user login """
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Username or password incorrect')
    
    else:
        login_form = UserLoginForm()
        
    return render(request, 'login.html', {'login_form': login_form})

####################################################################################
#       Define class based view for index page, both POST and GET requests         #
####################################################################################

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                return redirect(reverse('index'))
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
