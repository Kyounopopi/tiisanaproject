from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView,ListView,DetailView, UpdateView
from django.views import View
from .forms import CustomUserCreationForm,AccountUpdateForm
from django. urls import reverse_lazy
from .models import Customuser,Account
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



class AccountsView(LoginRequiredMixin, View):
    """"
    マイページ表示
    """
    login_url = '/accounts/login/'

    def get(self, request):
        try:
            account = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            account = Account.objects.create(user=request.user)
        context = {
            'account':account,
            'user':request.user
        }
        return render(request,'mypage.html',context)

class ProfileEditView(LoginRequiredMixin, View):
    """
    プロフィール編集
    """
    login_url = '/accounts/login/'
    
    def get(self, request):
        # Accountプロフィールを取得または作成
        try:
            account = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            account = Account.objects.create(user=request.user)
        
        form = AccountUpdateForm(instance=account)
        return render(request, 'profile_edit.html', {'form': form})
    
    def post(self, request):
        # Accountプロフィールを取得または作成
        try:
            account = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            account = Account.objects.create(user=request.user)
        
        form = AccountUpdateForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('accounts:mypages')
        
        return render(request, 'profile_edit.html', {'form': form})

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









