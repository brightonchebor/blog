from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth import views 

# Create your views here.
def password_success(request):
    return render(request, 'registration/password_success.html', {})

class PasswordsChangeView(views.PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    #success_url = reverse_lazy('password_success')
    success_url = reverse_lazy('home')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user

