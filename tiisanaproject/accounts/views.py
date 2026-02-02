from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView,ListView,DetailView, UpdateView
from django.views import View
from .forms import CustomUserCreationForm,AccountUpdateForm,UserProfileForm
from django. urls import reverse_lazy
from .models import Customuser,Account,UserProfile
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

class ProfileListView(LoginRequiredMixin, View):
    """
    プロフィール一覧表示
    """

    model= UserProfile
    template_name='accounts/profile_list.html'
    login_url = '/accounts/login/'
    template_name = 'accounts/profile_list.html'
    
    def get(self, request):
        # ユーザーに紐づく全てのAccountプロフィールを取得
        profiles = Account.objects.filter(user=request.user)
        
        context = {
            'profiles': profiles
        }
        return render(request, self.template_name, context)


class ProfileCreateView(LoginRequiredMixin, View):
    """
    プロフィール作成
    """
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('accounts:mypages')
    login_url = '/accounts/login/'
    template_name = 'profile_create.html'
    
    

    def form_valid(self,form):
        form.instance.owner= self.request.user
        return super().form_valid(form)
    

    def get(self, request):
        # 既にAccountプロフィールが存在するか確認
       
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        # 既にAccountプロフィールが存在するか確認
        
    
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = request.user
            profile.save()
            return redirect('accounts:mypages')
        
        return render(request, self.template_name, {'form': form})


class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = 'mypage.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profiles = UserProfile.objects.filter(owner=self.request.user)

        active_profile = None
        active_id = self.request.session.get('active_profile_id')

        if active_id:
            active_profile = profiles.filter(id=active_id).first()

        if not active_profile and profiles.exists():
            active_profile = profiles.first()
            self.request.session['active_profile_id'] = active_profile.id

        context['profiles'] = profiles
        context['active_profile'] = active_profile

        return context


class SelectProfileView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request, profile_id):
        profile = get_object_or_404(
            UserProfile,
            id=profile_id,
            owner=request.user
        )

        # セッションに選択中プロフィールを保存
        request.session['active_profile_id'] = profile.id

        return redirect('accounts:mypages')
    


class ActivProfileUpdateView(LoginRequiredMixin, View):
    login_url='/accounts/login/'
    template_name = 'profile_edit.html'

    def get(self, request):
        active_id = request.session.get('active_profile_id')

        if not active_id:
            return redirect('accounts:mypages')

        profile = get_object_or_404(
            UserProfile,
            id=active_id,
            owner=request.user
        )

        form = UserProfileForm(instance=profile)
        return render(request, self.template_name, {
            'form': form,
            'profile': profile
        })

    def post(self, request):
        active_id = request.session.get('active_profile_id')

        if not active_id:
            return redirect('accounts:mypages')

        profile = get_object_or_404(
            UserProfile,
            id=active_id,
            owner=request.user
        )

        form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('accounts:mypages')

        return render(request, self.template_name, {
            'form': form,
            'profile': profile
        })


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









