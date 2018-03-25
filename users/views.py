from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def dispatch(self, *args, **kwargs):
        shib_username = self.request.session.get('shib', {}).get('username', None)
        if self.request.user.is_authenticated or shib_username is None:
            return redirect(reverse('home'))
        return super().dispatch(*args, **kwargs)
