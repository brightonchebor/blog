from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth import views 
from myapp.models import Profile

# Create your views here.
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #cat_menu = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context

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

