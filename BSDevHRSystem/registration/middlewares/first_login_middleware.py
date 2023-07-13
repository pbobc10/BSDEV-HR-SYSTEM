from django.shortcuts import redirect
from django.urls import reverse

class FirstLoginMiddleWare:
    def __init__(self,get_reponse):
        self.get_response = get_reponse

    def __call__(self,request):
        user = request.user

        if user.is_authenticated and not user.last_login:
            print("test middleware 1")
            if request.path != reverse('accounts:change_password'):
                print("test middleware 2")
                return redirect('accounts:change_password')
            
        response = self.get_response(request)
        return response