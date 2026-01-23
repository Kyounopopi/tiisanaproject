from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView,ListView
from .forms import CustomUserCreationForm
from django. urls import reverse_lazy
from .models import Customuser
from django.contrib.auth.decorators import login_required

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self, form):
        user = form.save()
        self.object = user

        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"


class AccountscreenView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts.html"
    success_url = reverse_lazy('accounts:account_itirann')

    def form_valid(self, form):
        user = form.save()
        self.object = user

        return super().form_valid(form)
    

class AccountView(ListView):
    template_nae='accounts.html'
    model = Customuser

    context_object_name ='orderby_records'

    queryset = Customuser.objects.filter(username='example')



@login_required
def account_view(request):
    user = request.user


    if user.user_type == 'general':
        
        try:
            profile = user.general_profile
            profile_type = '一般ユーザー'
        except GenerauUserPrlfile.DoesNotExist:
            profile = None
            profile_type = '一般ユーザー'

    else:
        profile = None
        prifile_type = '不明'

    context = {
        'user': user,
        'profile': profile,
        'profile_type':profile_type,
    }

    return render(request, 'accounts/accountscreen.html', context)









