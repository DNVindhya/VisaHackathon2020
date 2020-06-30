from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_merchant:
            return redirect('merchdashboard/')
        elif request.user.is_consumer:
            return redirect('/customer/')
        else:
            return redirect('admin:index')
    return render(request, 'accounts/home.html')
